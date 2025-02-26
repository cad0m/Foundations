SELECT "username" FROM "users"
WHERE "id" = (
    SELECT "to_user_id"
    FROM "messages"
    JOIN "users" ON "users"."id" = "messages"."to_user_id"
    GROUP BY "username"
    ORDER BY COUNT("messages"."id") DESC, "username" ASC
    LIMIT 1
);
