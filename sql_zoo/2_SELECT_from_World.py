# -- Matt Caudill

#2. Find countries with a population of at least 200 million
SELECT name FROM world
WHERE population > 200e6

#3. Find name and per capita GDP for countries where pop>200 million
SELECT name, gdp/population FROM world
WHERE population > 200e6

#4. Find the name and population in millions of countries in South America
SELECT name, population/1e6 FROM world
WHERE continent='South America'

#5. Find the name and population for France, Germany and Italy
SELECT name, population FROM world
WHERE name IN ('France', 'Germany', 'Italy')

#6. Find countries with names that begin with 'United'
SELECT name FROM world
WHERE name LIKE 'United%'

#7. Find countries that are large by population or by area
SELECT name, population, area FROM world 
WHERE population > 250e6 OR area > 3e6

#8. Find countries that are big by area or population but not both
SELECT name, population, area FROM world
WHERE population > 250e6 XOR area > 3e6

#9. Find name population(in millions) and GDP(in Billions) for South
# America rounded to 2 decimals
SELECT name, ROUND(population/1e6,2), ROUND(gdp/1e9,2) FROM world
WHERE continent = 'South America'

#10. Find the name and per-capita GDP for countries with 1e12 of GDP. Round
# this to nearest 1000
SELECT name, ROUND(gdp/population,-3) FROM world 
WHERE gdp > 1e12

#11. substitute Australasia for Oceania for countries beginning with N
SELECT name, 
    CASE WHEN continent = 'Oceania' THEN 'Australasia'
         ELSE continent END
FROM world
WHERE name LIKE 'N%'

#12. Show name and continent but substitute Eurasia for Europe and Asia,
#substitute America for each country in North America or South America or
#Caribbean. Show countries beinning with A or B
SELECT name, 
    CASE WHEN continent IN ('Europe','Asia') THEN 'Eurasia'
         WHEN continent IN ('North America','South America','Caribbean')
         THEN 'America'
    ELSE continent END
FROM world
WHERE name LIKE 'A%' OR name LIKE 'B%'

#13.
SELECT name, continent,
CASE WHEN continent = 'Oceania' THEN 'Australasia'
     WHEN continent = 'Eurasia' OR name = 'Turkey' THEN 'Europe/Asia'
     WHEN continent = 'Caribbean' AND name LIKE 'B%' THEN 'North America'
     WHEN continent = 'Caribbean' AND name NOT LIKE 'B%' THEN 'South America
     '
     ELSE continent END
FROM world
ORDER BY name

# BBC Quiz

#1. Find the names of the countries that begin with the letter U
SELECT name FROM world
WHERE name like 'U%'

#2. Find the table with just the population of the UK
SELECT population FROM world
WHERE name='United Kingdom'

#3. Identify the problem with the following sql code
SELECT continent FROM world
WHERE 'name' = 'France'
# 'name' is a column of the table and should be referenced like name nt
# 'name'

#4. What does the following code yield
SELECT name, population / 10 FROM world
WHERE population < 10000
# Table 4

#5. Find the name and populations of countries in Europe and Asia
SELECT name, population FROM world
WHERE continent IN ('Europe', 'Asia')

#6. Select the code that would yield two row table
SELECT name FROM world
WHERE name IN ('Cuba', 'Togo')

#7. Which table does this code yield
SELECT name FROM world
WHERE continent = 'South America' AND population > 40000000
