SELECT "name" FROM "teams" WHERE "id" IN (
    SELECT "team_id"
    FROM "performances"
    JOIN "players" ON "players"."id" = "performances"."player_id"
    WHERE "first_name" = 'Satchel' AND "last_name" = 'Paige'
);
