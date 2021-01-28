import sqlite3


company_database = '../company.db'
conn1 = sqlite3.connect(company_database)
c = conn1.cursor()
