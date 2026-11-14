DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;

CREATE TABLE departments (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  floor INTEGER
) STRICT;

CREATE TABLE employees (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  position TEXT NOT NULL,
  salary INTEGER,
  hired TEXT,
  department_id INTEGER REFERENCES departments(id)
) STRICT;

INSERT INTO departments (name, floor) VALUES
  ('Корпоративный', 3),
  ('Судебный', 2),
  ('Консультационный', 1);

INSERT INTO employees (name, position, salary, hired, department_id) VALUES
  ('Айгерим Нурланова', 'Юрист', 450000, '2023-03-15', 1),
  ('Данияр Касымов', 'Старший юрист', 620000, '2022-09-01', 1),
  ('Сабина Омарова', 'Помощник юриста', 320000, '2024-01-20', 1),
  ('Ерлан Бектуров', 'Адвокат', 580000, '2021-11-10', 2),
  ('Алина Серикова', 'Юрист', 470000, '2023-06-05', 2),
  ('Нурсултан Ахметов', 'Стажёр', 250000, '2024-09-01', 2),
  ('Жанар Ибрагимова', 'Консультант', 410000, '2022-04-18', 3),
  ('Тимур Жумабеков', 'Старший консультант', 550000, '2020-08-25', 3);

UPDATE employees SET salary = salary + 50000 WHERE name = 'Айгерим Нурланова';

DELETE FROM employees WHERE name = 'Нурсултан Ахметов';