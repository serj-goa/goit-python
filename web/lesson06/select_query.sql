-- 1. Найти 5 студентов с наибольшим средним баллом по всем предметам.
select s.fullname, round(avg(g.grade), 2) as average_grade
from grades g
join students s on s.id = g.student_id
group by s.fullname
order by average_grade desc
LIMIT 5;

-- 2. Найти студента с наивысшим средним баллом по определенному предмету.
select d.name, s.fullname, round(avg(g.grade), 2) as average_grade
from grades g
join students s on s.id = g.student_id
join disciplines d on d.id = g.discipline_id
where d.id = 8
group by s.fullname
order by average_grade desc
LIMIT 1;

-- 3. Найти средний балл в группах по определенному предмету.
select d.name, gr.name, round(avg(g.grade), 2) as average_grade
from grades g
join students s on s.id = g.student_id
join disciplines d on d.id = g.discipline_id
join [groups] gr ON gr.id = s.group_id
where d.id = 1
group by gr.name, d.name
order by average_grade desc;

-- 4. Найти средний балл на потоке (по всей таблице оценок).
select d.name, gr.name, round(avg(g.grade), 2) as average_grade
from grades g
join students s on s.id = g.student_id
join disciplines d on d.id = g.discipline_id
join [groups] gr ON gr.id = s.group_id
group by gr.name, d.name
order by average_grade desc;

-- 5. Найти какие курсы читает определенный преподаватель.
select t.fullname, d.name
from disciplines d
join teachers t on t.id = d.teacher_id
where t.id = 2
order by d.name asc

-- 6. Найти список студентов в определенной группе.
select s.fullname, gr.name
from grades g
join students s on g.student_id = s.id
join groups gr on s.group_id = gr.id
where gr.id = 1

-- 7. Найти оценки студентов в отдельной группе по определенному предмету.
select s.fullname, gr.name, d.name, g.grade
from grades g
join disciplines d  on g.discipline_id = d.id
join students s on g.student_id = s.id
join groups gr on s.group_id = gr.id
where gr.id = 1 and  d.id = 7

-- 8. Найти средний балл, который ставит определенный преподаватель по своим предметам.
select t.fullname, round(avg(g.grade), 2) as avg_grade, d.name
from grades g
join disciplines d  on g.discipline_id = d.id
join teachers t on d.teacher_id = t.id
where t.id = 1
group by d.id
order by avg_grade desc

-- 9. Найти список курсов, которые посещает определенный студент.
select s.fullname, d.name
from grades g
join disciplines d  on g.discipline_id = d.id
join students s on g.student_id = s.id
where s.id = 12
group by d.id

-- 10. Список курсов, которые определенному студенту читает определенный преподаватель.
select s.fullname as student, d.name, t.fullname as teacher
from grades g
join disciplines d on g.discipline_id  = d.id
join students s on g.student_id = s.id
join teachers t on d.teacher_id = t.id
where s.id = 30 and t.id = 2
group by d.id

select s.fullname as stdent, round( avg(g.grade), 2) as average, t.fullname as teacher
from grades g
join disciplines d  on g.discipline_id = d.id
join students s on g.student_id = s.id
join teachers t on d.teacher_id = t.id
where s.id = 12 and t.id = 2
order by average desc

select s.fullname, gr.name, g.grade, g.date_of
from grades g
join students s on g.student_id = s.id
join groups gr on s.group_id = gr.id
join disciplines d on g.discipline_id = d.id
where gr.id = 1 and d.id = 8 and g.date_of =
(
	select max(g.date_of)
	from grades g
	join disciplines d2  on g.discipline_id = d2.id
	join students s on s.id = g.student_id
	join [groups] gr ON gr.id = s.group_id
	WHERE gr.id = 1 AND d2.id = 8
	)
ORDER by s.fullname ASC;
