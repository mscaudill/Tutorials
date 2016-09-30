# -- Matt Caudill

# game(id, mdate, stadium, team1, team2)
# goal(matchid, teamid, player, gtime)
# eteam(id, teamname, coach)

#1. Show the matchid and player for all goals scored by Germany
SELECT matchid, player FROM goal
WHERE teamid='GER'

#2. Find id,stadium and the teams in matchid 1012
SELECT id, stadium, team1, team2 FROM game
WHERE id = 1012

#3. The previous two commands can be combined into a single join
SELECT * FROM game JOIN goal ON (id=matchid)
# Show the player, teamid, stadium and mdate for every German goal
SELECT player, teamid, stadium, mdate FROM game JOIN goal ON (id=matchid)
WHERE teamid='GER'

#4. Show team1, team2, and player for every goal scored by a player called
# Mario
SELECT team1, team2, player FROM game JOIN goal ON(id=matchid)
WHERE player LIKE 'Mario%'

#5. Show the player, teamid, coach, gtime for all goals scored in the first
# 10 mins gtime<=10
SELECT player, teamid, coach, gtime FROM goal JOIN eteam ON(teamid=id) 
WHERE gtime<=10

#6. List the dates of the matches and the name of the team in which Fernando
# Santos was the team1 coach
SELECT mdate, teamname FROM game JOIN eteam ON(game.team1 = eteam.id)
WHERE coach = 'Feranando Santos'

#7. List the player for every goal scored in a game where the stadium was
# 'National Stadium, Warsaw'
SELECT player FROM goal JOIN game ON(goal.matchid=game.id)
WHERE stadium = 'National Stadium, Warsaw'

#8. Show the name of all players who scored a goal against Germany
SELECT DISTINCT player FROM goal JOIN game ON(goal.matchid = game.id)
WHERE 'GER' IN (team1,team2) AND teamid != 'GER'

#9. Show teamname and the total number of goals scored
SELECT teamname, COUNT(player) FROM eteam JOIN goal
ON(eteam.id=goal.teamid)
GROUP BY teamname

#10. Show the stadium and the number of goals
SELECT stadium, COUNT(player) FROM game JOIN goal ON(id=matchid)
GROUP BY stadium

#11. For every match involving 'POL' show matchid, date, and # of goals
SELECT matchid, mdate AS date, COUNT(player) AS goals 
FROM game JOIN goal ON(game.id = goal.matchid AND 'POL' IN (team1, team2))
GROUP BY matchid, mdate

#12. For every match were 'GER' scored, show matchid, mdate, and # goals
# scored by GER
SELECT matchid, mdate, COUNT(player) AS goals
FROM game JOIN goal ON(game.id = goal.matchid 
        AND 'GER' IN (team1, team2)
        AND teamid = 'GER')
GROUP BY matchid, mdate

#13. List every match with the goals scored by each team
SELECT mdate, team1,
       SUM(CASE WHEN teamid=team1 THEN 1 ELSE 0 END) AS score1,
       team2,
       SUM(CASE WHEN teamid=team2 THEN 1 ELSE 0 END) AS score2
FROM game LEFT JOIN goal ON matchid=id
GROUP BY mdate, team1, team2
ORDER BY mdate, matchid, team1, team2

# Join Quiz #
#############

#1. Find the stadium where 'Dimitris Salpingdis' scored
SELECT stadium FROM game JOIN goal ON game.id = goal.matchid
WHERE player = 'Dimitris Salpingdis'

#2. What col names may be used in goal JOIN eteam
matchid, teamid, player, gtime, id, teamname, coach

#3. Find the players, team, and the amt of goals scored against Greece
SELECT player, teamid, COUNT(*) AS goals 
FROM goal JOIN game ON matchid = id
WHERE 'GRE' IN (team1, team2) AND teamid !='GRE'
GROUP BY player, teamid

#4. Find the result of the following code
SELECT DISTINCT teamid, mdate
FROM goal JOIN game ON (matchid = id)
WHERE mdate = '9 June 2012'
# Table 1

#5. Show the player and their team for those who have scored against POL in
# National Stadium, Warsaw
SELECT DISTINCT player, teamid
FROM game JOIN goal ON(matchid = id)
WHERE 'POL' IN (team1, team2) 
AND teamid != 'POL' 
AND stadium = 'National Stadium, Warsaw' 

#6. Find the player, their team and the time they scored who have played in
# Stadion Miejski but not against ITA
SELECT DISTINCT player, teamid, gtime
FROM game JOIN goal ON (matchid = id)
WHERE stadium = 'Stadion Miejski (Wroclaw)'
AND ((teamid=team2 AND team1 !='ITA') OR (teamid=team1 AND team2 !='ITA'))

#7. Select the result of the following code
SELECT teamname, COUNT(*)
FROM eteam JOIN goal on teamid=id
GROUP BY teamname
HAVING COUNT(*) < 3

