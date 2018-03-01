#!/usr/bin/env python

"""Script for Ceska Posta tracking by tracking number"""

__author__ = "Jan Bijota"
__copyright__ = "Copyright 2018"
__credits__ = ["Jan Bijota"]
__license__ = "GPL"
__date__ = "2/27/2018"
__version__ = "0.1"
__maintainer__ = "Jan Bijota"
__email__ = "jan@bijota.cz"
__status__ = "Prototype"

import sys
import getpass

from lxml import html
import requests

# URLs of webpages for data scrapping
cpostTrackUrl = 'https://www.postaonline.cz/trackandtrace/-/zasilka/cislo?parcelNumbers='
ebayTrackUrl = 'https://www.ebay.com/myb/Summary?MyEbay&gbh=1'

# eBay login payload
payload = {
    "userid": "<USERNAME>",
    "pass": "<PASSWORD>",
    "htmid": "<TOKEN>"
}

# Session object will allow us to persist the login session across all our requests
session_requests = requests.session()


def ebayLogin():
    """Function for successful login to eBay
       see http://kazuar.github.io/scraping-tutorial/ for details"""
    login_url = "https://signin.ebay.com/ws/eBayISAPI.dll"
    result = session_requests.get(login_url)

    # Get data from console input
    payload["os_username"] = input('eBay Login: ')
    print('Login:', payload["os_username"])

    payload["os_password"] = getpass.getpass(
        prompt='eBay Password: ', stream=None)
    print('Zadal jsi:', payload["os_password"])

    # Get authenticity token from login page
    tree = html.fromstring(result.text)
    payload["htmid"] = list(
        set(tree.xpath("//input[@name='htmid']/@value")))[0]

    result = session_requests.post(
        login_url, data=payload, headers=dict(referer=login_url))

    # Print results
    print(result.ok)
    print(result.status_code)


def getEbayTrkNums():
    """Function gets provided tracking labels from My eBay page"""
    # Get traking numbers from myEbay page
    page = requests.get(ebayTrackUrl)
    tree = html.fromstring(page.content)

    trkLbl = tree.xpath('//p[@class="tracking-label"]/text()')
    trkLbl2 = tree.xpath('//p[@class="iframe-modal"]/text()')

    # Print tracking numbers
    print(trkLbl)
    print(trkLbl2)


def findMyPackage(trackNumber):
    """Main function executed after prog run"""
    page = requests.get(cpostTrackUrl + trackNumber)
    tree = html.fromstring(page.content)

    notFound = tree.xpath('//p[@class="error"]/text()')

    print(notFound[0:-1])


if __name__ == '__main__':
    # findMyPackage(sys.argv[1])
    ebayLogin()
    getEbayTrkNums()
