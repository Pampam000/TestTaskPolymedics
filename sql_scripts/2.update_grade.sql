-- Updating student grade if student_id and course id are known
UPDATE StudentExamGrade
SET grade_value = 4
WHERE student_id = 2 AND exam_id IN
      (SELECT id FROM Exam WHERE course_id = 2);