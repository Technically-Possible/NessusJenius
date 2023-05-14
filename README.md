# NessusJenius

Don't be a Nessus zero - use Jen's genius script to parse your scan results.

## Overview

The NessusJenius.py script is a Python script that can parse one or multiple .nessus files and extract relevant information from them, such as the IP address, port, protocol, severity, plugin ID, plugin name, synopsis, description, and risk factor. The script writes this information to a CSV file specified by the user.

## Installation:
The script requires Python 3 to run, along with the following packages:

lxml
argparse
logging
These packages can be installed using pip and the included requirements.txt file. To install the dependencies, navigate to the directory containing the script and run the following command:

```
pip install -r requirements.txt
```
## Requirements

- Python 3.5 or later
- lxml library

## Usage

The script takes two command-line arguments:

-d or --directory: the directory containing the .nessus files to parse
-o or --output: the output CSV file to write the extracted information to
To run the script, navigate to the directory containing the script and run the following command:
```Bash
python NessusJenius.py 
Enter the directory containing Nessus files: /path/to/nessus/files
Enter the name of the output file: NameOfTheFinalCSV

```
The script will parse all Nessus scan files in the specified directory and generate a CSV file containing information about the hosts, ports, and vulnerabilities detected in the scan.

## Credits

This script was developed by Jen as part of a cybersecurity project.
