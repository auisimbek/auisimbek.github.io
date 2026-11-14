-- 1. Сотрудники с зарплатой выше 500000, отсортированные по зарплате (WHERE + ORDER BY + LIMIT)
SELECT name, position, salary FROM employees WHERE salary > 500000 ORDER BY salary DESC LIMIT 5;

-- 2. Сотрудники, принятые после 2023 года, по имени (WHERE + ORDER BY + LIMIT)
SELECT name, hired, salary FROM employees WHERE hired > '2023-01-01' ORDER BY name LIMIT 10;

-- 3. Сотрудники из отдела 1 (Корпоративный), отсортированные по должности (WHERE + ORDER BY + LIMIT)
SELECT name, position, salary FROM employees WHERE department_id = 1 ORDER BY position LIMIT 5;

-- 4. Сколько всего сотрудников (COUNT)
SELECT COUNT(*) AS total_employees FROM employees;

-- 5. Средняя зарплата (AVG)
SELECT AVG(salary) AS average_salary FROM employees;

-- 6. Средняя зарплата по должностям (GROUP BY)
SELECT position, AVG(salary) AS avg_salary FROM employees GROUP BY position;

-- 7. Имя сотрудника, должность и название отдела (JOIN)
SELECT employees.name, employees.position, departments.name AS department
FROM employees
JOIN departments ON employees.department_id = departments.id;

-- 8. Сколько сотрудников в каждом отделе (JOIN + GROUP BY)
SELECT departments.name AS department, COUNT(employees.id) AS employee_count
FROM departments
JOIN employees ON departments.id = employees.department_id
GROUP BY departments.name;