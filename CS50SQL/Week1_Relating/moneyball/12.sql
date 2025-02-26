SELECT "first_name", "last_name"
FROM (
    SELECT "first_name", "last_name", ("salary" / "H") AS "dollars_per_hit"
    FROM "players"
    JOIN "salaries" ON "salaries"."player_id" = "players"."id"
    JOIN "performances" ON "salaries"."player_id" = "performances"."player_id" AND "salaries"."year" = "performances"."year"
    WHERE "performances"."year" = 2001 AND "H" != 0
    ORDER BY "dollars_per_hit", "first_name", "last_name"
    LIMIT 10
) AS "moneyhits"
INTERSECT
SELECT "first_name", "last_name"
FROM (
    SELECT "first_name", "last_name", ("salary" / "RBI") AS "dollars_per_rbi"
    FROM "players"
    JOIN "salaries" ON "salaries"."player_id" = "players"."id"
    JOIN "performances" ON "salaries"."player_id" = "performances"."player_id" AND "salaries"."year" = "performances"."year"
    WHERE "performances"."year" = 2001 AND "RBI" != 0
    ORDER BY "dollars_per_rbi", "first_name", "last_name"
    LIMIT 10
) AS "moneyribs"
ORDER BY "last_name";
