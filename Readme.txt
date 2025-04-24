API Call to add an employee
===========================
$ curl -X POST http://localhost:5000/employee -H "Content-Type: application/json" -d '{"id":1, "name":"Alice", "base_salary":50000, "bonus":5000}'

To update the salary
=====================
$ curl -X PUT http://localhost:5000/employee/<<employee id>> -H "Content-Type: application/json" -d '{"base_salary":55000}'

Example:
$ curl -X PUT http://localhost:5000/employee/1 -H "Content-Type: application/json" -d '{"base_salary":55000}'

To calculate salary
====================
$ curl http://localhost:5000/employee/<<employee id>>/salary

Example:
$ curl http://localhost:5000/employee/1/salary

To delete employee record
==========================
$ curl -X DELETE http://localhost:5000/employee/<<employee id>>

Example:
$ curl -X DELETE http://localhost:5000/employee/1

To list all the employees added
================================
$ curl http://localhost:5000/employees




