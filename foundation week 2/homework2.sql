

-- TASK1.1
/*CREATE DATABASE GAME;*/
/*USE GAME;*/
/*
CREATE TABLE PLAYER (
	ID VARCHAR(2),
	FNAME VARCHAR(10),
    LNAME VARCHAR(20),
    CLASS VARCHAR(10),
    POSITION VARCHAR(10),
	SSN VARCHAR(4)
);*/


/*INSERT INTO PLAYER
(ID,FNAME,LNAME,CLASS,POSITION,SSN)
VALUES 
('1', 'TEEMO', 'SHROOMER', 'SPECIALIST','TOP','2345'),
('2', 'CECIL', 'HEIDI','SPECIALIST','MID','5461'),
('3', 'ANNIE', 'HASTUR','MAGE','MID','8784'),
('4', 'FIORA', 'LAURENT','SLAYER','TOP','7867'),
('5', 'GAREN', 'CROWN','FIGHTER','TOP','4579'),
('6', 'MALCOLM', 'GRAVES','SPECIALIST','ADC','4578'),
('7', 'IRELIA', 'LITO','FIGHTER','TOP','5689'),
('8', 'HANITRA', 'RAKOT','SLAYER','TOP','6666')*/
;
/*SELECT * FROM PLAYERS;*/
/*SELECT * FROM PLAYER WHERE FNAME = 'TEEMO';*/
/*CREATE INDEX index_FNAME ON PLAYERS(FNAME);*/
/*SELECT * FROM PLAYER WHERE FNAME = 'TEEMO';*/
/*SELECT * FROM PLAYER WHERE CLASS='SPECIALIST' AND POSITION='MID';*/

/*CREATE INDEX class_pos_index ON PLAYER (SPECIALIST, POSITION);*/
/*SELECT * FROM PLAYER WHERE CLASS='SPECIALIST' AND POSITION='MID';*/

-- task 1.2
/*USE Bakery;

CREATE INDEX index_price ON Sweet(price);
SELECT distinct item_name from Sweet where price <= 0.50;*/

-- Task 1.3
use bank;
/*select * from accounts;*/
SELECT account_holder_name from accounts where balance<=0 AND overdraft_allowed=1;
/*CREATE INDEX index_overdraf_balance ON accounts(balance,overdraft_allowed);*/