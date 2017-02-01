"""This module does"""
#!/usr/bin/env python3

# pylint: disable=I0011
# pylint: disable=C0103

import xml.etree.ElementTree as etree
import csv
import os


ip = []
vuln = []
severity = []

start = 1


nessus_file = open('/tmp/nessus_file.csv', 'w')
csvwriter = csv.writer(nessus_file)
csvwriter.writerow(['ip Address', 'vulnerability', 'severity'])

count = 0
i = 0

data = []

for fileName in os.listdir("."):
    if ".nessus" in fileName:
        if start:
            mainTree = etree.parse(fileName)
            root = mainTree.getroot()
            for reportHost in root.iter('ReportHost'):
                ip.append(reportHost.get('name'))
            for reportItem in root.iter('ReportItem'):
                vuln.append(reportItem.get('pluginName'))
                severity.append(reportItem.get('severity'))
            # Only go through the while loop while there are still boxes (with IPs) to process
            while i < len(ip):
                data.append(ip[count])
                data.append(vuln[count])
                data.append(severity[count])
                csvwriter.writerow(data)
                data = []
                i += 1
                count += 1
nessus_file.close()
