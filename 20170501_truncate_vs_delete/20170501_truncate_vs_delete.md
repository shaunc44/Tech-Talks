## What's the difference between TRUNCATE and DELETE in SQL??  

The main difference between the two is space:  
```
1. TRUNCATE deletes all rows AND clears the space where the table was located
2. DELETE only delete rows and does not free space  
```

### When to use TRUNCATE?  

1. Delete all rows, reset row identity and free space containing table  
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


```
+----------------------------------------+----------------------------------------------+
|                Truncate                |                    Delete                    |
+----------------------------------------+----------------------------------------------+
| We can't Rollback after performing     | We can Rollback after delete.                |
| Truncate.                              |                                              |
|                                        |                                              |
| Example:                               | Example:                                     |
| BEGIN TRAN                             | BEGIN TRAN                                   |
| TRUNCATE TABLE tranTest                | DELETE FROM tranTest                         |
| SELECT * FROM tranTest                 | SELECT * FROM tranTest                       |
| ROLLBACK                               | ROLLBACK                                     |
| SELECT * FROM tranTest                 | SELECT * FROM tranTest                       |
+----------------------------------------+----------------------------------------------+
| Truncate reset identity of table.      | Truncate reset identity of table.            |
+----------------------------------------+----------------------------------------------+
| It locks the entire table.             | It locks the table row.                      |
+----------------------------------------+----------------------------------------------+
| Its DDL(Data Definition Language)      | Its DML(Data Manipulation Language)          |
| command.                               | command.                                     |
+----------------------------------------+----------------------------------------------+
| We can't use WHERE clause with it.     | We can use WHERE to filter data to delete.   |
+----------------------------------------+----------------------------------------------+
| Trigger is not fired while truncate.   | Trigger is fired.                            |
+----------------------------------------+----------------------------------------------+
| Syntax :                               | Syntax :                                     |
| 1) TRUNCATE TABLE table_name           | 1) DELETE FROM table_name                    |
|                                        | 2) DELETE FROM table_name WHERE              |
|                                        |    example_column_id IN (1,2,3)              |
+----------------------------------------+----------------------------------------------+
```

*Keep in mind that most SQL statements vary depending on which type SQL you use*  


##### *Sources:*  
<http://beginner-sql-tutorial.com/sql-delete-statement.htm>  
<http://stackoverflow.com/questions/139630/whats-the-difference-between-truncate-and-delete-in-sql>  