# -- Matt Caudill

# nobel(yr, subject, winner)

#1. Write a query for the nobel table that displays prizes in 1950.
SELECT yr, subject, winner FROM nobel
WHERE yr = 1950

#2. Who won the the 1962 Prize for literature
SELECT winner FROM nobel
WHERE yr = 1962 AND subject = 'Literature' 

#3. Find the year and subject of the Eistein's Nobel
SELECT yr, subject FROM nobel
WHERE winner = 'Albert Einstein'

#4. Find the name of the Peace winners since the year 2000 inclusive
SELECT winner FROM Nobel
WHERE subject = 'Peace' AND yr >= 2000

#5. Find all cols of the literature prize winners for 1980 to 1989 inclusive
SELECT yr, subject, winner FROM nobel
WHERE subject = 'Literature' AND yr >= 1980 AND yr <= 1989

#6. Show all details of the following winners Roosevelt, Wilson, Carter
SELECT * FROM nobel
WHERE winner IN ('Theodore Roosevelt', 'Woodrow Wilson', 'Jimmy Carter')

#7. Find the winners with the first name John
SELECT winner FROM nobel
WHERE winner LIKE 'John %'

#8. Show the Physics winners for 1980 with the chemistry winners for 1984
SELECT * FROM nobel
WHERE subject='Physics' AND yr = 1980 OR subject='Chemsitry' AND yr = 1984

#9. Show the winners for 1980 excluding Chemistry and Medicine
SELECT * FROM nobel
WHERE yr = 1980 AND subject NOT IN ('Chemsitry', 'Medicine')

#10. How who won a medicine prize prior to 1910 togehter with Literature
# prizes in 2004 and later
SELECT * FROM nobel
WHERE subject = 'MEDICINE' AND yr < 1910 OR 
      subject='Literature' AND yr >= 2004

#11. Find All Details of the prize won by Peter Grünberg (compose + "u)
SELECT * FROM nobel
WHERE winner = 'Peter Grünberg'

#12. Find all details for winner Eugene O'Neil (double quotes inside str)
SELECT * FROM nobel
WHERE winner = 'Eugene O''Neill'

#13. List * for winners where winner starts with Sir. Show the most recent
# first then by name order
SELECT winner, yr, subject FROM nobel
WHERE winner LIKE 'Sir %'
ORDER BY yr DESC, winner

#14. Show 1984 winneres and subject ordered by subject and winner name; but
# list Chemistry and Physics last.
SELECT winner, subject FROM nobel
WHERE yr = 1984
ORDER BY subject IN ('Physics', 'Chemsitry'), subject, winner

# Nobel Quiz #
##############

#1. Find the winners names that begin with C and end with n
SELECT winner FROM nobel
WHERE winner LIKE 'C%' AND winner LIKE '%n'

#2. How many chemistry awards were given between 1950 and 1960
SELECT COUNT(subject) FROM nobel
WHERE subject = 'Chemistry' AND yr BETWEEN 1950 AND 1960

#3. Find the amount of years where no medicine awards were given
SELECT COUNT(DISTINCT yr) FROM nobel
WHERE yr NOT IN (SELECT DISTINCT yr FROM nobel WHERE subject = 'Medicine')

#4.
SELECT subject, winner FROM nobel WHERE winner LIKE 'Sir%' AND yr LIKE
'196%'
# This would give Table 3

#5. Show the year in which neither a Physics or Chemistry award was given
SELECT yr FROM nobel
WHERE yr NOT IN (SELECT yr FROM nobel WHERE subject IN
('Chemistry','Physics'))

#6. Find years when medicine award was given but no peace or lit award was
SELECT DISTINCT yr FROM nobel
WHERE subject='Medicine' AND yr NOT IN (SELECT yr FROM nobel
                                        WHERE subject='Literature')
                         AND yr NOT IN (SELECT yr FROM nobel
                                        WHERE subject='Peace')

#7. Pick the table
SELECT subject, COUNT(subject) FROM nobel
WHERE yr='1960'
GROUP BY subject
# Gives table 4
