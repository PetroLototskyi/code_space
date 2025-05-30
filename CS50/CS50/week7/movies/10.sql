SELECT DISTINCT people.name
FROM people
JOIN directors ON people.id = directors.person_id
WHERE directors.movie_id IN (
    SELECT ratings.movie_id
    FROM ratings
    WHERE ratings.rating >= 9.0
);
