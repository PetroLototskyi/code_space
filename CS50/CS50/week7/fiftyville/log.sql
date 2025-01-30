-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Find crime scene description
 SELECT description FROM crime_scene_reports WHERE month = 7 AND day = 28 AND year = 2021 AND street = 'Humphrey Street';

-- | Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery. |
-- Let see these transcripts
SELECT transcript FROM interviews WHERE year=2021 AND month =7 AND transcript LIKE "%bakery%";

--Let check security camera for 10 minutes from 10:15 am. according to first witness to see the car license. Combine the query with people table to get info of drivers
SELECT b.activity, b.license_plate, p.name, p.phone_number, p. passport_number FROM bakery_security_logs b
JOIN people p ON b.license_plate=p.license_plate
WHERE b.year =2021
AND b.month =7 AND b.day=28 AND b.hour =10 AND b.minute>=
15 AND b.minute<=25;
-- We have list of 8 ( Vanessa, Bruce, Barry, Luca, Sofia, Iman, Diana, Kelsey) suspect and their info now

--Let's check the information from the  second witness about ATM withdrawal transaction done by thief. We need to combine 3 tables
SELECT p.name, atm.transaction_type FROM people p
JOIN bank_accounts b ON b.person_id=p.id
JOIN atm_transactions atm ON atm.account_number=b.account_number
WHERE atm.year=2021
AND atm.month=7
AND atm.day=28
AND atm.atm_location= "Leggett Street"
AND atm.transaction_type="withdraw";
--We can see some names repeat names in previous query list (Bruce, Diana, Iman, Luca). Our list become more narrow

--Let checK information of third witness. We need to check does our suspect made the call at mentioned time
SELECT p.caller, pe.name, p.receiver, pe2.name FROM phone_calls p JOIN people pe ON pe.phone_number=p.caller
JOIN people pe2 ON pe2.phone_number=p.receiver WHERE year =2021 AND month =7 AND day =28 And duration <60;
--Now our suspect list narrowed just to two names (Bruce called Robin and Diana called Philip)

--//--//--//
---Let check what was the the earliest next day flight. This is information from third witness
SELECT f.id, f.origin_airport_id, a.city, f.destination_airport_id, a2.city FROM flights f
JOIN airports a ON f.origin_airport_id=a.id
JOIN airports a2 ON f.destination_airport_id=a2.id
WHERE year = 2021 AND month = 7 AND day =29 ORDER BY hour LIMIT 1;
-- The earliest next day flight was to flight  to New York City

--Now thats check the flight passengers
SELECT pa.passport_number, p.name FROM passengers pa
JOIN people p ON pa.passport_number=p.passport_number
JOIN flights f ON f.id=pa.flight_id
WHERE f.id=36;
--In the outcome we can see that only one name match name from our suspects list. This is Bruce.
--He is the thief and the person he called will be his assistant. Which is Robin
--//--//--//

--WE CAN COMBINE TWO ABOVE queries (marked with --//--//--//) into one and make it dynamic:
SELECT pa.passport_number, p.name, a2.city FROM passengers pa
JOIN people p ON pa.passport_number=p.passport_number
JOIN flights f ON f.id=pa.flight_id
JOIN airports a2 ON f.destination_airport_id=a2.id
WHERE f.id IN (
SELECT f.id FROM flights f
JOIN airports a ON f.origin_airport_id=a.id
WHERE year = 2021 AND month = 7 AND day =29 ORDER BY hour LIMIT 1);
-----------------------------------------------------------------------------------------------


--NOW to make it fun let's combine all queries that reference to suspect list into one using INTERSECT operator.
--We dynamically received the thief name which is -"Bruce"
SELECT name
FROM (
    -- Query 1
    SELECT p.name
    FROM bakery_security_logs b
    JOIN people p ON b.license_plate = p.license_plate
    WHERE b.year = 2021
      AND b.month = 7
      AND b.day = 28
      AND b.hour = 10
      AND b.minute >= 15
      AND b.minute <= 25

    INTERSECT

    -- Query 2
    SELECT p.name
    FROM people p
    JOIN bank_accounts b ON b.person_id = p.id
    JOIN atm_transactions atm ON atm.account_number = b.account_number
    WHERE atm.year = 2021
      AND atm.month = 7
      AND atm.day = 28
      AND atm.atm_location = 'Leggett Street'
      AND atm.transaction_type = 'withdraw'

    INTERSECT

    -- Query 3
    SELECT pe.name
    FROM phone_calls p
    JOIN people pe ON pe.phone_number = p.caller
    JOIN people pe2 ON pe2.phone_number = p.receiver
    WHERE year = 2021
      AND month = 7
      AND day = 28
      AND duration < 60

    INTERSECT

    -- Query 4
    SELECT p.name
    FROM passengers pa
    JOIN people p ON pa.passport_number = p.passport_number
    JOIN flights f ON f.id = pa.flight_id
    JOIN airports a2 ON f.destination_airport_id = a2.id
    WHERE f.id IN (
        SELECT f.id
        FROM flights f
        JOIN airports a ON f.origin_airport_id = a.id
        WHERE year = 2021
          AND month = 7
          AND day = 29
        ORDER BY hour
        LIMIT 1
    )
) AS common_names;

