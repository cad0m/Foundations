CREATE TABLE "codes" (
    "id" INTEGER,
    "sentence_number" INTEGER,
    "character_number" INTEGER,
    "lenght" INTEGER,
    PRIMARY KEY("id")
);

INSERT INTO "codes" ("sentence_number", "character_number", "lenght")
VALUES
('14','98','4'),
('114','3','5'),
('618','72','9'),
('630','7','3'),
('932','12','5'),
('2230','50','7'),
('2346','44','10'),
('3041','14','5');

CREATE VIEW "decoding" AS
SELECT "sentence" AS "first_arg", "character_number" AS "second_arg", "lenght" AS "third_arg"
FROM "codes"
JOIN "sentences" ON "sentences"."id" = "codes"."sentence_number"
;

CREATE VIEW "message" AS
SELECT substr("first_arg", "second_arg", "third_arg") as "phrase"
FROM "decoding";

SELECT "phrase" FROM "message";
