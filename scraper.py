# -*- coding: utf-8 -*-

"""
Created Feb 2, 2019
@author: Alex Truesdale

Python tool to scrape .R code from github repo contents.
"""

from requests_html import HTMLSession
from bs4 import BeautifulSoup
import html
import csv
import re
import os

# Initilise HMTL requests session.
session = HTMLSession()

# Change directory to output dir.
os.chdir('/Users/alextruesdale/Documents/quantlet-scraper/code_output')

# Open source file as .csv and read in lines.
with open('QUANTLET_LINKS.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    urls = [line[0] for line in csv_reader]

# Define URL replacement pairings.
replacements = {
    'https://github.com': 'https://raw.githubusercontent.com',
    'blob/': ''
}

# Compile RegEx pattern for 'or' replacement statement; test on dummy URL.
pattern = re.compile('|'.join(replacements.keys()))
text = pattern.sub(lambda x: replacements[x.group(0)], 'https://github.com/QuantLet/ARR/blob/master/ARRcormer/ARRcormer.R')
text

# Initilise aggregate list container; loop through source URLs, find absolute links for .R files.
links_aggregate = []
for i, url in enumerate(urls):
    page = session.get(url)
    print(i, ': ', url)
    links = [pattern.sub(lambda x: replacements[x.group(0)], page) for page in page.html.absolute_links if page.endswith('.R')]
    if len(links) > 0:
        links_aggregate.extend(links)

# Redefine links_aggregate as set of unique URLs.
links_aggregate = [link for link in set(links_aggregate)]

# Create dictionary pairing URLs to their raw contents.
contents_dictionary = {}
for i, link in enumerate(links_aggregate):
    print(i, ': ', link)
    get_result = session.get(link)
    try:
        code = BeautifulSoup(get_result.html.html, 'html.parser')
        contents_dictionary.update({link: code.prettify()})
    else:
        print('ERROR:', link)

# Define aggregate_code_path; loop through pairwise dict. and write individual files
# Append code to aggregate file.

aggregate_code_path = 'CODE_AGGREGATE.R'
for file, contents in contents_dictionary.items():
    filename = file.split('/')[-1]
    print(filename)

    # with open(filename, 'w') as single_file:
    #     single_file.write(contents)
    #
    # with open(aggregate_code_path, 'a') as aggregate:
    #     aggregate.write(contents)
    #     aggregate.write('\n\n')
