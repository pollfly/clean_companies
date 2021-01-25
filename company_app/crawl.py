import requests
from bs4 import BeautifulSoup


url = "https://www.business-humanrights.org/en/companies/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())
option_list = soup.find_all('option')
dictionary = {i.text: i.get('value') for i in option_list[17:30]}
# # print(dictionary)
link = 'https://www.business-humanrights.org'
for company, comp_link in dictionary.items():
    if comp_link:
        # location
        url = link+comp_link
        print(url)
        print(company)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        icons = soup.find_all("div", class_="list-item__icon")
        for icon in icons:
            if "map-pin" in icon.svg.use.get('xlink:href'):
                break
        if "map-pin" in icon.svg.use.get('xlink:href'):
            parent = icon.find_parent()
            country = parent.findChild('p').text
            print(1, country)
        else:
            print("1 NONE")

        for icon in icons:
            if "tick" in icon.svg.use.get('xlink:href'):
                break
        if "tick" in icon.svg.use.get('xlink:href'):
            parent2 = icon.find_parent()
            products = parent2.findChild('div', class_="list-item__content")
            if products:
                products = products.text.strip().replace("\n","").replace("  ", "")
                print(2, products)
        else:
            for icon2 in icons:
                 if "information" in icon2.svg.use.get('xlink:href'):
                    break
            if "information" in icon2.svg.use.get('xlink:href'):
                parent = icon2.find_parent()
                products = parent.findChild('div', class_="list-item__content")
                if products:
                    products = products.text.strip().replace("\n", "").replace("  ", "")
                    print(2.5, products)
            else:
                print("2 None")

        # history
        history_list = soup.find("div", class_="company__top-issues")
        if history_list:
            history = history_list.find_all('h4')
            history = [a.text for a in history]
            if history:
                print(3, "\n".join(history))
            else:
                print("3 none")
        else:
            print("3.5 None")
        #print(a.text.strip())



# url = /en/companies/abercrombie-fitch/
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")