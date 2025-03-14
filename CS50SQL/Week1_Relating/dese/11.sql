SELECT "schools"."name", "per_pupil_expenditure", "graduated"
FROM "expenditures"
JOIN "schools" ON "expenditures"."district_id" = "schools"."district_id"
JOIN "graduation_rates" ON "schools"."id" = "graduation_rates"."school_id"
GROUP BY "schools"."name"
ORDER BY "per_pupil_expenditure" DESC, "schools"."name";

