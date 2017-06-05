.read fa16data.sql
.read sp17data.sql

CREATE TABLE obedience AS
  select seven, hilfinger FROM students;

CREATE TABLE smallest_int AS
  select time, smallest FROM students WHERE smallest > 16 ORDER By smallest LIMIT 20;

CREATE TABLE greatstudents AS
  select a.date, a.color, a.pet, b.number, a.number
  FROM fa16students as a, students as b
  WHERE a.date = b.date and a.color = b.color and a.pet = b.pet;

CREATE TABLE sevens AS
  select a.seven 
  From students as a, checkboxes as b
  Where a.time = b.time and a.number = 7 and b.'7' = 'True';

CREATE TABLE matchmaker AS
  select a.pet, a.song, a.color, b.color
  From students as a, students as b
  Where a.time < b.time and a.pet = b.pet and a.song = b.song;

