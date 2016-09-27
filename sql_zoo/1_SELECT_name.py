# -- Matt Caudill

#1. Find the country that starts with Y
SELECT name FROM world
WHERE name LIKE 'Y%'

#2. Find the country that ends in Y
SELECT name FROM world
WHERE name LIKE '%y'

#3. Find the countries that contain the letter x
SELECT name FROM world
WHERE name LIKE '%x%'

#4. Find countries ending with 'land'
SELECT name FROM world
WHERE name LIKE '%land'

#5. Find countries starting with 'C' and ending with 'ia'
SELECT name FROM world
WHERE name LIKE 'C%ia'

#6. Find name with a double o
SELECT name FROM world
WHERE name LIKE '%oo%'

#7. Find names with three a's
SELECT name FROM world
WHERE name LIKE '%a%a%a%'

#8. Find the countries that have a 't' as the second character
SELECT name FROM world
WHERE name LIKE '_t%'

#9. Find countries with two o's separated by two other characters
SELECT name FROM world
WHERE name LIKE '%o__o%'

#10. Find the countries that have exactly four characters
SELECT name FROM world
WHERE name LIKE '____'

#11. Find countries where the capital has the same name as the country
SELECT name  FROM world
WHERE name LIKE capital

#12. Find the countries where the capital is the country + city (eg Mexico
# City)
SELECT name FROM world
WHERE capital LIKE concat(name,' City')

#13. Find the capital and name where the capital includes the name of the
# country
SELECT capital, name FROM world
WHERE capital LIKE concat('%',name,'%')

#14. Find the capital and name where the capital is an extension of name of
# country
SELECT name, capital FROM world
WHERE capital LIKE concat(name,'_%')

#15. Find the name and the extension where the capital is an extension of
# the name of the country 
SELECT name, replace(capital,name,'') FROM world
WHERE capital LIKE concat(name,'_%')

