SELECT cases.number, cases.client, lawyers.name
FROM cases JOIN lawyers ON cases.lawyer_id =  lawyers.id;

SELECT cases.number, lawyers.name FROM cases JOIN lawyers ON cases.lawyer_id = lawyers.id 
WHERE lawyers.name = 'Мария Ким';


SELECT cases.number, lawyers.name FROM cases JOIN lawyers ON cases.lawyer_id = lawyers.id
WHERE cases.status = 'в работе'  ORDER BY lawyers.name;

SELECT COUNT (*) FROM cases

SELECT COUNT (*) FROM cases WHERE status = 'в работе'

SELECT SUM(amount) FROM cases WHERE client = 'ТОО Альфа'

