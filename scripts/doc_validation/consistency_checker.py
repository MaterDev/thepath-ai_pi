"""Terminology consistency checker.

Validates terminology consistency by:
1. Loading style guide definitions
2. Checking technical term usage
3. Validating cultural terminology
4. Ensuring consistent capitalization
"""

import re
from pathlib import Path
from typing import Dict, Set, List, Optional

from .validation_types import ValidationResult, ValidationIssue, Severity

class ConsistencyChecker:
    """Checks terminology consistency across documentation."""

    def __init__(self, docs_root: str):
        """Initialize the consistency checker.
        
        Args:
            docs_root: Root directory containing documentation files
        """
        self.docs_root = Path(docs_root)
        self.style_guide_path = self.docs_root / 'meta' / 'style-guide.md'

    def _load_style_guide(self) -> Dict[str, Dict]:
        """Load and parse the style guide.
        
        Returns:
            Dictionary of term definitions and rules
        """
        if not self.style_guide_path.exists():
            return {}
            
        content = self.style_guide_path.read_text(encoding='utf-8')
        terms = {}
        
        # Extract term sections
        sections = {
            'technical': self._extract_section(content, 'Technical Terms'),
            'cultural': self._extract_section(content, 'Cultural Terms')
        }
        
        # Parse each section
        for section_type, section_content in sections.items():
            if section_content:
                terms.update(self._parse_terms(section_content, section_type))
                
        return terms

    def _extract_section(self, content: str, section_name: str) -> Optional[str]:
        """Extract a named section from content.
        
        Args:
            content: Full document content
            section_name: Name of section to extract
            
        Returns:
            Section content if found, None otherwise
        """
        pattern = rf'(?:^|\n)#+ {section_name}\n(.*?)(?:\n#|\Z)'
        match = re.search(pattern, content, re.DOTALL)
        return match.group(1).strip() if match else None

    def _parse_terms(self, section: str, term_type: str) -> Dict[str, Dict]:
        """Parse terms from a section.
        
        Args:
            section: Section content to parse
            term_type: Type of terms (technical/cultural)
            
        Returns:
            Dictionary of parsed terms
        """
        terms = {}
        current_term = None
        current_def = {}
        
        for line in section.split('\n'):
            line = line.strip()
            if not line:
                continue
                
            # New term definition
            if line.startswith('#'):
                if current_term:
                    terms[current_term] = current_def
                current_term = line.lstrip('#').strip()
                current_def = {'type': term_type, 'alternatives': set()}
                
            # Term properties
            elif current_term:
                if ':' in line:
                    key, value = line.split(':', 1)
                    key = key.strip().lower()
                    value = value.strip()
                    
                    if key == 'use':
                        current_def['preferred'] = value
                    elif key == 'avoid':
                        current_def['alternatives'].update(
                            v.strip() for v in value.split(',')
                        )
                    else:
                        current_def[key] = value
                        
        # Add final term
        if current_term:
            terms[current_term] = current_def
            
        return terms

    def _check_term_usage(self, content: str, terms: Dict[str, Dict],
                         file_path: str) -> List[ValidationIssue]:
        """Check content for term usage issues.
        
        Args:
            content: Content to check
            terms: Dictionary of term definitions
            file_path: Path to file being checked
            
        Returns:
            List of validation issues found
        """
        issues = []
        
        for term, definition in terms.items():
            # Skip if no preferred usage defined
            if 'preferred' not in definition:
                continue
                
            # Find all variations of the term
            pattern = rf'\b({term}|{"".join(definition["alternatives"])})\b'
            matches = re.finditer(pattern, content, re.IGNORECASE)
            
            for match in matches:
                used_term = match.group(1)
                if used_term != definition['preferred']:
                    issues.append(ValidationIssue(
                        message=(
                            f'Inconsistent terminology: found "{used_term}", '
                            f'use "{definition["preferred"]}" instead'
                        ),
                        file=file_path,
                        severity=Severity.WARNING,
                        line=content.count('\n', 0, match.start()) + 1
                    ))
                    
        return issues

    def validate(self) -> ValidationResult:
        """Validate terminology consistency.
        
        Returns:
            ValidationResult containing consistency issues
        """
        result = ValidationResult()
        
        # Load style guide
        terms = self._load_style_guide()
        if not terms:
            result.stats.update({
                'technical_terms': 0,
                'cultural_terms': 0
            })
            return result
            
        # Count terms by type
        result.stats.update({
            'technical_terms': sum(1 for t in terms.values() 
                                 if t['type'] == 'technical'),
            'cultural_terms': sum(1 for t in terms.values() 
                                if t['type'] == 'cultural')
        })
        
        # Check all markdown files
        for md_file in self.docs_root.rglob('*.md'):
            # Skip style guide itself
            if md_file == self.style_guide_path:
                continue
                
            try:
                content = md_file.read_text(encoding='utf-8')
                rel_path = str(md_file.relative_to(self.docs_root))
                
                # Check terminology
                issues = self._check_term_usage(content, terms, rel_path)
                result.issues.extend(issues)
                
            except Exception as e:
                result.issues.append(ValidationIssue(
                    message=f'Error processing file: {str(e)}',
                    file=rel_path,
                    severity=Severity.ERROR
                ))
                
        return result
