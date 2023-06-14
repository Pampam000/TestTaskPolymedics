INSERT INTO Semester (start_date) VALUES ('2023-01-15');

INSERT INTO Building (number) VALUES (1), (2), (3);

INSERT INTO Classroom (number, building_number)
VALUES (102, 1), (103, 1), (104, 2), (105, 2), (104, 3), (105, 3);

INSERT INTO Department (title) VALUES ('full-time'), ('correspondence');

INSERT INTO Grade (value_) VALUES (2), (3), (4), (5);

INSERT INTO Faculty (title) VALUES ('juridical'), ('technical');

-- Creating 4 teachers. There are 2 of them who located in building 3.
INSERT INTO Teacher (name, birthdate, classroom_id)
VALUES ('Петров П.П.', '1970-01-01', 5), ('Иванов И.И.', '1970-01-01', 6),
('Андреев А.А.', '1970-01-01', 1), ('Васильев В.В.', '1970-01-01', 3);

INSERT INTO StudyGroup (title, department_title, faculty_title) VALUES
('Group1', 'full-time', 'technical'), ('Group2', 'full-time', 'technical'),
('Group3', 'full-time', 'juridical'), ('Group4', 'correspondence', 'juridical');


INSERT INTO Student (name, birthdate, group_id) VALUES
 ('St1', '2003-01-01', 1), ('St2', '2003-01-01', 1), ('St3', '2003-01-01', 1),
 ('St4', '2003-01-01', 2), ('St5', '2003-01-01', 2), ('St6', '2003-01-01', 2),
 ('St7', '2003-01-01', 3), ('St8', '2003-01-01', 3), ('St9', '2003-01-01', 3),
 ('St10', '2003-01-01', 4), ('St11', '2003-01-01', 4), ('St12', '2003-01-01', 4);


INSERT INTO StudyPlan (faculty_title, semester_id) VALUES
('technical', 1), ('juridical', 1);

-- Creating 2 courses for each study plan
INSERT INTO Course (title, duration_in_hours, teacher_id, study_plan_id)
VALUES ('Math', 100, 1, 1), ('Programming', 100, 3, 1),
('Jurisprudence', 100, 1, 2), ('History', 100, 2, 2);

INSERT INTO CourseProgram (description, course_id) VALUES
('A', 1), ('B', 2), ('C', 3), ('D', 4);

-- Creating exams for each course and for each group
INSERT INTO Exam (course_id, group_id, start_timestamp) VALUES
(1, 1, '2023-06-10 12:30:00'), (1, 2, '2023-06-10 14:30:00'),
(2, 1, '2023-07-10 12:30:00'), (2, 2, '2023-07-10 14:30:00'),
(3, 3, '2023-06-10 12:30:00'), (3, 4, '2023-06-10 14:30:00'),
(4, 3, '2023-07-12 12:30:00'), (4, 4, '2023-07-12 14:30:00');

-- Creating 3 tasks where 2 of them are old
INSERT INTO Task (course_id, description, created_at) VALUES
(1, 'Task1', '2020-01-01'), (1, 'Task2', '2020-01-01'),
(2, 'Task1', '2023-01-01')
