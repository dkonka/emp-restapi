from flask import Flask, jsonify, request
import sqlite3
from flask import g

app = Flask(__name__)

DATABASE = 'employee.db'

connect = sqlite3.connect(DATABASE)
cur = connect.cursor()

cur.execute(
    'CREATE TABLE IF NOT EXISTS employees (name TEXT, \
    base_salary INT, bonus INT)')
connect.commit()
connect.close()
# In-memory employee storage
employees = {}

# Add a new employee
@app.route('/employee', methods=['POST'])
def add_employee():
    data = request.get_json()
    connect = sqlite3.connect(DATABASE)
    cur = connect.cursor()
    cur.execute(
        f'INSERT INTO employees VALUES (\'{data["name"]}\', \'{data["base_salary"]}\', \'{data["bonus"]}\')'
    )
    rowid = cur.lastrowid
    connect.commit()
    connect.close()
    return jsonify({'message': 'Employee added', 'employee': rowid}), 200


# Update an employee's salary or bonus
@app.route('/employee/<int:emp_id>', methods=['PUT'])
def update_employee(emp_id):
    data = request.get_json()
    connect = sqlite3.connect(DATABASE)
    cur = connect.cursor()
    cur.execute(
        f'UPDATE employees SET base_salary = \'{data["base_salary"]}\', bonus = \'{data["bonus"]}\' where rowid = {emp_id}'
    )
    connect.commit()
    connect.close()
    return jsonify({'message': 'Employee updated', 'employee_id': emp_id})


# Delete an employee
@app.route('/employee/<int:emp_id>', methods=['DELETE'])
def delete_employee(emp_id):
    connect = sqlite3.connect(DATABASE)
    cur = connect.cursor()
    cur.execute(
        f'DELETE FROM employees where rowid = {emp_id}'
    )
    connect.commit()
    connect.close()
    return jsonify({'message': 'Employee deleted', 'employee': emp_id})
    


# Calculate salary (base + bonus)
@app.route('/employee/<int:emp_id>/salary', methods=['GET'])
def calculate_salary(emp_id):
    connect = sqlite3.connect(DATABASE)
    cur = connect.cursor()
    post =  cur.execute(
        f'select name,base_salary,bonus from employees where rowid = {emp_id}'
    )
    data = post.fetchone()

    return jsonify({'employee': data[0], 'total_salary': int(data[1]) + int(data[2])})


# Run the server
if __name__ == '__main__':
    app.run(debug=True)
