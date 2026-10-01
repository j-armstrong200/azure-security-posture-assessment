import csv

findings = []

with open("azure_resources.csv", newline="") as file:
    reader = csv.DictReader(file)

    for resource in reader:
        print(resource)
