-- Relations:
--      StudyPlan - 1:M
CREATE TABLE IF NOT EXISTS Semester (
  id BIGSERIAL PRIMARY KEY,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  CHECK(end_date > start_date)
);

-- Relations:
--      Classroom - 1:M
CREATE TABLE IF NOT EXISTS Building (
  number INT PRIMARY KEY
);

--Relations:
--      Building - M:1
--      Teacher - 1:1
--      Exam - 1:1
--      Lesson - 1:M
CREATE TABLE IF NOT EXISTS Classroom (
  id BIGSERIAL PRIMARY KEY,
  number INT,
  building_number INT NOT NULL,
  UNIQUE(building_number, number),
  FOREIGN KEY (building_number) REFERENCES Building(number)
);

-- Relations:
--      StudyGroup - 1:M
CREATE TABLE IF NOT EXISTS Department (
  title VARCHAR(50) PRIMARY KEY
);

-- Relations:
--      StudyGroup - 1:M
--      StudyPlan - 1:M
CREATE TABLE IF NOT EXISTS Faculty (
  title VARCHAR(50) PRIMARY KEY
);

-- Relations:
--      StudentExamGrade - 1:M
--      StudentTaskGrade - 1:M
CREATE TABLE IF NOT EXISTS Grade (
    value_ INT PRIMARY KEY
);

-- Relations:
--      Classroom - 1:1 (Classroom number could be null)
--      Course - 1:M
--      Lesson - 1:M
CREATE TABLE IF NOT EXISTS Teacher (
  id BIGSERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  birthdate DATE NOT NULL,
  classroom_id INT UNIQUE,
  is_employee BOOLEAN NOT NULL DEFAULT TRUE,
  FOREIGN KEY (classroom_id) REFERENCES Classroom(id)
  ON DELETE SET NULL
);

-- Relations:
--      Faculty - M:1
--      Department - M:1
--      Student - 1:M
--      LessonGroup - 1:M
CREATE TABLE IF NOT EXISTS StudyGroup (
  id BIGSERIAL PRIMARY KEY,
  title VARCHAR(50) NOT NULL,
  department_title VARCHAR(50) NOT NULL,
  faculty_title VARCHAR(50) NOT NULL,
  FOREIGN KEY (department_title) REFERENCES Department(title),
  FOREIGN KEY (faculty_title) REFERENCES Faculty(title)
);

-- Relations:
--      StudyGroup - M:1
--      StudentExamGrade - 1:M
--      StudentTaskGrade - 1:M
CREATE TABLE IF NOT EXISTS Student(
  id BIGSERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  birthdate DATE NOT NULL,
  group_id INT NOT NULL,
  is_graduated BOOLEAN NOT NULL DEFAULT False,
  is_expelled BOOLEAN NOT NULL DEFAULT False,
  FOREIGN KEY (group_id) REFERENCES StudyGroup(id)
);


-- Relations:
--      Semester - M:1
--      Faculty - M:1
CREATE TABLE IF NOT EXISTS StudyPlan (
  id BIGSERIAL PRIMARY KEY,
  faculty_title VARCHAR(50),
  semester_id INT NOT NULL,
  FOREIGN KEY (faculty_title) REFERENCES Faculty(title),
  FOREIGN KEY (semester_id) REFERENCES Semester(id)
);

-- Relations:
--      CourseProgram - 1:1
--      Teacher - M:1
--      Exam - 1:1
--      Task - 1:M
--      Lesson - 1:M
--      StudyPlan - M:1 (study_plan_id could be null -
--                       means course is not include in any study plan yet)
CREATE TABLE IF NOT EXISTS Course (
  id BIGSERIAL PRIMARY KEY,
  title VARCHAR(50) NOT NULL,
  duration_in_hours INT NOT NULL,
  teacher_id INT NOT NULL,
  study_plan_id INT,
  FOREIGN KEY (teacher_id) REFERENCES Teacher(id),
  FOREIGN KEY (study_plan_id) REFERENCES StudyPlan(id)
);

-- Relations:
--      Course - 1:1
CREATE TABLE IF NOT EXISTS CourseProgram (
  id BIGSERIAL PRIMARY KEY,
  description TEXT NOT NULL,
  course_id INT NOT NULL UNIQUE,
  FOREIGN KEY (course_id) REFERENCES Course(id)
  ON DELETE CASCADE
);

-- Relations:
--      Course - 1:1
--      Classroom - M:1
--      StudyGroup - M:1
CREATE TABLE IF NOT EXISTS Exam (
  id BIGSERIAL PRIMARY KEY,
  course_id INT NOT NULL,
  group_id INT NOT NULL,
  start_timestamp TIMESTAMP NOT NULL,
  end_timestamp TIMESTAMP NOT NULL,
  classroom_id INT,
  FOREIGN KEY (course_id) REFERENCES Course(id),
  FOREIGN KEY (classroom_id) REFERENCES Classroom(id)
  ON DELETE SET NULL,
  FOREIGN KEY (group_id) REFERENCES StudyGroup(id),
  UNIQUE (group_id, start_timestamp),
  CHECK (end_timestamp > start_timestamp)
);

-- Relations:
--      Course - M:1
--      StudentTaskGrade - 1:M
CREATE TABLE IF NOT EXISTS Task (
  id BIGSERIAL PRIMARY KEY,
  title VARCHAR(50),
  course_id INT NOT NULL,
  description TEXT NOT NULL,
  created_at DATE NOT NUll DEFAULT CURRENT_DATE,
  FOREIGN KEY (course_id) REFERENCES Course(id)
);

-- Relations:
--      Students - M:1
--      Grade - M:1
--      Exam - M:1
CREATE TABLE IF NOT EXISTS StudentExamGrade (
  id BIGSERIAL PRIMARY KEY,
  student_id INT NOT NULL,
  exam_id INT NOT NULL,
  grade_value INT DEFAULT NULL,
  FOREIGN KEY (student_id) REFERENCES Student(id)
  ON DELETE CASCADE,
  FOREIGN KEY (exam_id) REFERENCES Exam(id)
  ON DELETE CASCADE,
  FOREIGN KEY (grade_value) REFERENCES Grade(value_),
  UNIQUE (student_id, exam_id)
);

-- Relations:
--      Students - M:1
--      Grade - M:1
--      Task - M:1
CREATE TABLE IF NOT EXISTS StudentTaskGrade (
  id BIGSERIAL PRIMARY KEY,
  student_id INT NOT NULL,
  task_id INT NOT NULL,
  grade_value INT NOT NULL,
  FOREIGN KEY (student_id) REFERENCES Student(id)
  ON DELETE CASCADE,
  FOREIGN KEY (task_id) REFERENCES Task(id)
  ON DELETE CASCADE,
  FOREIGN KEY (grade_value) REFERENCES Grade(value_),
  UNIQUE (student_id, task_id)
);

-- Relations:
--      Lesson - 1:M
CREATE TABLE IF NOT EXISTS Day_ (
    value_ VARCHAR(10) PRIMARY KEY
);

-- Relations:
--      Lesson - 1:M
CREATE TABLE IF NOT EXISTS StartLessonTime (
  value_ TIME PRIMARY KEY
);

-- Relations:
--      StartLessonTime - 1:1
--      Day_ - 1:1
--      Teacher - M:M
--      Course - M:M
--      Croup - M:M
CREATE TABLE IF NOT EXISTS Lesson (
  number INT NOT NULL,
  day_value VARCHAR(10) NOT NULL,
  start_time TIME NOT NULL,
  end_time TIME NOT NULL,
  classroom_id INT NOT NULL,
  course_id INT NOT NULL,
  teacher_id INT NOT NULL,
  group_id INT NOT NULL,
  FOREIGN KEY (course_id) REFERENCES Course(id),
  FOREIGN KEY (teacher_id) REFERENCES Teacher(id),
  FOREIGN KEY (group_id) REFERENCES StudyGroup(id),
  FOREIGN KEY (classroom_id) REFERENCES Classroom(id),
  UNIQUE (day_value, start_time, classroom_id),
  CHECK (end_time > start_time)
);
