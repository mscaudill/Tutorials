# -- Matt Caudill

# stops(id, name)
# route(num,company, pos, stop)

# 1. How many stops are there in the database
SELECT COUNT(name) FROM stops

#2. Find the id value of the stop Craiglockhart
SELECT id
FROM stops 
WHERE name = 'Craiglockhart'

#3. Find the id and name for the stops on the '4' 'LRT' service
SELECT id, name 
FROM stops JOIN route ON(stops.id = route.stop)
WHERE num='4' AND company='LRT'

#4. Restrict outputs to stops that have a count of 2
SELECT company, num, COUNT(*)
FROM route WHERE stop=149 OR stop=53
GROUP BY company, num
HAVING COUNT(*)=2

#5. Change the query so that it shows the services from craiglockhart to
# london road
SELECT a.company, a.num, a.stop, b.stop
FROM route a JOIN route b ON(a.company=b.company AND a.num=b.num)
WHERE a.stop=53 AND b.stop=149

#6. Same as 5 but using name refernce instead of stop id number
SELECT a.company, a.num, stopa.name, stopb.name
FROM route a JOIN route b ON
(a.company=b.company AND a.num=b.num)
JOIN stops stopa ON(a.stop=stopa.id)
JOIN stops stopb ON(b.stop=stopb.id)
WHERE stopa.name='Craiglockhart' AND stopb.name='London Road'

#7. Give a list of all the routes which connect stops 115 and 137
# Haymarket and Leith
SELECT DISTINCT a.company, a.num
FROM route a JOIN route b ON
(a.company=b.company AND a.num=b.num)
JOIN stops stopa ON(a.stop=stopa.id)
JOIN stops stopb ON(b.stop=stopb.id)
WHERE stopa.name='Haymarket' AND stopb.name='Leith'

#8. Give a list of the services whcih connect 'Craiglockhart' and
# 'Tollcross'
SELECT DISTINCT a.company, a.num
FROM route a JOIN route b ON
(a.company = b.company AND a.num=b.num)
JOIN stops stopa ON(a.stop = stopa.id)
JOIN stops stopb ON(b.stop = stopb.id)
WHERE stopa.name = 'Craiglockhart' AND stopb.name = 'Tollcross'

#9. Give a list of the distinct stops that may be reached from craiglockhart
# by taking one bus offered by the LRT company. include company and bus#
SELECT DISTINCT stopb.name, a.company, a.num
FROM route a JOIN route b ON(a.company=b.company AND a.num=b.num)
JOIN stops stopa ON(a.stop=stopa.id)
JOIN stops stopb ON(b.stop=stopb.id)
WHERE stopa.name='Craiglockhart'

#10. Find the routes involving two buses that go from Craiglockhart to
# Sighthill show bus # and company for the first bus, the stop name and the
# name of the stop for the transfer
SELECT DISTINCT a.num, a.company, stopb.name ,  c.num,  c.company
FROM route a JOIN route b
ON (a.company = b.company AND a.num = b.num)
JOIN ( route c JOIN route d ON (c.company = d.company AND c.num= d.num))
JOIN stops stopa ON (a.stop = stopa.id)
JOIN stops stopb ON (b.stop = stopb.id)
JOIN stops stopc ON (c.stop = stopc.id)
JOIN stops stopd ON (d.stop = stopd.id)
WHERE  stopa.name = 'Craiglockhart' AND stopd.name = 'Sighthill'
AND  stopb.name = stopc.name
ORDER BY LENGTH(a.num), b.num, stopb.id, LENGTH(c.num), d.num

# Quiz #
########

#1. show that it is possible to get from Craiglockhart to Haymarket

