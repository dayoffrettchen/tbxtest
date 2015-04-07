#!/usr/bin/env python
import re
import urllib.request

from bs4 import BeautifulSoup


def find_links(link):
    global soup, site_link
    soup = BeautifulSoup(urllib.request.urlopen(link))
    for site_link in soup.find_all('a'):
        print(site_link)
        # href_ = site_link #['href']
        # print(href_)
        # if not href_:
        #     continue
        # if href_ == '/':
        #     continue
        # if href_ in link:
        #     print(href_)
        # if home in href_ and re.sub(home, '', href_) in link:
        #     print(href_)


__author__ = 'christoph'
home = "http://localhost:9002/"
links = [
    # "https://localhost:9002/goettingen/buecher/c-SL0101",
    # "https://localhost:9002/goettingen/Musterfiliale-2/Apple/sv-000001JK-PV0004UW",
    # "https://localhost:9002/goettingen/Musterfiliale-2/s-000001JK",
    "https://localhost:9002/goettingen/buecher-filme-musik-games/c-SL01",
    # "https://localhost:9002/goettingen/Apple/v-PV0004UW"
]

for link in links:
    link = link.split("?")[0]
    link = link.split("#")[0]
    print("#################################################")
    print("{0}".format(link))
    print("#################################################")
    find_links(link)
    print()




