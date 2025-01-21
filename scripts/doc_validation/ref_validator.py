"""
Reference validation for documentation integrity.

This module provides functionality to validate cross-references within documentation,
ensuring that:

1. All references point to existing files
2. No circular references exist
3. Reference chains don't exceed maximum depth
4. References in YAML blocks are valid

The validator handles both markdown-style links and references within YAML blocks,
making it suitable for validating both content and configuration files.
"""

import re
import yaml
from pathlib import Path
from typing import Dict, Set, List
from .validation_types import ValidationResult, Severity

class RefValidator:
    """Validates cross-references in documentation files.
    
    This class scans markdown files for references to other documents and ensures
    they maintain a healthy reference structure. It checks for issues like broken
    links, circular references, and overly deep reference chains.
    
    Attributes:
        docs_root: Root directory of documentation
        reference_map: Map of documents to their references
        max_depth: Maximum allowed depth for reference chains
    """

    def __init__(self, docs_root: str):
        """Initialize the validator.
        
        Args:
            docs_root: Path to documentation root directory
        """
        self.docs_root = Path(docs_root)
        self.reference_map: Dict[str, Set[str]] = {}
        self.max_depth = 3  # Maximum allowed reference depth

    def validate(self) -> ValidationResult:
        """Run validation and return results.
        
        Returns:
            ValidationResult containing any issues found and reference statistics
        """
        result = ValidationResult()
        
        # Build reference map
        self._scan_documents()
        
        # Track statistics
        total_refs = sum(len(refs) for refs in self.reference_map.values())
        result.add_stat("total_references", total_refs)
        result.add_stat("total_documents", len(self.reference_map))
        
        # Validate references
        self._validate_references(result)
        
        return result

    def _scan_documents(self) -> None:
        """Scan all markdown documents and build reference map.
        
        This method walks through all markdown files in the documentation tree
        and extracts references from both markdown links and YAML blocks.
        """
        for md_file in self.docs_root.rglob("*.md"):
            refs = self._extract_references(md_file)
            self.reference_map[str(md_file.relative_to(self.docs_root))] = refs

    def _extract_references(self, file_path: Path) -> Set[str]:
        """Extract all references from a markdown file.
        
        Args:
            file_path: Path to the markdown file
            
        Returns:
            Set of referenced file paths
        """
        refs = set()
        content = file_path.read_text()
        
        # Extract markdown links
        self._extract_markdown_refs(content, refs)
        
        # Extract YAML references
        self._extract_yaml_blocks(content, refs)
        
        return refs

    def _extract_markdown_refs(self, content: str, refs: Set[str]) -> None:
        """Extract references from markdown links.
        
        Args:
            content: File content to scan
            refs: Set to add found references to
        """
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        for _, path in re.findall(link_pattern, content):
            if not path.startswith(('http://', 'https://')):
                refs.add(path)

    def _extract_yaml_blocks(self, content: str, refs: Set[str]) -> None:
        """Extract references from YAML code blocks.
        
        Args:
            content: File content to scan
            refs: Set to add found references to
        """
        yaml_blocks = re.findall(r'```yaml\n(.*?)\n```', content, re.DOTALL)
        for block in yaml_blocks:
            try:
                data = yaml.safe_load(block)
                refs.update(self._extract_yaml_refs(data))
            except yaml.YAMLError:
                pass

    def _extract_yaml_refs(self, data: dict) -> Set[str]:
        """Extract references from YAML data structure.
        
        Args:
            data: YAML data to scan
            
        Returns:
            Set of referenced file paths
        """
        refs = set()
        if isinstance(data, dict):
            for value in data.values():
                if isinstance(value, str) and value.endswith('.md'):
                    refs.add(value)
                elif isinstance(value, (dict, list)):
                    refs.update(self._extract_yaml_refs(value))
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, (dict, list)):
                    refs.update(self._extract_yaml_refs(item))
                elif isinstance(item, str) and item.endswith('.md'):
                    refs.add(item)
        return refs

    def _validate_references(self, result: ValidationResult) -> None:
        """Perform all reference validations.
        
        Args:
            result: ValidationResult to add issues to
        """
        # Check for broken links
        self._check_broken_links(result)
        
        # Check for circular references
        for source in self.reference_map:
            self._check_circular(source, [], result)
        
        # Check reference depth
        for source in self.reference_map:
            depth = self._check_depth(source, set())
            if depth > self.max_depth:
                result.add_issue(
                    f"Reference chain too deep (depth: {depth}, max: {self.max_depth})",
                    source,
                    Severity.WARNING
                )

    def _check_broken_links(self, result: ValidationResult) -> None:
        """Check for broken links in all documents.
        
        Args:
            result: ValidationResult to add issues to
        """
        for source, refs in self.reference_map.items():
            for ref in refs:
                target = self.docs_root / ref
                if not target.exists():
                    result.add_issue(
                        f"Broken reference to '{ref}'",
                        source,
                        Severity.ERROR
                    )

    def _check_circular(self, current: str, path: List[str], 
                       result: ValidationResult) -> None:
        """Check for circular references starting from current document.
        
        Args:
            current: Current document being checked
            path: Current reference path
            result: ValidationResult to add issues to
        """
        if current in path:
            cycle = ' -> '.join(path[path.index(current):] + [current])
            result.add_issue(
                f"Circular reference detected: {cycle}",
                current,
                Severity.ERROR,
                context=cycle
            )
            return

        path.append(current)
        for ref in self.reference_map.get(current, set()):
            self._check_circular(ref, path.copy(), result)

    def _check_depth(self, current: str, visited: Set[str]) -> int:
        """Check the maximum reference depth from current document.
        
        Args:
            current: Current document being checked
            visited: Set of already visited documents
            
        Returns:
            Maximum depth of reference chain
        """
        if current in visited:
            return 0
        
        visited.add(current)
        max_depth = 0
        
        for ref in self.reference_map.get(current, set()):
            depth = self._check_depth(ref, visited.copy())
            max_depth = max(max_depth, depth)
        
        return max_depth + 1
