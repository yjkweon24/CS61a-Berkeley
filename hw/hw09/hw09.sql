create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
  select name, size from dogs, sizes where height > min and height <= max;
  
-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
  select child from dogs, parents where dogs.name = parents.parent Order by height desc;


-- Sentences about siblings that are the same size
create table sentences as
  with siblingspair(sib1, sib2) as ( --sib1 = a.child, sib2 = b.child
    	select a.child, b.child from parents as a, parents as b 
    	where a.child < b.child and a.parent = b.parent  -- appear only once in alphabetical order.
    ), -- parens should be the same.
  sizess(name1, name2, size) as (
  	select a.sib1, a.sib2, c.size  from size_of_dogs as c, size_of_dogs as d, siblingspair as a
  	where c.size = d.size and a.sib1 = c.name and a.sib2 = d.name
  	)
  select name1 || " and " || name2 || " are " || size || " siblings" from sizess;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
create table stacks as
  with
    pairs(name1, name2, name3, name4, totalheight) as (
      select a.name, b.name, c.name, d.name, a.height + b.height + c.height + d.height
      from dogs as a, dogs as b, dogs as c, dogs as d
      where a.height < b.height and b.height < c.height and c.height < d.height
    )
  select name1 || ', ' || name2 || ', ' || name3 || ', ' || name4, totalheight
  from pairs where totalheight >= 170 order by totalheight;

-- non_parents is an optional, but recommended question
-- All non-parent relations ordered by height difference
--create table non_parents as
--  select ;

create table ints as
    with i(n) as (
        select 1 union
        select n+1 from i limit 100
    )
    select n from i;

create table divisors as
    select a.n as number, count(*) as count from ints as a, ints as b 
    where number % b.n = 0 group by a.n;

create table primes as
    select number from divisors where count = 2;






