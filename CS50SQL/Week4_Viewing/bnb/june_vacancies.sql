CREATE VIEW "june_vacancies" AS
SELECT "id", "property_type", "host_name", COUNT("date") AS "days_vacant"
FROM "available"
WHERE "date" BETWEEN '2023-06-01' AND '2023-06-30'
GROUP BY "id";
