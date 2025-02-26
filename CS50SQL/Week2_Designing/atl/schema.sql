CREATE TABLE "passangers" (
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "age" INTEGER NOT NULL,
    PRIMARY KEY ("id")
);

CREATE TABLE "airlines" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "concourse" TEXT NOT NULL CHECK("concourse" IN ('A', 'B', 'C', 'D', 'E', 'F')),
    PRIMARY KEY ("id")
);

CREATE TABLE "checkins" (
    "passanger_id" INTEGER,
    "flight_id" INTEGER,
    "dates" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY ("passanger_id") REFERENCES "passangers"("id"),
    FOREIGN KEY ("flight_id") REFERENCES "airlines"("id")
);

CREATE TABLE "flights" (
    "id" INTEGER,
    "flight_number" INTEGER NOT NULL,
    "airline_id" INTEGER NOT NULL,
    "from_code" INTEGER NOT NULL,
    "to_code" INTEGER NOT NULL,
    "departure_date" NUMERIC,
    "arrival_date" NUMERIC,
    PRIMARY KEY ("id"),
    FOREIGN KEY ("airline_id") REFERENCES "airelines"("id")
);

