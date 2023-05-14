import os
import argparse
from lxml import etree
import logging
import csv

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_nessus_file(nessus_file):
    with open(nessus_file, 'rb') as f:
        nessus_xml = f.read()
    root = etree.fromstring(nessus_xml)
    report_items = root.xpath('//ReportItem')
    hosts = []
    for report_item in report_items:
        host = {}
        host['ip'] = report_item.getparent().get('name')
        host['port'] = report_item.get('port')
        host['protocol'] = report_item.get('protocol')
        host['severity'] = report_item.get('severity')
        host['plugin_id'] = report_item.get('pluginID')
        host['plugin_name'] = report_item.get('pluginName')
        host['synopsis'] = report_item.find('synopsis').text if report_item.find('synopsis') is not None else ''
        host['description'] = report_item.find('description').text if report_item.find('description') is not None else ''
        host['risk_factor'] = report_item.find('risk_factor').text if report_item.find('risk_factor') is not None else ''
        hosts.append(host)
    logging.info(f'Finished parsing {nessus_file}')
    return hosts

def parse_nessus_files(nessus_files):
    all_hosts = []
    for nessus_file in nessus_files:
        if not os.path.isfile(nessus_file):
            logging.warning(f'{nessus_file} is not a valid file')
            continue
        all_hosts.extend(parse_nessus_file(nessus_file))
    return all_hosts

def main():
    nessus_dir = input("Enter the directory containing Nessus files: ")
    output_file = input("Enter the name of the output file: ")
    nessus_files = [os.path.join(nessus_dir, f) for f in os.listdir(nessus_dir) if f.endswith('.nessus')]
    all_hosts = parse_nessus_files(nessus_files)
    output_file += '.csv'
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['ip', 'port', 'protocol', 'severity', 'plugin_id', 'plugin_name', 'synopsis', 'description', 'risk_factor'])
        writer.writeheader()
        for host in all_hosts:
            writer.writerow(host)
    logging.info(f'Output written to {output_file}')

if __name__ == '__main__':
    main()
