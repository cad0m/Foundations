CREATE TABLE "meteorites" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "class" TEXT,
    "mass" REAL,
    "discovery" TEXT CHECK("discovery" IN ('Fell' , 'Found')),
    "year" INTEGER,
    "lat" REAL,
    "long" REAL,
    PRIMARY KEY("id")
);
CREATE TABLE "clean" (
    "name" TEXT NOT NULL,
    "class" TEXT,
    "mass" REAL,
    "discovery" TEXT,
    "year" INTEGER,
    "lat" REAL,
    "long" REAL
);

.import --csv meteorites.csv temp

insert into "clean" ("name", "class", "mass", "discovery", "year", "lat", "long")
SELECT "name", "class", "mass", "discovery", "year", "lat", "long" FROM "temp"
WHERE "nametype" != 'Relict';

DROP TABLE "temp";

UPDATE "clean" SET "year" = NULL WHERE "year" = '';
UPDATE "clean" SET "mass" = NULL WHERE "mass" = '';
UPDATE "clean" SET "lat" = NULL WHERE "lat" = '';
UPDATE "clean" SET "long" = NULL WHERE "long" = '';

UPDATE "clean" set "lat" = ROUND("lat" , 2)
WHERE "lat" NOT NULL;
UPDATE "clean" set "long" = ROUND("long" , 2)
WHERE "long" NOT NULL;
UPDATE "clean" set "mass" = ROUND("mass" , 2)
WHERE "mass" NOT NULL;

insert into "meteorites" ("name", "class", "mass", "discovery", "year", "lat", "long")
SELECT "name", "class", "mass", "discovery", "year", "lat", "long" FROM "clean"
ORDER BY "year", "name";

CREATE VIEW "average_book_rating" AS
SELECT "book_id", "title", "year", ROUND(AVG("rating"), 2) AS "rating"
FROM "ratings"
JOIN "books" ON "books"."id" = "ratings"."book_id"
GROUP BY "book_id"
ORDER by "title";

SELECT "year", ROUND(AVG("rating"), 2) AS "rating"
FROM "average_book_rating"
GROUP BY "year";

WITH "average_book_rating" AS (
    SELECT "book_id", "title", "year", ROUND(AVG("rating"), 2) AS "rating"
    FROM "ratings"
    JOIN "books" ON "books"."id" = "ratings"."book_id"
    GROUP BY "book_id"
)
SELECT "year", ROUND(AVG("rating"), 2) AS "rating"
FROM "average_book_rating"
GROUP BY "year";

