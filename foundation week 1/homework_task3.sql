-- Task 3.1
USE Parts;
/*SELECT * from SUPPLIER c where c.city<>'London';*/
/*SELECT distinct s.city, s.jname from PROJECT s where s.city<>'London';*/
-- JOIN OF SUPPLIER AND PROJECT TABLES
/*SELECT distinct PROJECT.jname, PROJECT.city, SUPPLIER.city from PROJECT INNER JOIN SUPPLIER ON PROJECT.city=SUPPLIER.city;*/
/*SELECT  distinct s.jname, s.city from PROJECT s where s.city= ANY(SELECT c.city from SUPPLIER c where c.city<>'London');*/

-- TASK 3.2
-- JOIN SUPPLIER, PROJECT AND PART TAbles
SELECT distinct PROJECT.jname, PART.PNAME, SUPPLIER.SNAME, PROJECT.city,SUPPLIER.city,PART.city 
from ((PROJECT INNER JOIN SUPPLIER ON PROJECT.city=SUPPLIER.city) INNER JOIN PART ON PROJECT.city=PART.city);
