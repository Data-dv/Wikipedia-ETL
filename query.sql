-- Active: 1725452786648@@127.0.0.1@5435@amdariDB
--1
-- list 10 largest universities by enrollment
SELECT "University","Country","Enrollment"
from universities 
ORDER BY "Enrollment" DESC LIMIT 10

--2 number of universities with enrollment less than 50,000
SELECT count("University")
from universities
where "Enrollment" < 50000; 

--3 list countries and unversities with enrollemt greater than 100k
SELECT "Country", "University"
FROM universities
WHERE "Enrollment" > 100000;

-- 4 Number of universities funded privately
SELECT count("University")
FROM universities 
WHERE "Type" LIKE '%Pri%';

-- 5 Number of universities funded publicly
SELECT count("University")
FROM universities 
WHERE "Type" LIKE '%Pub%';

-- 6 list universities created before world war 1
SELECT u."University", u."Country", u."Enrollment"
from universities u 
WHERE "Founded" <= 1914
ORDER BY "Enrollment" DESC LIMIT 5; --(30)

--7 list of universities created after world war 2
SELECT u."University", u."Country", u."Enrollment"
from universities u 
WHERE "Founded" >= 1945
ORDER BY "Enrollment" DESC LIMIT 5; --32

--8 list of universities created between ww1 and ww2
SELECT u."University", u."Country", u."Enrollment"
from universities u 
WHERE "Founded" BETWEEN 1914 AND 1945
ORDER BY "Enrollment" DESC LIMIT 5; --8
