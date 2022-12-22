

                 
from lib2to3.pgen2.token import RIGHTSHIFT


1. %sql SELECT EMP_ID, S.School_NAME, C.Community_Name, B_DATE, SEX, JOB_TITLE, MIN_SALARY, MAX_SALARY
FROM Attendance RIGHTSHIFT JOIN EMPLOYEE WHERE hardship_index > (select AVG(98);


2.select school, school_ID, crime_type, community_name from Canada_school as emp where student_ID IN (select emp from jobs where TITLE= 'Crime');


Exercise 2 #1 

1. CREATE VIEW school_name AS Canada
SELECT school, leaders_icon
FROM school_board


Excerise 3 #1

1.--#SET TERMINATOR @
CREATE PROCEDURE UPDATE_LEADERS_SCORE ( 
    IN LEADERS_SCORE INTEGER, IN School_ID  INTEGER )     -- ( { IN/OUT type } { parameter-name } { data-type }, ... )                          
LANGUAGE SQL                                                
MODIFIES SQL DATA                                           
BEGIN
        DECLARE SQLCODE INTEGER DEFAULT 0;                  
       DECLARE retcode INTEGER DEFAULT 0;                  
        DECLARE CONTINUE HANDLER FOR SQLEXCEPTION           
        SET retcode = SQLCODE;                              
        
        UPDATE LEADERS_SCORE 
        SET Balance = Balance:0;
        WHERE AccountName = 'ID';
        
        UPDATE Schhol_ID
        SET Balance = Balance:0;
        WHERE Accountname = 'ID'
   
        
        IF retcode < 0 THEN                                  --  SQLCODE returns negative value for error, zero for success, positive value for warning
            ROLLBACK WORK;
        
        ELSE
            COMMIT WORK;
        
        END IF;
        
END
@  

Exercise 3 #2

2. UPDATE CHICAGO_PUBLIC_SCHOOLS SET[[Leaders_Score field ]=[School_ID]] WHERE [Leader_Score];


Exercise 3 #3

3.
DELIMITER //
UPDATE SALEPRICE ( 
    IN CHICAGO_PUBLIC_SCHOOLS VARCHAR(5) )     -- ( { IN/OUT type } { parameter-name } { data-type }, ... )

LANGUAGE SQL                                                -- Language used in this routine
MODIFIES SQL DATA                                           -- This routine will only write/modify data in the table

BEGIN 

    IF Leaders_Icon = 'TRUE' THEN                           -- Start of conditional statement
        UPDATE school_ID
        SET School_ID = SALEPRICE + (SALEPRICE + 1)
        WHERE ID = School_ID;
    
    ELSE IF Leaders_Icon = 'NULL' THEN                           
        UPDATE school_ID
        SET School_ID = SALEPRICE - (SALEPRICE - 1)
        WHERE ID = School_ID;
        
    ELSE
        UPDATE Leaders_Icon
        SET School_ID = School_ID
        WHERE ID = School_ID;

    END IF;                                                 -- End of conditional statement
    
END
@  

DELIMITER ;