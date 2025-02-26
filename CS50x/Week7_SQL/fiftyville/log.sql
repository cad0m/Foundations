-- Keep a log of any SQL queries you execute as you solve the mystery.

-- find more infos about the crime
SELECT "description" FROM crime_scene_reports
WHERE "year" = 2023 AND "month" = 7 AND "day" = 28 AND "street" = "Humphrey Street";

--seek more info from the interviews
SELECT transcript FROM interviews
WHERE "year" = 2023 AND "month" = 7 AND "day" = 28 AND transcript LIKE '%bakery%';

-- seek more info from the bakery
SELECT name FROM people
WHERE license_plate IN (
    SELECT license_plate FROM bakery_security_logs
    WHERE "year" = 2023 AND "month" = 7 AND "day" = 28 AND "hour" = 10 AND "activity" = 'exit' AND "minute" BETWEEN 15 AND 25
);

-- get the accout user name
SELECT people.name
FROM atm_transactions
JOIN bank_accounts ON bank_accounts.account_number = atm_transactions.account_number
JOIN people ON people.id = bank_accounts.person_id
WHERE "year" = 2023 AND "month" = 7 AND "day" = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw';

-- seek info from the call
SELECT * FROM phone_calls
WHERE "year" = 2023 AND "month" = 7 AND "day" = 28 AND duration <= 60;

-- get the people who can be the criminal
SELECT "name", id FROM people
WHERE phone_number IN(
    SELECT "caller" FROM phone_calls
    WHERE "year" = 2023 AND "month" = 7 AND "day" = 28 AND duration <= 60
)
AND license_plate IN(
    SELECT license_plate FROM bakery_security_logs
    WHERE "year" = 2023 AND "month" = 7 AND "day" = 28 AND "hour" = 10 AND "activity" = 'exit' AND "minute" BETWEEN 15 AND 25
)
AND id IN(
    SELECT people.id
    FROM atm_transactions
    JOIN bank_accounts ON bank_accounts.account_number = atm_transactions.account_number
    JOIN people ON people.id = bank_accounts.person_id
    WHERE "year" = 2023 AND "month" = 7 AND "day" = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw'
);
-- we get diana and bruce


-- check the earliest flight tomorrow
SELECT flights.id FROM flights
JOIN airports ON airports.id = flights.origin_airport_id
WHERE "year" = 2023 AND "month" = 7 AND "day" = 29 AND city = 'Fiftyville'
ORDER BY "hour", "minute"
LIMIT 1;
-- search for poeple whos gonna take it
SELECT people.name, FROM passengers
JOIN people ON people.passport_number = passengers.passport_number
WHERE flight_id = (
    SELECT flights.id FROM flights
    JOIN airports ON airports.id = flights.origin_airport_id
    WHERE "year" = 2023 AND "month" = 7 AND "day" = 29 AND city = 'Fiftyville'
    ORDER BY "hour", "minute"
    LIMIT 1
);
-- only bruce in this list and diana no so the thief is bruce
-- see where bruce escape to
SELECT city FROM airports
WHERE id = (
    SELECT destination_airport_id FROM flights
    JOIN airports ON airports.id = flights.origin_airport_id
    WHERE "year" = 2023 AND "month" = 7 AND "day" = 29 AND city = 'Fiftyville'
    ORDER BY "hour", "minute"
    LIMIT 1
);
-- its New York City
-- see who helped bruce
SELECT name FROM people
WHERE phone_number IN (
    SELECT "receiver" FROM phone_calls
    WHERE "caller" = (
        SELECT phone_number FROM people
        WHERE "name" = 'Bruce'
    )
    AND "year" = 2023 AND "month" = 7 AND "day" = 28 AND duration < 60
);
-- so its Robin
