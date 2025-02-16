import sqlite3
from rich.progress import Progress
import pandas as pd

class Database:

    def __init__(self, path: str):
        self.path = path    
    def initConnection(self):
        try:
            self.connection = sqlite3.connect(self.path)    
        except Exception as e:
            print('Error Connection ', e)
    def getConnection(self):
        if not hasattr(self, 'connection'):
            self.initConnection()
        return self.connection
    
    def insert_many(self, table: str, columns: list, data):
        if isinstance(data, pd.DataFrame) and data.empty:
            print("⚠️ No hay datos para insertar.")
            return

        MAX_BATCH_SIZE = 1000  
        num_batches = (len(data) // MAX_BATCH_SIZE) + 1

        column_names = ", ".join(columns)
        placeholders = ", ".join(["?"] * len(columns))
        query = f"INSERT INTO {table} ({column_names}) VALUES ({placeholders})"

        # Inicializar la barra de progreso
        with Progress() as progress:
            task = progress.add_task(f"[green]Insertando datos en {table}...", total=num_batches)

            # Insertar datos por lotes
            for i in range(num_batches):
                batch = data[i * MAX_BATCH_SIZE : (i + 1) * MAX_BATCH_SIZE]
                if isinstance(batch, pd.DataFrame):
                    if not batch.empty:
                        cursor = self.connection.cursor()
                        cursor.executemany(query, batch.values.tolist())
                        self.connection.commit()
                elif isinstance(batch, list):
                    if batch:
                        cursor = self.connection.cursor()
                        cursor.executemany(query, batch)
                        self.connection.commit()
                
                # Avanzar la barra de progreso
                progress.update(task, advance=1)

        print(f"✅ {len(data)} filas insertadas en '{table}'.")

    def close_connection(self):
        """ Cierra la conexión con la base de datos """
        self.connection.close()