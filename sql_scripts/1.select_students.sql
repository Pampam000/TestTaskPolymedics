SELECT s.*
FROM Student s
JOIN StudyGroup g ON s.group_id = g.id
JOIN StudyPlan sp ON sp.faculty_title = g.faculty_title
JOIN Course c ON c.study_plan_id = sp.id
WHERE c.title = 'Math';