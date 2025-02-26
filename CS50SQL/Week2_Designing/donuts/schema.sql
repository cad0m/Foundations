CREATE TABLE "ingredients" (
    "id" INTEGER,
    "flour" REAL,
    "yeast" REAL,
    "oil" REAL,
    "butter" REAL,
    "sugar" REAL,
    PRIMARY KEY("id")
);

CREATE TABLE "donuts" (
    "id" INTEGER,
    "name" TEXT NOT NULL UNIQUE,
    "gluten_free" TEXT NOT NULL CHECK("gluten_free" IN ('yes', 'no')),
    "price" INTEGER NOT NULL,
    "ingredient_id" INTEGER,
    PRIMARY KEY("id"),
    FOREIGN KEY("ingredient_id") REFERENCES "ingredients"("id")
);

CREATE TABLE "orders" (
    "id" INTEGER,
    "track_number" INTEGER UNIQUE,
    "donuts_id" INTEGER,
    "customer_id" INTEGER,
    PRIMARY KEY("id", "donuts_id"),
    FOREIGN KEY("donuts_id") REFERENCES "donuts"("id"),
    FOREIGN KEY("customer_id") REFERENCES "customer"("id")
);

CREATE TABLE "customers" (
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "order_id" INTEGER,
    PRIMARY KEY("id", "order_id"),
    FOREIGN KEY("order_id") REFERENCES "orders"("id")
);

