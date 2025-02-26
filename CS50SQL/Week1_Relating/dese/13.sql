SELECT "name"
FROM "districts"
WHERE "id" IN (
    SELECT "district_id"
    FROM "staff_evaluations"
    WHERE "needs_improvement" > (
        SELECT AVG("needs_improvement")
        FROM "staff_evaluations"
    )
);
