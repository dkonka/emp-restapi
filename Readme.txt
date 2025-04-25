API Call to add an employee
===========================
$ curl --location 'http://127.0.0.1:5000/employee' --header 'Content-Type: application/json' --data '{"name": "konka", "base_salary": 50, "bonus": 100}'

To update the salary
=====================
$ curl --location --request PUT 'http://127.0.0.1:5000/employee/1' --header 'Content-Type: application/json' --data '{"base_salary": 100, "bonus": 200}'


To calculate salary
====================
$ curl --location 'http://127.0.0.1:5000/employee/1/salary'


To delete employee record
==========================
$ curl --location --request DELETE 'http://127.0.0.1:5000/employee/1'


options Call
$ curl --location --request OPTIONS 'http://127.0.0.1:5000/employee/1'




