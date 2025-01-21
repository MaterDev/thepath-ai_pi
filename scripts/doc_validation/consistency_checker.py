"""
Terminology consistency validation for documentation.

This module provides functionality to validate terminology consistency across
documentation files, ensuring that:

1. Technical terms are used correctly and consistently
2. Cultural terminology adheres to style guide rules
3. Terminology variations are caught and flagged
4. Style guide rules are properly enforced

The checker uses the style guide as a source of truth for approved terminology
and validates all documentation against these rules.
"""

import re
from pathlib import Path
from typing import Dict, List, Set
from .validation_types import ValidationResult, Severity

class ConsistencyChecker:
    """Validates terminology consistency across documentation.
    
    This class ensures that terminology is used consistently throughout the
    documentation by checking against rules defined in the style guide. It
    handles both technical and cultural terminology.
    
    Attributes:
        docs_root: Root directory of documentation
        style_guide: Path to the style guide file
        technical_terms: Dictionary of approved technical terms
        cultural_terms: Dictionary of approved cultural terms
    """

    def __init__(self, docs_root: str):
        """Initialize the consistency checker.
        
        Args:
            docs_root: Path to documentation root directory
        """
        self.docs_root = Path(docs_root)
        self.style_guide = self.docs_root / 'meta' / 'style-guide.md'
        self.technical_terms = {}
        self.cultural_terms = {}

    def validate(self) -> ValidationResult:
        """Run consistency checks and return results.
        
        Performs comprehensive terminology validation including:
        - Loading terminology guidelines
        - Checking technical term usage
        - Validating cultural terminology
        - Tracking terminology statistics
        
        Returns:
            ValidationResult containing consistency issues and statistics
        """
        result = ValidationResult()
        
        if not self.style_guide.exists():
            result.add_issue(
                "Style guide not found",
                str(self.style_guide.relative_to(self.docs_root)),
                Severity.WARNING
            )
            return result
        
        # Load terminology guidelines
        self._load_guidelines()
        
        # Track statistics
        result.add_stat("technical_terms", len(self.technical_terms))
        result.add_stat("cultural_terms", len(self.cultural_terms))
        
        # Check all documents
        self._check_all_documents(result)
        
        return result

    def _load_guidelines(self) -> None:
        """Load terminology guidelines from style guide.
        
        Extracts both technical and cultural terminology rules from the
        style guide and organizes them into structured dictionaries for
        validation.
        """
        content = self.style_guide.read_text()
        
        # Extract technical terms
        tech_section = re.search(
            r'## Technical Terminology\n(.*?)(?=\n#|\Z)',
            content,
            re.DOTALL
        )
        if tech_section:
            self.technical_terms = self._parse_term_section(tech_section.group(1))
        
        # Extract cultural terms
        cultural_section = re.search(
            r'## Cultural Terminology\n(.*?)(?=\n#|\Z)',
            content,
            re.DOTALL
        )
        if cultural_section:
            self.cultural_terms = self._parse_term_section(cultural_section.group(1))

    def _parse_term_section(self, section: str) -> Dict[str, Dict]:
        """Parse a terminology section into structured data.
        
        Args:
            section: Raw terminology section content
            
        Returns:
            Dictionary mapping terms to their usage rules
        """
        terms = {}
        current_term = None
        
        for line in section.split('\n'):
            if line.startswith('### '):
                current_term = line[4:].strip()
                terms[current_term] = {
                    'definition': '',
                    'usage': [],
                    'avoid': []
                }
            elif current_term:
                if line.startswith('Definition:'):
                    terms[current_term]['definition'] = line[11:].strip()
                elif line.startswith('- Use:'):
                    terms[current_term]['usage'].append(line[7:].strip())
                elif line.startswith('- Avoid:'):
                    terms[current_term]['avoid'].append(line[9:].strip())
        
        return terms

    def _check_all_documents(self, result: ValidationResult) -> None:
        """Check all documentation files for terminology consistency.
        
        Args:
            result: ValidationResult to add issues to
        """
        for md_file in self.docs_root.rglob("*.md"):
            if md_file == self.style_guide:
                continue
            
            rel_path = str(md_file.relative_to(self.docs_root))
            content = md_file.read_text()
            
            # Check technical terms
            for term, details in self.technical_terms.items():
                self._check_term_usage(
                    content, term, details, 'technical',
                    rel_path, result
                )
            
            # Check cultural terms
            for term, details in self.cultural_terms.items():
                self._check_term_usage(
                    content, term, details, 'cultural',
                    rel_path, result
                )

    def _check_term_usage(self, content: str, term: str, 
                         details: Dict, term_type: str,
                         file_path: str, result: ValidationResult) -> None:
        """Check usage of a specific term in content.
        
        Args:
            content: Document content to check
            term: Term to validate
            details: Term usage rules and patterns
            term_type: Type of term (technical/cultural)
            file_path: Path to document being checked
            result: ValidationResult to add issues to
        """
        # Check for incorrect variations
        for avoid in details['avoid']:
            matches = re.finditer(avoid, content, re.IGNORECASE)
            for match in matches:
                result.add_issue(
                    f"Used '{match.group()}' instead of '{term}'",
                    file_path,
                    Severity.WARNING,
                    self._get_line_number(content, match.start()),
                    f"{term_type} term"
                )
        
        # Check for proper usage patterns
        if details['usage']:
            proper_usage = False
            for usage in details['usage']:
                if re.search(usage, content, re.IGNORECASE):
                    proper_usage = True
                    break
            
            if not proper_usage and re.search(term, content, re.IGNORECASE):
                match = re.search(term, content, re.IGNORECASE)
                result.add_issue(
                    f"Term '{term}' used outside of approved patterns",
                    file_path,
                    Severity.WARNING,
                    self._get_line_number(content, match.start()),
                    f"{term_type} term"
                )

    def _get_line_number(self, content: str, pos: int) -> int:
        """Get line number for a position in content.
        
        Args:
            content: Text content to analyze
            pos: Character position in content
            
        Returns:
            Line number (1-based) containing the position
        """
        return content.count('\n', 0, pos) + 1
