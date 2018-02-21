"""Script for Ceska Posta tracking by tracking number"""

import sys

from lxml import html
import requests

cpostTrackUrl = 'https://www.postaonline.cz/trackandtrace/-/zasilka/cislo?parcelNumbers='

def findMyPackage(trackNumber):
    """Main function executed after prog run"""
    page = requests.get(cpostTrackUrl + trackNumber)
    tree = html.fromstring(page.content)

    notFound = tree.xpath('//p[@class="error"]/text()')

    print(notFound[0:-1])

if __name__ == '__main__':
    findMyPackage(sys.argv[1])
