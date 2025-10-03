CREATE TABLE "codes"(
    "sentence_row" INTEGER,
    "start_position" INTEGER,
    "lenght" INTEGER
);

INSERT INTO "codes"("sentence_row", "start_position", "lenght")
VALUES
(14,98,4),
(114,3,5),
(618,72,9),
(630,7,3),
(932,12,5),
(2230,50,7),
(2346,44,10),
(3041,14,5);

CREATE VIEW "message" AS
SELECT substr("sentences"."sentence", "codes"."start_position", "codes"."lenght") AS "phrase" FROM "sentences"
JOIN "codes" ON "sentences"."id" = "codes"."sentence_row";

