## What is the "Gang of Four" book?  


### *Design Patterns: Elements of Reusable Object-Oriented Software*  
	i.   Erich Gamma  
	ii.  Richard Helm  
	iii. Ralph Johnson  
	iv.  John Vlissides  

#### 2. Inefficient data replication  
	i.  creates bandwith issues when replicated to multiple data centers  

#### 3. Issues with table corruption  
	i.  replicas create misapplied records (active records that should be inactive)  
	ii. queries then return active and inactive records  

#### 4. Poor replica MVCC support  
	i.  mvcc is a method used to handle data consistency when multiple processess are using the same table  
	ii. PostgreSQL doesn't have true MVCC support  

#### 5. Difficulty upgrading to newer releases  
	i.  very difficult and time consuming to replicate data after an upgrade


### *MySQL Advantages*  

#### 1. Replication  
	i.  support different replication modes  
	ii. easier to do logical replication with MySQL  

#### 2. Buffer Pool (caching)  
	i.  customizable design  
	ii. fewer context switches  

#### 3. Connection Handling  
	i.  MySQL implements concurrent connections by spawning a thread-per-connection. This is relatively low overhead  


##### *Sources:*  
<https://en.wikipedia.org/wiki/Design_Patterns>  