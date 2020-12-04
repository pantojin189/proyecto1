from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

print('Hacer peticion a BBVA Bancomer de saldo del cliente')


# Creando la aplicación
app = Flask(__name__)
# Configuración de la conexión con la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Root.1234'
app.config['MYSQL_DB'] = 'iric'
# Creación de objeto para la conexión a la base de datos
mysql = MySQL(app)
app.secret_key = 'mysecret'

@app.route('/students/get', methods=['GET'])
def get_students():
    # Arreglo
    payload = []
    # Diccionario
    student = {}
    cursor = mysql.connection.cursor()
    cursor.execute("select * from student")
    data = cursor.fetchall()
    # Ciclo
    for row in data:
        student = {
            'id': row[0],
            'nombre': row[1],
            'a_paterno': row[2],
            'a_materno': row[3],
            'e_mail': row[4]
        }
        payload.append(student)
        student = {}
    return jsonify(payload)

@app.route('/students/add', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    a_paterno = request.form['a_paterno']
    a_materno = request.form['a_materno']
    e_mail = request.form['e_mail']
    cursor = mysql.connection.cursor()
    # Codigo para utililizar procedimientos almacenados
    cursor.execute(
        'insert into student(nombre, a_paterno, a_materno, e_mail) values(%s, %s, %s, %s)',
        (nombre, a_paterno, a_materno, e_mail)
    )
    # Confirma la operacion insert
    mysql.connection.commit()
    return jsonify({'message': 'Registro agregado'})
# Ejecución de app
if __name__ == '__main__':
    app.run()