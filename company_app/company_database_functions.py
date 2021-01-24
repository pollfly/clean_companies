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


def add_company(name, location, year, products, history):
    conn1 = sqlite3.connect('../company.db')
    c = conn1.cursor()
    c.execute("INSERT INTO companies VALUES (?,?,?,?,?)", (name, location, year, products, history))
    conn1.commit()
    conn1.close()


def delete_one(id):
    conn1 = sqlite3.connect('../company.db')
    c = conn1.cursor()
    c.execute("DELETE FROM companies WHERE rowid = (?)", id)
    conn1.commit()
    conn1.close()


def lookup_comp(comp=None):
    if not comp:
        comp = input("Search for a company: ")
    conn1 = sqlite3.connect('../company.db')
    c = conn1.cursor()
    c.execute("SELECT * FROM companies WHERE name = (?) or name = (?) or name = (?) or name = (?) ",
              (comp, comp.upper(), comp.lower(), comp.title()))
    items = c.fetchall()
    if items:
        for comp, location, year, products, history in items:
            return f"""
            <h1> <strong>Company:</strong><big style="color: blue"> {comp}</big></h1> 
            <hr/>
            <p> <strong>Location:</strong> {location} </p>
            <p> <strong>Founded:</strong> {year} </p>
            <p> <strong>Products:</strong> {products} </p>
            <p> <strong>History:</strong> {history} </p>"""
    else:
        if len(comp) < 2:
            return "<h2>Company not found</h2> <br> "
        else:
            letters = comp[:2]
            c.execute("SELECT name FROM companies WHERE name LIKE (?)", (f'{letters}%',))
            items = c.fetchall()
            if not items:
                return "<h2>Company not found</h2> <br> "
            stringify = ""
            for item in items:
                stringify += f"<form action='/{item[0]}'> <input type='submit' value={item[0]}> </form>"
            if items:
                return f"<h1>Do you mean one of these companies?<h1/>{stringify}<hr/>"