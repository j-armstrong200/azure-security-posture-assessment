import csv

findings = []

with open("azure_resources.csv", newline="") as file:
    reader = csv.DictReader(file)

    for resource in reader:
        if resource["resource_type"] == "Storage Account" and resource["public_access"] == "Yes":
            print("HIGH:", resource["resource_name"], "is a Storage Account with public access enabled!")
            findings.append({
                "resource_name": resource["resource_name"],
                "severity": "High",
                "finding": "Storage Account with public access enabled"
    })

        if resource["resource_type"] == "Storage Account" and resource["https_only"] == "No":
            print("MEDIUM:", resource["resource_name"], "does not require HTTPS!")
            findings.append({
                "resource_name": resource["resource_name"],
                "severity": "Medium",
                "finding": "Storage Account does not require HTTPS"
    })

        if resource["resource_type"] == "Storage Account" and resource["encryption_enabled"] == "No":
            print("HIGH:", resource["resource_name"], "does not have encryption enabled!")
            findings.append({
                "resource_name": resource["resource_name"],
                "severity": "High",
            "finding": "Storage Account encryption is disabled"
    })

    with open("security_findings.csv", "w", newline="") as report_file:
        fieldnames = ["resource_name", "severity", "finding"]
        writer = csv.DictWriter(report_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(findings)