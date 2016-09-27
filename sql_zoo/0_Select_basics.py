# -- Matt Caudill 

# 1. Select population from world table where name = 'Germany'
SELECT population FROM world
WHERE name = 'Germany'

# 2. Select name and population from world that are "IN" the list
# (Ireland, Iceland, Denmark)
SELECT name, population FROM world
WHERE name IN ('Ireland', 'Iceland', 'Denmark')

# 3. Find Countries with areas "BETWEEN" two sizes
SELECT name, area FROM world
WHERE area BETWEEN 200000 AND 250000

# Quiz#
#######
#1.
SELECT name, population FROM world
WHERE population BETWEEN 1000000 AND 1250000

#2.
Table E

#3.
SELECT name FROM WORLD
WHERE name LIKE '%a' OR name LIKE '%l'

#4. 
SELECT name LENGTH(name)
FROM world
WHERE LENGTH(name)=5 AND region='Europe'
#produces table 3

#5. 
SELECT name, area*2 FROM world
WHERE population = 64000
# produces table 3

#6. The query that shows countries with area > 50000 and pop < 100e6
SELECT name, area, population FROM world
WHERE area > 50000 AND population < 10000000

#7. The query returning the pop density of China, Australia, Nigeria and
# France is 
SELECT name, population/area FROM WORLD
WHERE name IN ('China', 'Australia', 'Nigeria', 'France')

