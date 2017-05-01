## What's the difference between a TRUNCATE and DELETE in SQL??  

*The main difference between the two is space: truncate clears the space where the table was located, whereas delete does not  


### When to use TRUNCATE?  

1. Delete all rows and free space containing table  
```
TRUNCATE TABLE employees;  
```


### When to use DELETE?  

1. Delete specific rows  
```
DELETE FROM employee WHERE id = 100;  
```

2. Delete all rows  
```
DELETE FROM employee;  
```



*####Keep in mind that most SQL statements vary depending on which type SQL you use*  


##### *Sources:*  
<http://beginner-sql-tutorial.com/sql-delete-statement.htm>  
<http://stackoverflow.com/questions/139630/whats-the-difference-between-truncate-and-delete-in-sql>  