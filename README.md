# NessusJenius

Don't be a Nessus zero - use Jen's genius script to parse your scan results.

## Overview

NessusJenius is a Python script that parses Nessus scan results in XML format and generates a CSV file containing information about the hosts, ports, and vulnerabilities detected in the scan.

## Requirements

- Python 3.5 or later
- lxml library

## Usage

1. Clone the repository:
git clone https://github.com/<username>/NessusJenius.git

2. Install the required libraries:
pip install -r requirements.txt

3. Run the script: python nessusjenius.py -d /path/to/nessus/files -o output.csv


Replace `/path/to/nessus/files` with the path to the directory containing your Nessus scan files, and `output.csv` with the name of the CSV file you want to generate.

The script will parse all Nessus scan files in the specified directory and generate a CSV file containing information about the hosts, ports, and vulnerabilities detected in the scan.

## Credits

This script was developed by Jen as part of a cybersecurity project.
