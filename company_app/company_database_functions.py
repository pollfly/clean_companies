import sqlite3


def get_all_companies():
    conn1 = sqlite3.connect('../company.db')
    c = conn1.cursor()
    c.execute("SELECT rowid, * FROM companies")
    items = set(c.fetchall())
    conn1.close()
    return items


def add_company(name, location, products, history):
    conn1 = sqlite3.connect('../company.db')
    c = conn1.cursor()
    c.execute("INSERT INTO companies VALUES (?,?,?,?)", (name, location, products, history))
    conn1.commit()
    conn1.close()


def delete_company(id):
    conn1 = sqlite3.connect('../company.db')
    c = conn1.cursor()
    c.execute("DELETE FROM companies WHERE rowid = (?)", id)
    conn1.commit()
    conn1.close()


def lookup_company(comp=None):
    if not comp:
        comp = input("Search for a company: ")
    conn1 = sqlite3.connect('../company.db')
    c = conn1.cursor()
    c.execute("SELECT * FROM companies WHERE name = (?) or name = (?) or name = (?) or name = (?) ",
              (comp, comp.upper(), comp.lower(), comp.title()))
    items = c.fetchall()
    if items:
        for comp, location, products, history in items:
            history = history.replace("\n", "<br>")
            print(history)
            return f"""
            <h1> <strong>Company:</strong><big style="color: blue"> {comp}</big></h1> 
            <hr/>
            <p> <strong>Location:</strong> {location} </p>
            <p> <strong>Products:</strong> {products} </p>
            <p> <strong>History:</strong> {history} </p>"""
    else:
        if len(comp) < 2:
            return "<h1>Company not found</h1> <br> "
        else:
            letters = comp[:2]
            c.execute("SELECT name FROM companies WHERE name LIKE (?)", (f'{letters}%',))
            items = c.fetchall()
            # P.Z: here you are checking "if not items", 5 lines after you are checking "if items" but items is not
            # changed. Maybe you can use if-else?
            if not items:
                return "<h2>Company not found</h2> <br> "
            stringify = ""
            list_items = [list(i) for i in items]
            for item in list_items:
                item[0] = item[0].strip()
                stringify += f"<form action='/{item[0]}'> <input type='submit' value='{item[0]}'> </form>"
            if items:
                return f"<h1>Do you mean one of these companies?<h1/>{stringify}<hr/>"