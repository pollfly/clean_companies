from random import randint
import requests
from time import sleep
from bs4 import BeautifulSoup
import sqlite3
from company_database_functions import add_company
import config


# config.c.execute("""CREATE TABLE companies (
#         name text,
#         country_founded text,
#         products text,
#         history text)
#         """)

def icon_finder(icon_list, icon_name, division_type, class_name=None):
    for icon in icon_list:
        if icon_name in icon.svg.use.get('xlink:href'):
            break
    if icon_name in icon.svg.use.get('xlink:href'):
        parent = icon.find_parent()
        wanted_info = parent.findChild(division_type, class_=class_name)
        return wanted_info.text.strip().replace("  ", "")
    else:
        return False


def one_time_database_dump():
    url = "https://www.business-humanrights.org/en/companies/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    company_option_list = soup.find_all('option')
    comp_link_dictionary = {i.text: i.get('value') for i in company_option_list}
    link = 'https://www.business-humanrights.org'
    num = 1
    for company, comp_link in comp_link_dictionary.items():
        company_info = [company.strip()]
        if comp_link:
            url = link + comp_link
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            sleep(randint(1, 5))
            icons = soup.find_all("div", class_="list-item__icon")
            country = icon_finder(icons, "map-pin", "p")
            if country:
                company_info.append(country)
            else:
                company_info.append("to be added")
            products = icon_finder(icons, "tick", 'div', "list-item__content")
            if products:
                company_info.append(products)
            else:
                products2 = icon_finder(icons, "information", "p")
                if products2:
                    company_info.append(products2)
                else:
                    company_info.append("To be added")
            history_list = soup.find("div", class_="company__top-issues")
            if history_list:
                history = history_list.find_all('h4')
                history = [a.text for a in history]
                if history:
                    company_info.append("\n".join(history))
                else:
                    company_info.append("To be added")
            else:
                company_info.append("To be added")
            print(f'{num} companies done')
            num += 1
            yield company_info

# for company in one_time_database_dump():
#     add_company(*company)
