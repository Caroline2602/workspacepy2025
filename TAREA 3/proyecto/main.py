from controllerc.menu import *
from configuracionc.app import *
import os

if __name__ == "__main__":
    db_path = './proyecto/datux/2025.db'
    
    # Crear el directorio si no existe
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    # Crear el archivo de la base de datos si no existe
    if not os.path.exists(db_path):
        open(db_path, 'w').close()
    
    app = App(db_path)
    menu(app)
    pass