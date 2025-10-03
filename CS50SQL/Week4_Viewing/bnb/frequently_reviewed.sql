CREATE VIEW "frequently_reviewed" AS
SELECT l."id", l."property_type", l."host_name", COUNT("reviews") AS "reviews"
FROM "listings" l
JOIN "reviews" r ON r."listing_id" = l."id"
GROUP BY "listing_id"
ORDER BY "reviews" DESC, l."property_type", l."host_name"
LIMIT 100;
