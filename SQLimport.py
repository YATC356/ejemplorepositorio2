import mysql.connector

# conectar a la base de datos
conn = mysql.connector.connect(
    host="localhost",  user="root", password="admin", database="facturacion_db"
)
cursor = conn.cursor()
criterio = input("Ingresa el criterio de busqueda: ")
query= f"SELECT * FROM articulos WHERE descripcion like \'%{criterio}%\'; delete articulos where id = 8;"
print(f"CONSULTA: {query}")

# ejecutar el SELECT
cursor.execute(query)
resultados = cursor.fetchall()

# mostrar los datos
for fila in resultados:
    print(f"el codigo {fila[1]} corresponde a {fila[2]} y vale {fila[4]}")

# cerrar conexion
conn.close()

