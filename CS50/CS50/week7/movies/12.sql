SELECT movies.title
FROM movies
JOIN stars AS s1 ON movies.id = s1.movie_id
JOIN people AS p1 ON p1.id = s1.person_id AND p1.name = 'Bradley Cooper'
JOIN stars AS s2 ON movies.id = s2.movie_id
JOIN people AS p2 ON p2.id = s2.person_id AND p2.name = 'Jennifer Lawrence';
