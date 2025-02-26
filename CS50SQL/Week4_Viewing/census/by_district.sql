CREATE VIEW "by_district" AS
SELECT "district",
SUM("families") as "families",
SUM("households") as "households",
SUM("population") as "population",
SUM("male") as "male",
SUM("female") as "female"
FROM "census"
GROUP BY "district";
