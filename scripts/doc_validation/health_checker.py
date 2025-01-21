"""
Documentation health checker.

Validates documentation health by:
1. Checking for required sections
2. Measuring documentation coverage
3. Validating metadata presence
"""

import re
from pathlib import Path
from typing import Dict, List, Set

from .validation_types import ValidationResult, ValidationIssue, Severity

class HealthChecker:
    """Checks documentation health and coverage."""

    def __init__(self, docs_root: str):
        """Initialize the health checker.
        
        Args:
            docs_root: Root directory containing documentation files
        """
        self.docs_root = Path(docs_root)
        
        # Define required sections by doc type
        self.required_sections = {
            'technical': {
                'Overview',
                'Implementation',
                'Usage',
                'Configuration'
            },
            'overview': {
                'Introduction',
                'Key Features',
                'Architecture'
            },
            'world_building': {
                'Overview',
                'Mechanics',
                'Balancing'
            }
        }
        
        # Define expected metadata fields
        self.required_metadata = {
            'title',
            'description',
            'last_updated'
        }

    def _get_doc_type(self, file_path: Path) -> str:
        """Determine document type from path.
        
        Args:
            file_path: Path to document
            
        Returns:
            Document type (technical, overview, world_building)
        """
        rel_path = file_path.relative_to(self.docs_root)
        parts = rel_path.parts
        
        if len(parts) > 0:
            if parts[0] in self.required_sections:
                return parts[0]
        return 'other'

    def _extract_sections(self, content: str) -> Set[str]:
        """Extract section headers from content.
        
        Args:
            content: Document content
            
        Returns:
            Set of section names
        """
        headers = re.findall(r'^#+\s+(.+)$', content, re.MULTILINE)
        return {h.strip() for h in headers}

    def _extract_metadata(self, content: str) -> Dict[str, str]:
        """Extract YAML metadata from content.
        
        Args:
            content: Document content
            
        Returns:
            Dictionary of metadata fields
        """
        metadata = {}
        meta_match = re.match(r'---\n(.*?)\n---', content, re.DOTALL)
        if meta_match:
            meta_text = meta_match.group(1)
            for line in meta_text.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    metadata[key.strip()] = value.strip()
        return metadata

    def _calculate_coverage(self, sections: Set[str], required: Set[str]) -> float:
        """Calculate section coverage percentage.
        
        Args:
            sections: Found sections
            required: Required sections
            
        Returns:
            Coverage percentage (0-100)
        """
        if not required:
            return 100.0
        return len(sections.intersection(required)) / len(required) * 100

    def validate(self) -> ValidationResult:
        """Validate documentation health.
        
        Returns:
            ValidationResult containing health issues and statistics
        """
        result = ValidationResult()
        total_coverage = 0.0
        doc_count = 0
        
        for md_file in self.docs_root.rglob('*.md'):
            try:
                content = md_file.read_text(encoding='utf-8')
                rel_path = str(md_file.relative_to(self.docs_root))
                
                # Check sections
                doc_type = self._get_doc_type(md_file)
                if doc_type in self.required_sections:
                    sections = self._extract_sections(content)
                    required = self.required_sections[doc_type]
                    
                    # Calculate coverage
                    coverage = self._calculate_coverage(sections, required)
                    total_coverage += coverage
                    doc_count += 1
                    
                    # Check missing sections
                    missing = required - sections
                    if missing:
                        result.issues.append(ValidationIssue(
                            message=f'Missing required sections: {", ".join(missing)}',
                            file=rel_path,
                            severity=Severity.WARNING
                        ))
                
                # Check metadata
                metadata = self._extract_metadata(content)
                missing_meta = self.required_metadata - set(metadata.keys())
                if missing_meta:
                    result.issues.append(ValidationIssue(
                        message=f'Missing metadata fields: {", ".join(missing_meta)}',
                        file=rel_path,
                        severity=Severity.WARNING
                    ))
                    
            except Exception as e:
                result.issues.append(ValidationIssue(
                    message=f'Error processing file: {str(e)}',
                    file=rel_path,
                    severity=Severity.ERROR
                ))
        
        # Calculate overall coverage
        result.stats['coverage_percentage'] = (
            total_coverage / doc_count if doc_count > 0 else 0
        )
        
        return result
