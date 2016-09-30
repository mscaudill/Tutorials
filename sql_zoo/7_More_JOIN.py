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
