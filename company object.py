class Company:
    def __init__(self, comp_name, date_founded, country_of_origin):
        self.comp_name = comp_name
        self.date_founded = date_founded
        self.country_of_origin = country_of_origin
        self.product_list = []

    def add_product(self, product):
        if not product in self.product_list:
            self.product_list.append(product)
            return "product added"
        else:
            return "product already added"

    def remove_product(self, product):
        if product in self.product_list:
            self.product_list.remove(product)



print(type([1,2,3]))