# -- Matt Caudill

#world(name, continent, area, population, gdp)

#1. List each country name where the population is larger than russia
SELECT name FROM world
WHERE population > (SELECT population FROM world WHERE name='Russia')

#2. Show the countries in Europe with a per capita GDP > UK
SELECT name FROM world
     WHERE continent='Europe' AND gdp/population >
     (SELECT gdp/population FROM world WHERE name='United Kingdom')

#3. List the name and continent of countries in the continents containing
# either Argentina or Australia. Order by name
SELECT name, continent FROM world
 WHERE continent IN 
 (SELECT continent FROM world WHERE name IN ('Argentina', 'Australia'))
 ORDER BY name

#4. Find the countries with populations > Canada but < Poland
SELECT name, population FROM world
 WHERE population > (SELECT population FROM world WHERE name = 'Canada')
 AND population < (SELECT population FROM world WHERE name = 'Poland')

#5. Show the name and population of each country in Europe. Show the
# population as a percentage of the population of Germany
SELECT name, 
       concat(ROUND(population/(SELECT population FROM world 
                                WHERE name='Germany')*100,0), '%')
FROM world WHERE continent = 'Europe'

#6. Find countries that have a gdp greater than every country in Europe
# ALL allows comparisons with select list
SELECT name FROM world
WHERE gdp > ALL(SELECT gdp FROM world WHERE gdp > 0 AND continent='Europe')

#7.Find the largest country by area in each continent, show continent name
# and area 
SELECT continent, name, area FROM world x
WHERE area >= ALL(SELECT area FROM world y 
                  WHERE y.continent = x.continent
                  AND area > 0)

#8. List each continent and the name of the country that comes first
# alphabetically
SELECT continent, name FROM world x
WHERE name<=ALL(SELECT name FROM world y WHERE y.continent = x.continent)

#9 Find the continents where all countries have a pop <=25e6. Then find the
# names of the countries in these continents
SELECT name, continent, population FROM world x
WHERE 25e6 >= ALL(SELECT population FROM world y WHERE
                  y.continent=x.continent)

#10. Find countries with > 3x their neighbors in the same conitinent. Find
# countries and continents
SELECT name, continent FROM world x
WHERE population >= 3*ALL(SELECT population FROM world y WHERE
                          y.continent=x.continent AND
                          x.name!=y.name)

