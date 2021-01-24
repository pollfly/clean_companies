class Company:
    def __init__(self, comp_name, date_founded, country_of_origin, type_of_comp, human_rights_history=""):
        self.name = comp_name
        self.date_founded = date_founded
        self.country_of_origin = country_of_origin
        self.product_list = []
        self.type_of_comp = type_of_comp
        self.human_rights_history = human_rights_history
        self.dict_form = {"Name": self.name, "Type": self.type_of_comp, "Date Founded": self.date_founded,
                          "Country": self.country_of_origin, "Products": self.product_list,
                          "Human Rights History": self.human_rights_history
        }


    def __str__(self):
        return f"""{self.name}
Founded: {self.date_founded}
{self.country_of_origin}
{self.type_of_comp}
Human Rights History:\n {self.human_rights_history} """


    def add_product(self, product):
        if not product in self.product_list:
            self.product_list.append(product)
            return "product added"
        else:
            return "product already added"


    def remove_product(self, product):
        if product in self.product_list:
            self.product_list.remove(product)
            return "product removed"


    def green_check(self):
        problems = 0
        for product in self.product_list:
            if not product.green:
                problems += 1
        return f"This company has environmental issues in {problems} products"


    def add_history(self, to_add):
        self.human_rights_history += f"- {to_add} \n"


nike = Company("Nike", "1930", "USA", "Sportswear", "- uses child labor")
adidas = Company("Adidas", "1960", "USA", "Sportswear", "- doesn't recycle")