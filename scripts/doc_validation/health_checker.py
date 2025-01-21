"""
Documentation health and coverage validation.

This module provides functionality to monitor and validate documentation health,
ensuring that:

1. All required sections are present in documents
2. Documentation coverage meets minimum standards
3. Terminology is used consistently
4. Critical sections are complete and well-formed

The checker uses configurable rules for different document types and maintains
statistics about documentation health over time.
"""

import re
import json
from pathlib import Path
from typing import Dict, List, Set, Tuple
from .validation_types import ValidationResult, Severity

class HealthChecker:
    """Validates documentation health and coverage.
    
    This class monitors documentation quality by checking for required sections,
    measuring coverage, and ensuring consistent terminology usage. It supports
    different requirements for different types of documentation.
    
    Attributes:
        docs_root: Root directory of documentation
        required_sections: Map of document types to their required sections
    """

    def __init__(self, docs_root: str):
        """Initialize the health checker.
        
        Args:
            docs_root: Path to documentation root directory
        """
        self.docs_root = Path(docs_root)
        self.required_sections = {
            'features': ['Purpose and Overview', 'Technical Implementation', 
                       'Cultural Integration', 'Testing Guidelines'],
            'systems': ['Overview', 'Architecture', 'Components', 
                      'Integration Points'],
            'api': ['Endpoints', 'Request/Response', 'Authentication', 
                   'Error Handling']
        }

    def validate(self) -> ValidationResult:
        """Run health checks and return results.
        
        Performs comprehensive health validation including:
        - Section coverage analysis
        - Terminology consistency checks
        - Documentation completeness validation
        
        Returns:
            ValidationResult containing health metrics and issues
        """
        result = ValidationResult()
        
        # Calculate coverage
        coverage, coverage_details = self._calculate_coverage()
        result.add_stat("coverage_percentage", coverage)
        result.add_stat("coverage_details", coverage_details)
        
        # Add coverage issues
        self._add_coverage_issues(coverage_details, result)
        
        # Check terminology consistency
        self._check_terminology(result)
        
        return result

    def _calculate_coverage(self) -> Tuple[float, Dict]:
        """Calculate documentation coverage percentage and details.
        
        Analyzes all documentation files to determine:
        - Percentage of required sections present
        - Missing sections in each document
        - Overall documentation completeness
        
        Returns:
            Tuple of (coverage percentage, detailed coverage information)
        """
        total_components = 0
        documented_components = 0
        coverage_details = {}

        for doc_type, required in self.required_sections.items():
            type_path = self.docs_root / doc_type
            if not type_path.exists():
                continue

            components = list(type_path.rglob("*.md"))
            total_components += len(components)
            
            for comp in components:
                content = comp.read_text()
                has_all_sections = all(
                    self._has_section(content, section)
                    for section in required
                )
                if has_all_sections:
                    documented_components += 1
                
                rel_path = str(comp.relative_to(self.docs_root))
                coverage_details[rel_path] = {
                    'has_all_sections': has_all_sections,
                    'missing_sections': [
                        section for section in required
                        if not self._has_section(content, section)
                    ]
                }

        coverage = (documented_components / total_components * 100 
                   if total_components > 0 else 0)
        return coverage, coverage_details

    def _has_section(self, content: str, section: str) -> bool:
        """Check if content has a specific section.
        
        Args:
            content: Document content to check
            section: Section name to look for
            
        Returns:
            True if section is present, False otherwise
        """
        patterns = [
            f"# {section}",
            f"## {section}",
            f"### {section}"
        ]
        return any(pattern in content for pattern in patterns)

    def _add_coverage_issues(self, coverage_details: Dict,
                           result: ValidationResult) -> None:
        """Add coverage-related issues to validation result.
        
        Args:
            coverage_details: Detailed coverage information
            result: ValidationResult to add issues to
        """
        for doc_path, details in coverage_details.items():
            if not details['has_all_sections']:
                result.add_issue(
                    f"Missing required sections: {', '.join(details['missing_sections'])}",
                    doc_path,
                    Severity.WARNING
                )

    def _check_terminology(self, result: ValidationResult) -> None:
        """Check terminology consistency across documents.
        
        Args:
            result: ValidationResult to add issues to
        """
        style_guide = self.docs_root / 'meta' / 'style-guide.md'
        
        if not style_guide.exists():
            result.add_issue(
                "Style guide not found - terminology consistency cannot be verified",
                "meta/style-guide.md",
                Severity.WARNING
            )
            return
            
        approved_terms = self._extract_approved_terms(style_guide.read_text())
        
        for md_file in self.docs_root.rglob("*.md"):
            if md_file == style_guide:
                continue
                
            doc_content = md_file.read_text()
            self._check_term_usage(doc_content, approved_terms, 
                                 str(md_file.relative_to(self.docs_root)),
                                 result)

    def _extract_approved_terms(self, content: str) -> Dict[str, Dict]:
        """Extract approved terminology from style guide.
        
        Args:
            content: Style guide content
            
        Returns:
            Dictionary of approved terms and their usage rules
        """
        terms = {}
        
        # Extract technical terms
        term_section = re.search(
            r'## Technical Terminology\n(.*?)(?=\n#|\Z)',
            content,
            re.DOTALL
        )
        if term_section:
            terms.update(self._parse_term_section(term_section.group(1)))
        
        # Extract cultural terms
        cultural_section = re.search(
            r'## Cultural Terminology\n(.*?)(?=\n#|\Z)',
            content,
            re.DOTALL
        )
        if cultural_section:
            terms.update(self._parse_term_section(cultural_section.group(1)))
        
        return terms

    def _parse_term_section(self, section: str) -> Dict[str, Dict]:
        """Parse a terminology section into structured data.
        
        Args:
            section: Raw terminology section content
            
        Returns:
            Dictionary of terms and their definitions/usage rules
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

    def _check_term_usage(self, content: str, approved_terms: Dict[str, Dict],
                         file_path: str, result: ValidationResult) -> None:
        """Check content for terminology consistency.
        
        Args:
            content: Document content to check
            approved_terms: Dictionary of approved terms
            file_path: Path to the document being checked
            result: ValidationResult to add issues to
        """
        for term, details in approved_terms.items():
            variations = self._find_term_variations(content, term)
            if variations - {term}:
                result.add_issue(
                    f"Inconsistent usage of '{term}': found variations {variations}",
                    file_path,
                    Severity.WARNING
                )

    def _find_term_variations(self, content: str, term: str) -> Set[str]:
        """Find variations of a term in content.
        
        Args:
            content: Text to search for variations
            term: Base term to find variations of
            
        Returns:
            Set of term variations found in the content
        """
        variations = set()
        pattern = f"{term}|{term.lower()}|{term.upper()}|{term.title()}"
        variations.update(re.findall(pattern, content))
        return variations
