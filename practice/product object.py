class Product:
    def __init__(self, name, type, company):
        self.name = name
        self.company = company
        self.type = type
        self.issues = []

    def __str__(self):
        return f"{self.name} - {self.company}"


class Food(Product):

    def add_ingredient(self, ingredient):
        if not ingredient in self.ingredients:
            self.ingredients.append(ingredient)


class Textile(Product):
    def __init(self, name, company):
        super.__init__(self, name, company)
        self.materials = []

    def add_ingredient(self, materials):
        if not materials in self.materials:
            self.materials.append(materials)