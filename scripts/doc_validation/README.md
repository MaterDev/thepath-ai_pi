# Documentation Validation Package

This package provides a comprehensive set of tools for validating documentation in the agenic context system. It helps maintain documentation quality, consistency, and integrity through automated validation checks.

## Components

### 1. Core Validation Types (`validation_types.py`)
- Defines common data structures for validation results
- Provides severity levels for issues
- Implements result collection and statistics

### 2. Reference Validator (`ref_validator.py`)
Validates documentation cross-references:
- Checks for broken links
- Detects circular references
- Monitors reference depth
- Validates YAML references

### 3. Health Checker (`health_checker.py`)
Monitors documentation health:
- Tracks section coverage
- Validates required content
- Monitors documentation completeness
- Tracks historical metrics

### 4. Consistency Checker (`consistency_checker.py`)
Ensures terminology consistency:
- Validates technical terms
- Checks cultural terminology
- Enforces style guide rules
- Prevents terminology drift

## Integration

These validation components are designed to work together through the main validation script (`validate_docs.py`). The script:

1. Runs all validations
2. Collects and aggregates results
3. Generates comprehensive reports
4. Saves results to temporary storage
5. Provides terminal output

## Usage

The validation package is typically used through the main validation script:

```bash
./validate_docs.py /path/to/docs
```

This will:
1. Run all validation checks
2. Generate a comprehensive report
3. Save results to `/tmp/doc_validation/`
4. Display results in the terminal
5. Exit with appropriate status code

## Output

The validation process generates two types of output:

1. Human-readable report (`validation_report_TIMESTAMP.txt`)
   - Summary statistics
   - Detailed validation results
   - Issue descriptions and locations

2. JSON results (`validation_results_TIMESTAMP.json`)
   - Raw validation data
   - Detailed statistics
   - Machine-readable format

## Best Practices

1. Run validations before committing documentation changes
2. Review all validation reports carefully
3. Address errors before warnings
4. Keep the style guide updated
5. Monitor documentation health trends

## Implementation Notes

- All validators return `ValidationResult` objects
- Results include both issues and statistics
- Issues are categorized by severity
- File paths are stored relative to docs root
- JSON output preserves all validation details
