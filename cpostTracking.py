"""Script for Ceska Posta tracking by tracking number"""

import sys

from lxml import html
import requests

# URLs of webpages for data scrapping
cpostTrackUrl = 'https://www.postaonline.cz/trackandtrace/-/zasilka/cislo?parcelNumbers='
ebayTrackUrl = 'https://www.ebay.com/myb/Summary?MyEbay&gbh=1'

# eBay login payload
payload = {
	"userid": "<USER NAME>",
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

    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='htmid']/@value")))[0]

    result = session_requests.post(login_url, data = payload, headers = dict(referer=login_url))

    print(result.ok)
    print(result.status_code)

def getEbayTrkNums():
    """Function gets provided tracking labels from My eBay page"""
    page = requests.get(ebayTrackUrl)
    tree = html.fromstring(page.content)

    trkLbl = tree.xpath('//p[@class="tracking-label"]/text()')
    trkLbl2 = tree.xpath('//p[@class="iframe-modal"]/text()')

    print(trkLbl)
    print(trkLbl2)

def findMyPackage(trackNumber):
    """Main function executed after prog run"""
    page = requests.get(cpostTrackUrl + trackNumber)
    tree = html.fromstring(page.content)

    notFound = tree.xpath('//p[@class="error"]/text()')

    print(notFound[0:-1])

if __name__ == '__main__':
    findMyPackage(sys.argv[1])
