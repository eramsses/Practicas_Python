import psycopg2

conexion = psycopg2.connect(
    user="postgres",
    password="michelle",
    host="127.0.0.1",
    port="5432",
    database="test_db")

try:
    cursor = conexion.cursor()
    sentencia = "SELECT * FROM personas"
    cursor.execute(sentencia)

    registros = cursor.fetchall()

    print(registros)
except Exception as e:
    print(e)
finally:
    cursor.close()
    conexion.close()



