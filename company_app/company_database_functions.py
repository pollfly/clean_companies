import sqlite3
import config


def connect_to_database():
    config.conn1 = sqlite3.connect(config.company_database)
    config.c = config.conn1.cursor()


def commit_close_database_connection():
    config.conn1.commit()
    config.conn1.close()


def get_all_companies_info(comp_id=False, name=True, country_founded=True, products=True, history=True):
    a = locals()
    company_info_dict = a
    connect_to_database()
    stringify = ""
    for info_type, boolean in company_info_dict.items():
        if boolean:
            stringify += f"{info_type}, "
    stringify = stringify[:-2]
    config.c.execute(f"SELECT {stringify} FROM companies")
    items = set(config.c.fetchall())
    config.conn1.close()
    return items


def add_company(name, location, products, history):
    connect_to_database()
    config.c.execute("INSERT INTO companies VALUES (?,?,?,?)", (name, location, products, history))
    commit_close_database_connection()


def delete_company(id_num):
    connect_to_database()
    config.c.execute("DELETE FROM companies WHERE rowid = (?)", id_num)
    commit_close_database_connection()


def lookup_company(company=None):
    if not company:
        company = input("Search for a company: ")
    connect_to_database()
    config.c.execute("SELECT * FROM companies WHERE name = (?) or name = (?) or name = (?) or name = (?) ",
                     (company, company.upper(), company.lower(), company.title()))
    items = config.c.fetchall()
    if items:
        for company, location, products, history in items:
            history = history.replace("\n", "<br>")
            print(history)
            return f"""
            <h1> <b>Company:</b><big style="color: blue"> {company}</big></h1> 
            <hr/>
            <p> <big><b>Location:</b></big> {location} </p>
            <p> <big><b>Products:</b></big> {products} </p>
            <p> <big><b>Human Rights Topics:</b></big><br> {history} </p>"""
    else:
        if len(company) < 2:
            return "<h1>Company not found</h1> <br> "
        else:
            letters = company[:2]
            config.c.execute("SELECT name FROM companies WHERE name LIKE (?) or (?)", (f"%{company}%", f"{letters}%"))
            items = config.c.fetchall()
            if not items:
                return "<h2>Company not found</h2> <br> "
            else:
                stringify = ""
                list_items = [list(i) for i in items]
                for item in list_items:
                    item[0] = item[0].strip()
                    stringify += f"""<form action="/{item[0]}"> <input type="submit" value="{item[0]}"> </form>"""
                if items:
                    return f"<h1>Do you mean one of these companies?<h1/>{stringify}<hr/>"
