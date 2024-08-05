# migrate_data.py
import pandas as pd
from sqlalchemy import create_engine, text

# Conexión a PostgreSQL
postgres_engine = create_engine('postgresql://jsprofile:seguridadJire2024@localhost:5432/dbown')


# Ejecutar el comando para eliminar la tabla con CASCADE
with postgres_engine.connect() as connection:
    connection.execute(text("DROP TABLE IF EXISTS tienda_variation CASCADE"))
    # connection.execute(text("DROP TABLE IF EXISTS catalogo_categoria CASCADE"))

# Leer datos desde el archivo Excel
# df_catalogo_categoria = pd.read_excel('dbjs.xls', sheet_name='catalogo_categoria')
df_tienda_variation = pd.read_excel('dbjsVariation.xls', sheet_name='tienda_variation')

# Escribir datos en PostgreSQL
# df_catalogo_categoria.to_sql('catalogo_categoria', postgres_engine, if_exists='replace', index=False)
df_tienda_variation.to_sql('tienda_variation', postgres_engine, if_exists='replace', index=False)

print('Data migration completed successfully')
