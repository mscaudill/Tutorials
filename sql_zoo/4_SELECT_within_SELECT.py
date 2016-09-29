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

# Nested Select Quiz #
######################
# bbc(name, region, area, population, gdp)

#1.  Show name region and population of the smallest country in each region
SELECT name, region, population FROM bbc x
WHERE population <= ALL(SELCECT population FROM bbc y WHERE y.region =
        x.region AND population > 0)

#2. Show the countries belonging to regions with all pops > 50,000
SELECT name, region, population FROM bbx x
WHERE 50e3 < ALL(SELECT population FROM bbc y where y.region = x.region AND
        y.population >0)

#3. Find the countries with less than 1/3 the population of the countries
# around it
SELECT name, region FROM bbc x
WHERE population < ALL(SELECT population/3 FROM BBC y WHERE
        x.region=y.region AND y.name != x.name)

#4. Select the result from the following code
SELECT name FROM bbc
WHERE population > (SELECT population FROM bbc WHERE name = 'UK')
AND region IN (SELECT region FROM bbc WHERE name = 'UK')
# Should be table D

#5. Show the countries with a greater GDP tan any countru in africa
SELECT name FROM bbc
WHERE gdp > ALL(SELECT MAX(gdp) FROM bbc WHERE region='Africa')

#6. Find the countries with populations smaller than Russia but bigger than
# Denmark
SELECT name FROM bbc
WHERE population < (SELECT population FROM bbc WHERE name = 'Russia')
AND population > (SELECT population FROM bbc WHERE name = 'Denmark')

#7. Find the result of the following code
SELECT name FROM bbc
WHERE population > ALL(SELECT MAX(population) FROM bbc WHERE
        region='Europe') AND region = 'South Asia'
# Table B

