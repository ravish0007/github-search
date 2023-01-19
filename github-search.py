#!/usr/bin/env python3

import argparse
import requests
import sys

parser = argparse.ArgumentParser()
parser.add_argument("search_string")

args = parser.parse_args()

headers = {
    'Accept': 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2022-11-28',
}

params = {
    'q': args.search_string,
}

try:
    response = requests.get('https://api.github.com/search/repositories', params=params, headers=headers)
    if response:
        print(f'Search results for "{args.search_string}"', end='\n\n')
        for item in response.json()['items']:
            print(item['html_url'], '->', item['full_name'])
    else:
        print('Request unsuccessful, status_code ->', response.status_code)
        sys.exit(1)
except ConnectionError:
    print('Error occured, check your internet and try again.')




