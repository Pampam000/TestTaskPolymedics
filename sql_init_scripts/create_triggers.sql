-- Create default value for Semester.end_date
CREATE OR REPLACE FUNCTION set_end_date()
RETURNS TRIGGER AS $$
BEGIN
  IF NEW.end_date IS NULL THEN
  NEW.end_date = NEW.start_date + INTERVAL '5 months';
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_end_date_trigger
BEFORE INSERT OR UPDATE ON Semester
FOR EACH ROW
EXECUTE FUNCTION set_end_date();

-- Create default value for Exam.end_timestamp
CREATE OR REPLACE FUNCTION set_end_timestamp()
RETURNS TRIGGER AS $$
BEGIN
  IF NEW.end_timestamp IS NULL THEN
  NEW.end_timestamp = NEW.start_timestamp + INTERVAL '2 hours';
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_end_timestamp_trigger
BEFORE INSERT OR UPDATE ON Exam
FOR EACH ROW
EXECUTE FUNCTION set_end_timestamp();

-- Create default value for Lesson.end_time
CREATE OR REPLACE FUNCTION set_end_time()
RETURNS TRIGGER AS $$
BEGIN
  IF NEW.end_date IS NULL THEN
  NEW.end_time = NEW.start_time + INTERVAL '90 minutes';
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_end_time_trigger
BEFORE INSERT OR UPDATE ON Lesson
FOR EACH ROW
EXECUTE FUNCTION set_end_time();

-- Auto-complete student exam grade while creating exam
CREATE FUNCTION insert_student_exam_grade() RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO StudentExamGrade(student_id, exam_id)
    SELECT s.id, NEW.id
    FROM Student s
    WHERE NEW.group_id = s.group_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER insert_student_exam_grade_trigger
AFTER INSERT ON exam
FOR EACH ROW
EXECUTE FUNCTION insert_student_exam_grade();

-- Updating table StudentExamGrade while updating student.group_id
CREATE OR REPLACE FUNCTION update_student_group()
RETURNS TRIGGER AS $$
BEGIN
  IF NEW.group_id != OLD.group_id THEN
    DELETE FROM StudentExamGrade WHERE student_id = OLD.id;
    INSERT INTO StudentExamGrade (student_id, exam_id)
    SELECT NEW.id, Exam.id
    FROM Exam
    WHERE Exam.group_id = NEW.group_id;
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_student_group_trigger
AFTER UPDATE OF group_id ON Student
FOR EACH ROW
EXECUTE FUNCTION update_student_group();