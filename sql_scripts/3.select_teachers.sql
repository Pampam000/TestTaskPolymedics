SELECT t.*, c.number AS room
FROM Teacher t
JOIN Classroom c
ON t.classroom_id = c.id
WHERE c.building_number = 3;