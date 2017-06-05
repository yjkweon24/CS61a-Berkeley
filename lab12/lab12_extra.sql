.read lab12.sql

CREATE TABLE fa16favnum AS
  select number, COUNT(*) As count From fa16students
  Group by number Order by count desc Limit 1;


CREATE TABLE fa16favpets AS
  select pet, Count(*) As count From fa16students
  Group by pet Order by count desc Limit 10;


CREATE TABLE sp17favpets AS
  select pet, Count(*) As count From students
  Group by pet Order by count desc Limit 10;
  ;


CREATE TABLE sp17dragon AS
  select pet, Count(*) As count From students
  Where pet = "dragon" Group by pet Order by count desc Limit 1;


CREATE TABLE sp17alldragons AS
  select pet, Count(*) As count From students
  Where pet Like "%dragon%" Order by count desc Limit 1;


CREATE TABLE obedienceimage AS
  select seven, hilfinger, Count(*) As count From students
  Where seven = "7" Group by hilfinger Order by hilfinger;

CREATE TABLE smallest_int_count AS
  select smallest, Count(*) As count From students
  Group by smallest Order by smallest;
