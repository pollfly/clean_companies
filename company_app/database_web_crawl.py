from random import randint
import requests
from time import sleep
from bs4 import BeautifulSoup
import sqlite3
from company_database_functions import add_company


conn1 = sqlite3.connect('../company.db')

c = conn1.cursor()

# c.execute("""CREATE TABLE companies (
#         name text,
#         country_founded text,
#         products text,
#         history text)
#         """)


def one_time_database_dump():
    url = "https://www.business-humanrights.org/en/companies/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    option_list = soup.find_all('option')
    dictionary = {i.text: i.get('value') for i in option_list}
    link = 'https://www.business-humanrights.org'
    num = 1
    for company, comp_link in dictionary.items():
        company_info = [company]
        if comp_link:
            url = link+comp_link
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            sleep(randint(1, 5))
            icons = soup.find_all("div", class_="list-item__icon")
            for icon in icons:
                if "map-pin" in icon.svg.use.get('xlink:href'):
                    break
            if "map-pin" in icon.svg.use.get('xlink:href'):
                parent = icon.find_parent()
                country = parent.findChild('p').text
                company_info.append(country)
            else:
                company_info.append("To be added")

            for icon in icons:
                if "tick" in icon.svg.use.get('xlink:href'):
                    break
            if "tick" in icon.svg.use.get('xlink:href'):
                parent2 = icon.find_parent()
                products = parent2.findChild('div', class_="list-item__content")
                if products:
                    products = products.text.strip().replace("\n","").replace("  ", "")
                    company_info.append(products)
            else:
                for icon2 in icons:
                    if "information" in icon2.svg.use.get('xlink:href'):
                        break
                if "information" in icon2.svg.use.get('xlink:href'):
                    parent = icon2.find_parent()
                    products = parent.findChild('div', class_="list-item__content")
                    if products:
                        products = products.text.strip().replace("\n", "").replace("  ", "")
                        company_info.append(products)
                else:
                    company_info.append("To be added")
        # history
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

conn1.close()