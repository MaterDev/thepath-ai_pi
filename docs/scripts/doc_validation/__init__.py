"""Documentation validation package.

This package provides tools for validating documentation:
1. Reference validation - check links between documents
2. Health checks - verify required sections and metadata
"""

from .validation_types import ValidationResult, ValidationIssue, Severity
from .ref_validator import RefValidator
from .health_checker import HealthChecker

__all__ = [
    'ValidationResult',
    'ValidationIssue',
    'Severity',
    'RefValidator',
    'HealthChecker'
]
