SELECT movies.title FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
Where people.name IN ('Bradley Cooper', 'Jennifer Lawrence')
GROUP BY movies.id
HAVING COUNT(DISTINCT people.name) = 2;

-- HAVING Clause: It checks that both actor names are present in the results by counting distinct names and ensuring the count is 2.