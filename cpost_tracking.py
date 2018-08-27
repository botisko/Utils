"""Script for Ceska Posta tracking by tracking number"""

import sys
from lxml import html
import requests

cpost_track_url = 'https://www.postaonline.cz/trackandtrace/-/zasilka/cislo?parcelNumbers='


def find_package(track_number):
    """Main function executed after prog run"""
    page = requests.get(cpost_track_url + track_number)
    tree = html.fromstring(page.content)

    pkg_not_found = tree.xpath('//p[@class="error"]/text()')

    print(pkg_not_found[0:-1])


if __name__ == '__main__':
    find_package(sys.argv[1])
