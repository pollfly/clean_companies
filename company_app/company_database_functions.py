import sqlite3

def show_all():
    conn1 = sqlite3.connect('../company.db')
    c = conn1.cursor()
    c.execute("SELECT rowid, * FROM companies")
    items = c.fetchall()
    for item in items:
        print(item)
    conn1.commit()
    conn1.close()


# Add a new record to the table
def add_company(name, location, year, products, history):
    conn1 = sqlite3.connect('../company.db')
    c = conn1.cursor()
    c.execute("INSERT INTO companies VALUES (?,?,?,?,?)", (name, location, year, products, history))
    conn1.commit()
    conn1.close()

# Delete a record from the Table
def delete_one(id):
    conn1 = sqlite3.connect('../company.db')
    c = conn1.cursor()
    c.execute("DELETE FROM companies WHERE rowid = (?)", id)
    # commit our command
    conn1.commit()
    # Close connection
    conn1.close()
# print(c.fetchall())

def lookup_comp(comp=None):
    if not comp:
        comp = input("Search for a company: ")
    conn1 = sqlite3.connect('../company.db')
    c = conn1.cursor()
    c.execute("SELECT * FROM companies WHERE name = (?) or name = (?) or name = (?) or name = (?) ", (comp, comp.upper(), comp.lower(), comp.title()))
    items = c.fetchall()
    if items:
        for comp, location, year, products, history in items:
            return f"""
            <h1><br> <strong>Company:</strong> {comp} <br/></h1> 
            <br> <strong>Location:</strong> {location} <br/>
            <br> <strong>Founded:</strong> {year} <br/>
            <br> <strong>Products:</strong> {products} <br/>
            <br> <strong>History:</strong> {history} <br/>"""
    else:
        if len(comp) < 2:
            return "Company not found"
        else:
            letters = comp[:2]
            c.execute("SELECT name FROM companies WHERE name LIKE (?)", (f'{letters}%',))
            items = c.fetchall()
            if not items:
                return "Company not found"
            stringify = ""
            for item in items:
                stringify += f"<form action='/{item[0]}'> <input type='submit' value={item[0]}> </form>"
                #stringify += f'<br>{number} - {item[0]}\n'
            if items:
                return f"<h1>Did you mean one of these companies?<h1/>{stringify}"

                # name = input(f"""did you mean one of these companies? \n{stringify}.

            #     Enter number of company you want to search. If none, enter 'No'. """)
            #     if name.title() == 'No':
            #         return "Search ended"
            #     else:
            #         return lookup_comp(items[int(name)-1][0])
            #
            # else:
            #     return "Company not found"

# def not_found(comp):
#     letters = comp[:2]
#     conn1 = sqlite3.connect('../company.db')
#     c = conn1.cursor()
#     c.execute("SELECT name FROM companies WHERE name LIKE (?)", (f'{letters}%',))
#     items = c.fetchall()
#     if not items:
#         return "Company not found"
#     stringify = ""
#     for number, item in enumerate(items, 1):
#         stringify += f'{number} - {item[0]}\n'
#     if items:
#         name = input(f"""did you mean one of these companies? \n{stringify}.
#             Enter number of company you want to search. If none, enter 'No'. """)
#         if name.title() == 'No':
#             return "Search ended"
#         else:
#             return lookup_comp(items[int(name) - 1][0])



lookup_comp("co")