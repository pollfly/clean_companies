import sqlite3


conn1 = sqlite3.connect('../company.db')

c = conn1.cursor()
# c.execute("""CREATE TABLE companies (
#         name text,
#         city_founded text,
#         year_founded text,
#         products text,
#         history text)
#         """)
#
# many_companies = [("Company","City", 2020, "products", "history of terrible"),
#                   ("Company2","City2", 2019, "products2", "history of terrible part 2"),
#                   ('Adidas', 'San Francisco', '1930', 'shoes, clothes', 'cannibalism'),
#                   ('NIKE', 'New York', '1950', 'shoes', 'child labor')]
#
# c.executemany("INSERT INTO companies VALUES (?,?,?,?,?)", many_companies)
conn1.commit()


conn1.close()