SELECT "japanese_title",ROUND("entropy", 2) AS "rounded entropy" FROM "views" WHERE "artist" = 'Hokusai' ORDER BY "constrast" DESC LIMIT 5;
