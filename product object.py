class Product:
    def __init__(self, name, company):
        self.name = name
        self.company = company

class Food(Product):
    def __init__(self, name, company):
        super.__init__(self, name, company)
        self.ingredients = []

    def add_ingredient(self, ingredient):
        if not ingredient in self.ingredients:
            self.ingredients.append(ingredient)


