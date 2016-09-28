# --Matt Caudill

# world(name, continent, area, population, gdp)

#1 Show the population of the world
SELECT SUM(population) FROM world

#2. List all the continents just once
SELECT DISTINCT(continent) FROM world

#3. Find the total GDP of Africa
SELECT SUM(gdp) FROM world
WHERE continent = 'Africa'

#4. How many countries have an area of at least 1e6
SELECT COUNT(name) FROM world
WHERE area > 1e6

#5. What is the combined population of France, Germany and Spain
SELECT SUM(population) FROM world
WHERE name IN ('France', 'Germany', 'Spain')

#6. For each continent show the continent and the number of countries
SELECT continent, COUNT(name) FROM world
GROUP BY continent

#7. For each continent show the continent and the number of countries with
# populations of at least 10 million
SELECT continent ,COUNT(name) FROM world
WHERE population > 10e6
GROUP BY continent

#8. List the continents that have a total population of >= 100e6
SELECT continent FROM world
GROUP BY continent
HAVING SUM(population)>100e6

# SUM and COUNT Quiz #
######################

#1. Find the sum of population of all countries in Europe
SELECT SUM(population) FROM bbc
WHERE region = 'Europe'

#2. Find the number of countries with populations < 150e3
SELECT COUNT(name) FROM bbc
WHERE population < 150e3

#3. The list of core SQL aggregate functions are
# AVG COUNT MAX MIN SUM

#4 Which table does the following give
SELECT region, SUM(area) FROM bbc
WHERE SUM(area) > 15e6
GROUP BY region
# NO RESULT - invalid use of WHERE should use HAVING to filter after GROUP
# BY

#5. Find the average population of Poland Germany and Denmark
SELECT AVG(population) FROM bbc
WHERE name IN ('Poland', 'Germany', 'Denmark')

#6. Find the average population  density of each region
SELECT region, SUM(population)/SUM(area) AS density FROM bbc
GROUP BY region

#7. Find the name and population density of the country with the largest
# population
SELECT name, population/area AS density FROM bbc
WHERE population = (SELECT MAX(population) FROM bbc)

#8. Pick the table
SELECT region, SUM(area) FROM bbc
GROUP BY region
HAVING SUM(area)<=20e6
# yields table D
