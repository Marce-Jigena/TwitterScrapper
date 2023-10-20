import pypyodbc as odbc

class Db:

    DRIVER_NAME = 'SQL SERVER'
    SERVER_NAME = 'LAPTOP-KPJGE02C'
    DATABASE_NAME = 'TweeterScrapper'

    connection_string = f"""
        DRIVER={{{DRIVER_NAME}}};
        SERVER={SERVER_NAME};
        DATABASE={DATABASE_NAME};
        Trust_Connection=yes;
    """

    conn = odbc.connect(connection_string)
