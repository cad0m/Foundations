SELECT "birth_state" ,COUNT("bats") AS "Number of right bat player depend on theyre stat" FROM "players" WHERE "bats" = 'R' GROUP BY "birth_state" ORDER BY "bats";
