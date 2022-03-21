"""Daily Menus of restaurants near Honeywell Brno"""

import sys

from lxml import html
import requests

# Xpath trees and web pages of restaurants
# SODEXO WHOLE WEEK '//div[@id="menu-4"]//div[@class="content"]//table[@class="food"]//td[@class="popisJidla"]/text()'
webs = ['http://www.restaurant-goa-slatina.cz/lang-cs/denni-menu', 'https://www.alltasty.cz', 'http://honeywell-brno-2.portal.sodexo.cz/cs/uvod']
trees = ['//div[@class="floatbox"]//td[@valign="top"]//text()', '//div[@class="left-div item-name"]//text()', '//div[@class="content"]//table[@class="food"]//td[@class="popisJidla"]/text()']

# Headers for printing results
header = '=' * 80
headerSmall = '=' * 36

def getMenu(sel):
    """Get menus from selected restaurants"""
    page = requests.get(webs[sel])
    tree = html.fromstring(page.content)

    selMenu = tree.xpath(trees[sel])

    return selMenu

def printMenu(numMenu, selMenu):
    """Print the wanted menu"""
    if numMenu == 1:
    # GOA
        printGoa(selMenu)
    elif numMenu == 2:
    # AllTasty
        #printAllTasty(selMenu)
        print('This restaurant is not implemented yet.')
    # Sodexo
    elif numMenu == 3:
        printSodexo(selMenu)
    else:
        print("Wrong restaurant...")

def printGoa(selMenu):
    """Print weekly menu from GOA Slatina"""
    print(header + '=')
    print(headerSmall + ' INDICKA ' + headerSmall)
    print(header + '=')

    for i in selMenu[10:-33]:
        print(i)

    print(header + '=')

def printSodexo(selMenu):
    """Print daily menu from Sodexo canteen"""
    print(header)
    print(headerSmall + ' SODEXO ' + headerSmall)
    print(header)

    for i in selMenu:
        print(i)

    print(header)

# def printAllTasty(selMenu):
#     """Print daily menu from All Tasty"""
#
#     print(header)
#     print(headerSmall + ' ALLTASTY ' + headerSmall)
#     print(header)
#
#     for i in selMenu:
#         print(i)
#
#     print(header)

def main():
    """Main script menu"""
    sel = input("Please select desired restaurant:\n\t1) GOA\n\t2) AllTasty\n\t3) Sodexo\n\t")
    selMenu = getMenu(int(sel)-1)
    # vyjimka - check numerka
    # neco jsem zadal?
    printMenu(int(sel), selMenu)

if __name__ == '__main__':
    main()
