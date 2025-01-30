SELECT DISTINCT people.name
FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
JOIN stars kb_stars ON movies.id = kb_stars.movie_id
JOIN people kb ON kb_stars.person_id = kb.id AND kb.name = 'Kevin Bacon' AND kb.birth = 1958
WHERE people.name <> 'Kevin Bacon';
