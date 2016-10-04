# -- Matt Caudill

# teacher(id, dept, name, phone, mobile)
# dept(id, name)

#1. List the teachers who have NULL for their department
SELECT name FROM teacher
WHERE dept IS NULL

#2. Inner join misses the teachers with no departments
SELECT teacher.name, dept.name
FROM teacher INNER JOIN dept ON(teacher.dept=dept.id)

#3. Use a different join so that all teachers are listed
SELECT teacher.name, dept.name
FROM teacher LEFT JOIN dept ON(teacher.dept = dept.id)

#4. Use a different join so that all depts are listed
SELECT teacher.name, dept.name
FROM teacher RIGHT JOIN dept ON(teacher.dept=dept.id)

#5. Use COALESCE to show teacher name and number or default number
SELECT name, COALESCE(mobile, '07986 444 2266') FROM teacher

#6. Print teacher name and department name for all teachers using NONE when
# there is no dept
SELECT teacher.name, COALESCE(dept.name, 'None') AS department
FROM teacher LEFT JOIN dept ON(teacher.dpet = dept.id)

#7. Use count to show the number of teachers and the number of mobiles
SELECT COUNT(name), COUNT(mobile) FROM teacher

#8. Use COUNT and GROUPBY dept.name to show each dept and # of staff. Use
# Right Join to ensure engineering is listed
SELECT dept.name, COUNT(teacher.name)
FROM teacher RIGHT JOIN dept ON(teacher.dept=dept.id)
GROUP BY dept.name

#9. USE case to show the name of each teacher followed by 'Sci' if they are
# in dept 1,2 and 'Art' otherwise
SECLECT name, 
CASE WHEN teacher.dept IN (1,2) THEN 'Sci'
     ELSE 'Art'
END
FROM teacher

#10. Use case to label teacher as sci if dept in (1,2), Art if in (3) and
# None otherwise
SELECT name, 
CASE WHEN teacher.dept IN (1,2) THEN 'Sci'
     WHEN teacher.dept = 3 THEN 'Art'
     ELSE 'None'
END
FROM teacher

# Quiz #
########
#1. Select the code which uses Join correctly
SELECT teacher.name, dept.name FROM teacher LEFT OUTER JOIN dept
ON(teacher.dept > dept.id)

#2. Show the name of department which employs Cutflower
SELECT dept.name FROM teacher JOIN dept ON(teacher.dept=dept.id)
WHERE teacher.name='Cutflower'

#3. Show the list of all depts and number of employed teachers
SELECT dept.name, COUNT(teacher.name)
FROM teacher RIGHT JOIN dept ON(teacher.dept = dept.id)
GROUP BY dept.name

#4. SELECT name, dept, COALESCE(dept,0) AS result FROM teacher yields
# 2-- displays 0 in result column for teachers without a dept

#5. The following query yields what?
SELECT name,
CASE WHEN phone = 2752 THEN 'two'
     WHEN phone = 2753 THEN 'three'
     WHEN phone = 2754 THEN 'four'
END AS digit
FROM teacher
# shows four for Throd

#6. The following code yields
SELECT name,
CASE WHEN dept IN (1) THEN 'Computing'
ELSE 'Other'
END
FROM teacher
# this give table A
