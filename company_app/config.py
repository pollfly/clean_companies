import sqlite3


company_database = '../company.db'
conn1 = sqlite3.connect(company_database)
cursor = conn1.cursor()


# cursor.execute("""CREATE TABLE companies (
#         name text,
#         country_founded text,
#         products text,
#         history text)
#         """)