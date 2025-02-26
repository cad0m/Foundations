SELECT "districts"."name"
FROM "districts"
JOIN "expenditures" ON "districts"."id" = "expenditures"."district_id"
WHERE "pupils" IN (SELECT MIN("pupils") FROM "expenditures");
