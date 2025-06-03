-- Display student by Student_name, gpa, School_lunch
select student_name,gpa,school_lunch
from students;


-- Show Student who get School_lunch (where)
select student_name,gpa,school_lunch
from students
Where school_lunch="Yes" and gpa>3.3;


-- Sort student by gpa (Order_by) by desc order
select student_name,gpa,school_lunch
from students
Where school_lunch="Yes" and gpa>3.3
Order BY gpa DESC;

-- Show the average gpa for each grade level (Group by)
Select grade_level, avg(gpa)
from students
Group by(grade_level)
order by(grade_level);

-- show the grade_level who's gpa is below 3.3
Select grade_level, avg(gpa) as avg_gps
from students
Group by(grade_level)
having avg_gps<3.3
order by(grade_level);

-- Displaying limited number of rows
select student_name,gpa,school_lunch
from students
limit 5;

-- Number of rows satsifiy the condition COUNT of the value
select COUNT(*) -- student_name,gpa,school_lunch
from students
Where school_lunch="Yes" and gpa>3.3;


-- Removing the Duplicates 
select distinct(gpa)
from students
Order BY gpa DESC;


-- Displaying student_grade table
select *
from student_grades;


-- Combined the information using left join
select students.id , students.student_name,
		student_grades.class_name, student_grades.final_grade
from students Left join student_grades
	on students.id=student_grades.student_id;