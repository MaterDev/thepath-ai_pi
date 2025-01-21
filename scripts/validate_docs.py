#!/usr/bin/env python3
"""
Documentation validation script for the agenic context system.

This script provides a unified interface for running all documentation validation
checks and generating comprehensive reports. It:

1. Runs all validation checks (references, health, consistency)
2. Generates detailed reports with issues and statistics
3. Saves results to a temporary directory for tracking
4. Provides clear terminal output for immediate feedback

The script is designed to be run both manually and as part of development
workflows to maintain high documentation quality.
"""

import sys
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List

from doc_validation import (
    RefValidator,
    HealthChecker,
    ConsistencyChecker,
    ValidationResult,
    Severity
)

class ValidationReporter:
    """Manages documentation validation and reporting.
    
    This class coordinates running all validation checks and generates
    comprehensive reports in both human-readable and machine-readable formats.
    
    Attributes:
        docs_root: Root directory of documentation
        temp_dir: Directory for storing validation results
    """

    def __init__(self, docs_root: str):
        """Initialize the validation reporter.
        
        Args:
            docs_root: Path to documentation root directory
        """
        self.docs_root = Path(docs_root)
        self.temp_dir = Path("/tmp/doc_validation")
        self.temp_dir.mkdir(parents=True, exist_ok=True)

    def run_validations(self) -> Dict[str, ValidationResult]:
        """Run all validation checks.
        
        Executes each validator in sequence and collects their results.
        
        Returns:
            Dictionary mapping validator names to their results
        """
        return {
            "references": RefValidator(self.docs_root).validate(),
            "health": HealthChecker(self.docs_root).validate(),
            "consistency": ConsistencyChecker(self.docs_root).validate()
        }

    def generate_report(self, results: Dict[str, ValidationResult]) -> str:
        """Generate a human-readable report.
        
        Creates a detailed report including:
        - Overall summary statistics
        - Results from each validator
        - Detailed issue descriptions
        - Relevant context and locations
        
        Args:
            results: Dictionary of validation results
            
        Returns:
            Formatted report string
        """
        lines = [
            "Documentation Validation Report",
            f"Generated: {datetime.now().isoformat()}",
            "",
            "Summary:",
            "--------"
        ]

        # Add summary statistics
        total_errors = sum(r.error_count for r in results.values())
        total_warnings = sum(r.warning_count for r in results.values())
        lines.extend([
            f"Total Errors: {total_errors}",
            f"Total Warnings: {total_warnings}",
            ""
        ])

        # Add detailed results for each validator
        for validator_name, result in results.items():
            lines.extend([
                f"{validator_name.title()} Validation",
                "-" * (len(validator_name) + 11),
                f"Errors: {result.error_count}",
                f"Warnings: {result.warning_count}",
                ""
            ])

            # Add statistics
            if result.stats:
                lines.append("Statistics:")
                for key, value in result.stats.items():
                    if isinstance(value, (int, float, str, bool)):
                        lines.append(f"- {key}: {value}")
                lines.append("")

            # Add issues
            if result.issues:
                lines.append("Issues:")
                for issue in result.issues:
                    prefix = "ERROR" if issue.severity == Severity.ERROR else "WARNING"
                    location = f"{issue.file}"
                    if issue.line:
                        location += f" (line {issue.line})"
                    
                    lines.append(f"[{prefix}] {location}")
                    lines.append(f"  {issue.message}")
                    if issue.context:
                        lines.append(f"  Context: {issue.context}")
                lines.append("")

        return "\n".join(lines)

    def save_report(self, report: str, results: Dict[str, ValidationResult]) -> None:
        """Save the report and raw results.
        
        Saves both human-readable and machine-readable versions of the results:
        1. Text report for human consumption
        2. JSON data for programmatic analysis
        
        Args:
            report: Generated human-readable report
            results: Raw validation results
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Save human-readable report
        report_file = self.temp_dir / f"validation_report_{timestamp}.txt"
        report_file.write_text(report)
        
        # Save raw results as JSON
        json_results = {
            name: {
                "timestamp": result.timestamp.isoformat(),
                "stats": result.stats,
                "issues": [
                    {
                        "message": i.message,
                        "file": i.file,
                        "line": i.line,
                        "severity": i.severity.value,
                        "context": i.context
                    }
                    for i in result.issues
                ]
            }
            for name, result in results.items()
        }
        
        json_file = self.temp_dir / f"validation_results_{timestamp}.json"
        json_file.write_text(json.dumps(json_results, indent=2))

def main():
    """Main entry point for the validation script.
    
    Usage:
        validate_docs.py <docs_root>
    
    The script will:
    1. Run all validations
    2. Generate and display a report
    3. Save results to /tmp/doc_validation/
    4. Exit with status 1 if any errors were found
    """
    if len(sys.argv) != 2:
        print("Usage: validate_docs.py <docs_root>")
        sys.exit(1)

    docs_root = sys.argv[1]
    reporter = ValidationReporter(docs_root)
    
    print("Running documentation validation...")
    results = reporter.run_validations()
    
    print("\nGenerating report...")
    report = reporter.generate_report(results)
    
    print("\nSaving results...")
    reporter.save_report(report, results)
    
    # Print report to terminal
    print("\n" + report)
    
    # Exit with error if any validation had errors
    has_errors = any(r.error_count > 0 for r in results.values())
    sys.exit(1 if has_errors else 0)

if __name__ == "__main__":
    main()
