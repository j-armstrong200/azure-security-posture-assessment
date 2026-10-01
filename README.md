# azure-security-posture-assessment
Python-based Azure security posture assessment project for identifying cloud security misconfigurations and generating security findings.

## Overview

This project simulates an Azure cloud security posture assessment using Python. The script analyzes sample Azure resource configurations to identify potential security misconfigurations related to public access, HTTPS enforcement, and encryption.

The goal of the project is to demonstrate basic cloud security assessment concepts, automated security checks, severity classification, and remediation recommendations.

## Security Checks

The Python script checks for:

- Storage Accounts with public access enabled
- Storage Accounts that do not require HTTPS
- Storage Accounts with encryption disabled
- Assigns severity levels to identified security findings
- Provides remediation recommendations for identified security issues
- Generates a CSV report containing the assessment results

## Technologies and Concepts

- Python
- Microsoft Azure
- Cloud Security
- Security Posture Assessment
- Security Misconfiguration Detection
- Data Encryption
- HTTPS Enforcement
- Public Access Controls
- Risk Severity Classification
- Security Remediation
- CSV Data Analysis
- Security Reporting

## Sample Findings

The assessment identifies findings such as:

```text
HIGH: client-files-storage is a Storage Account with public access enabled!
MEDIUM: legacy-storage does not require HTTPS!
HIGH: backup-storage does not have encryption enabled!
```

## Files

- security_assessment.py - Python script that performs the Azure security assessment
- azure_resources.csv - Sample Azure resource configuration data
- security_findings.csv - Automatically generated security findings report with severity levels and remediation recommendations
- README.md - Project documentation

## What I Learned

This project helped me practice using Python to automate a basic cloud security posture assessment. I learned how to analyze Azure resource configuration data, identify security misconfigurations, assign severity levels, and generate remediation recommendations.

I also gained experience with public access controls, HTTPS enforcement, encryption, automated security reporting, and debugging Python logic to ensure assessment findings are accurate.

## Disclaimer

This project uses fictional sample Azure resource data and is intended for educational and portfolio purposes only.
