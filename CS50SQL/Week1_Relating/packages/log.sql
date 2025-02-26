
-- *** The Lost Letter ***
-- see if letter was sent
SELECT "address", "type", "contents", "action"
FROM "packages"
JOIN "scans" ON "packages"."id" = "scans"."package_id"
JOIN "addresses" ON "scans"."address_id" = "addresses"."id"
WHERE "contents" LIKE '%congratula%';
-- *** The Devious Delivery ***
SELECT "address", "type", "contents", "action"
FROM "packages"
JOIN "scans" ON "scans"."package_id" = "packages"."id"
JOIN "addresses" ON "scans"."address_id" = "addresses"."id"
WHERE "contents" LIKE '%duck%' AND "action" = 'Drop' AND "from_address_id" IS NULL;
-- *** The Forgotten Gift ***
SELECT "address" , "type",  "contents", "action" , "name", "timestamp"
FROM "packages"
JOIN "scans" ON "scans"."package_id" = "packages"."id"
JOIN "addresses" ON "scans"."address_id" = "addresses"."id"
JOIN "drivers" ON "scans"."driver_id" = "drivers"."id"
WHERE "from_address_id" = ( SELECT "id" FROM "addresses" WHERE "address" = '109 Tileston Street')
AND "to_address_id" = ( SELECT "id" FROM "addresses" WHERE "address" = '728 Maple Place');

