-- task 2.1
use shop1;
/*select c.week,c.day,count(*)from SALES1 c group by c.day,c.week order by c.week;*/

-- task2.2
/*set sql_safe_updates=0;
update SALES1 SET SalesPerson='Annette' where SalesPerson='Inga';*/
/*SELECT * FROM SALES1;*/

-- TASK 2.3
/*select count(c.SalesAmount) from SALES1 c where SalesPerson="Annette";*/

-- Task 2.4
/*select c.SalesPerson,c.Day, sum(c.SalesAmount) from SALES1 c group by c.Salesperson, c.Day;*/

-- Task 2.5
/*select c.SalesPerson, sum(c.SalesAmount) from SALES1 c group by c.Salesperson;*/

-- Task 2.6
/*select c.SalesPerson, AVG(c.SalesAmount),MAX(c.SalesAmount), MIN(c.SalesAmount), sum(c.SalesAmount), count(c.SalesAmount) from SALES1 c group by c.Salesperson;*/

-- Task 2.7
/*select c.Store,sum(c.SalesAmount) from SALES1 c group by c.Store;*/

-- Task 2.8
/*select c.SalesPerson,count(*) from SALES1 c  group by c.SalesPerson having count(c.SalesAmount) < 3 ;*/

-- TAsk 2.9
select c.Month, sum(c.SalesAmount) FROM SALES1 c group by c.Month having sum(c.SalesAmount) < 100;