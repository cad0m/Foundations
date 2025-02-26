WITH "first_user" AS (
    SELECT "friend_id" FROM "friends"
    WHERE "user_id" = (
        SELECT "id" FROM "users"
        WHERE "username" = 'lovelytrust487'
    )
)
SELECT * FROM "first_user"
WHERE "friend_id" IN (
    SELECT "friend_id" FROM "friends"
    WHERE "user_id" = (
        SELECT "id" FROM "users"
        WHERE "username" = 'exceptionalinspiration482'
    )
);
