from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory employee storage
employees = {}


# Add a new employee
@app.route('/employee', methods=['POST'])
def add_employee():
    data = request.get_json()
    emp_id = data['id']
    employees[emp_id] = {
        'name': data['name'],
        'base_salary': data['base_salary'],
        'bonus': data.get('bonus', 0)
    }
    return jsonify({'message': 'Employee added', 'employee': employees[emp_id]}), 201


# Update an employee's salary or bonus
@app.route('/employee/<int:emp_id>', methods=['PUT'])
def update_employee(emp_id):
    if emp_id not in employees:
        return jsonify({'error': 'Employee not found'}), 404
    data = request.get_json()
    employees[emp_id].update({
        'base_salary': data.get('base_salary', employees[emp_id]['base_salary']),
        'bonus': data.get('bonus', employees[emp_id]['bonus'])
    })
    return jsonify({'message': 'Employee updated', 'employee': employees[emp_id]})


# Delete an employee
@app.route('/employee/<int:emp_id>', methods=['DELETE'])
def delete_employee(emp_id):
    if emp_id in employees:
        deleted = employees.pop(emp_id)
        return jsonify({'message': 'Employee deleted', 'employee': deleted})
    return jsonify({'error': 'Employee not found'}), 404


# Calculate salary (base + bonus)
@app.route('/employee/<int:emp_id>/salary', methods=['GET'])
def calculate_salary(emp_id):
    if emp_id not in employees:
        return jsonify({'error': 'Employee not found'}), 404
    emp = employees[emp_id]
    total_salary = emp['base_salary'] + emp.get('bonus', 0)
    return jsonify({'employee': emp['name'], 'total_salary': total_salary})

# Get all employees
@app.route('/employees', methods=['GET'])
def get_all_employees():
    return jsonify(employees)


# Run the server
if __name__ == '__main__':
    app.run(debug=True)
