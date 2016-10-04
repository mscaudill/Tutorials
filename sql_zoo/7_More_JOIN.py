# -- Matt Caudill

# three tables movie(id, title, yr, director, budget, gross)
#              actor(id, name)
#              casting(movieid, actorid, ord)

#1. List the films where the yr is 1962 show id, title
SELECT id, title 
FROM movie
WHERE yr = 1962

#2. list the year of Citizen Kane
SELECT yr 
FROM movie
WHERE title='Citizen Kane'

#3. List all the Star Trek movies include id, title, yr. Order by yr
SELECT id, title, yr
FROM movies
WHERE title LIKE '%Star Trek%'
ORDER BY yr

#4. What are the film titles with these ids 11768, 11955, 21191
SELECT title
FROM movie
WHERE id IN (11768, 11955, 21191)

#5. what id number does the actress Glenn Close have
SELECT id 
FROM actor 
WHERE name = 'Glenn Close'

#6 What is the id of the film Casablanca
SELECT id 
FROM movie
WHERE title='Casablanca'

#7. Obtain the cast list from Casablanca
SELECT name FROM casting JOIN actor ON actorid=id
WHERE movieid=11768

#8. Obtain the cast list for the film Alien
SELECT name FROM casting JOIN actor ON actorid=id
WHERE movieid = (SELECT id FROM movie WHERE title='Alien')

#9. List the films in which Harrison Ford appeared
SELECT title
FROM movie JOIN casting id=movieid
WHERE actorid = (SELECT id FROM actor WHERE name='Harrison Ford')

#10. Find the films Harrison Ford has appeared in but not in the starring
# role
SELECT title
FROM movie JOIN casting ON id=movieid
WHERE actorid = (SELECT id FROM actor WHERE name='Harrison Ford')
AND ord != 1

#11. List the films together with the leading star for all 1962 films
SELECT title, name
FROM movie JOIN casting ON(id=movieid)
JOIN actor ON(actor.id = actorid)
WHERE ord=1 AND yr = 1962

#12. show the year and the number of movies for any year in which John
# Travolta made more than 2 movies
SELECT yr, COUNT(title)
FROM movie JOIN casting ON(movie.id = casting.movieid)
JOIN actor ON(casting.actorid = actor.id)
WHERE name = 'John Travolta'
GROUP BY yr
HAVING COUNT(title) > 2

#13. List the film and the leading actor for all films Julie Andrews played
# in
SELECT title, name
FROM movie JOIN casting ON(movie.id = casting.movieid) 
JOIN actor ON(casting.actorid = actor.id)
WHERE ord = 1 AND movieid IN
(SELECT movieid FROM casting JOIN actor ON(actorid=id)
WHERE name='Julie Andrews')

#14. Obtain an alphabetical list of actors who had at least 30 starring
# roles
SELECT name FROM casting JOIN actor ON(casting.actorid = actor.id)
WHERE ord=1
GROUP BY name
HAVING COUNT(movieid) >= 30
ORDER BY name

#15. List the films released in the year 1978 ordered by the number of
# actors in the cast then by title
SELECT title, COUNT(ord)
FROM movie JOIN casting ON(movie.id = casting.movieid)
WHERE yr = 1978
GROUP BY title
ORDER BY COUNT(ord) DESC, title

#16. List all the people who have worked with Art Garfunkel
SELECT DISTINCT name FROM casting JOIN actor ON(actorid=id)
WHERE movieid IN (SELECT movieid FROM casting JOIN actor ON(actorid=id)
WHERE name='Art Garfunkel') AND name!='Art Garfunkel'

# QUIZ #
########
#1. List the directors of the movies which have netted a loss
SELECT name 
FROM actor JOIN movie ON actor.id = director
WHERE gross < budget

#2. SELECT the correct example of joinin three tables
SELECT * 
FROM actor JOIN casting ON actor.id = actorid
JOIN movie ON movie.id = movieid

#3. Find the list of actors called John by order of movies in which they
# acted
SELECT name, COUNT(movieid)
FROM casting JOIN actor on actorid=actor.id
WHERE name LIKE 'John %'
GROUP BY name
ORDER BY 2 DESC

#4. Select the table the following code would yield
SELECT title
FROM movie JOIN casting ON (movieid = movie.id)
JOIN actor ON (actorid = actor.id)
WHERE name='Paul Hogan' AND ord=1
# yields table B

#5. Select the code that yields all the actors that starred in movies dir by
# Ridley scott who has id 351
SELECT name
FROM movie JOIN casting ON movie.id = movieid
JOIN actor ON actor.id = actorid
WHERE ord = 1 AND director = 351

#6. Two ways to link movie and actor
# link the dir column of movies with primary key in actor
# connect primary keys of movie and actor via casting

#7. Find the table given by
SELECT title,yr
FROM movie, casting, actor
WHERE name='Robert De Niro' ANS movieid=movie.id AND actorid=actor.id
AND ord = 3
#Table 3
