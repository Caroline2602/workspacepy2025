from sqlite3 import Connection

class CLIENT:
    def __init__(self, QUANTITY, INVOICENUMBER):
        self.QUANTITY = QUANTITY
        self.INVOICENUMBER = INVOICENUMBER

    def __repr__(self):
        return f"CLIENT(QUANTITY={self.QUANTITY}, INVOICENUMBER={self.INVOICENUMBER})"

class Productos:
    """ Tabla PRODUCTOS: DESCRIPTION, PRICE"""

    def create_table(self, con: Connection):
        query = """
            CREATE TABLE IF NOT EXISTS PRODUCTOS (

                PRODUCTID INTEGER NOT NULL,
                QUANTITY INTEGER NOT NULL
            );
        """
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()



class Ventas:
    """ Tabla VENTAS con múltiples relaciones """

    def create_table(self, con: Connection):
        query = """
            CREATE TABLE IF NOT EXISTS VENTAS (
            
                ORDERID VARCHAR(20) NOT NULL,
                PRODUCTID INTEGER NOT NULL,
                QUANTITY INTEGER NOT NULL,
            
            );
        """
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()


         
         