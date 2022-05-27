<h1 align="center"> SysAdmin Part 3 </h1>

The objective of this challenge is to obtain the flag in the system.

---
The password can be in two directories which are `/etc` and `/var`. 
In the `/var/www/` directory, there is a .php file containing connection information to a MySQL database.
```
$mysqlDatabaseName ="arch";
$mysqlUserName ="arch";
$mysqlPassword ="asdftgTst5sdf6309sdsdff9lsdftz";
$mysqlHostName ="127.0.0.1";
$mysqlExportPath ="/var/tmp/ar.sql";
```

We then connect to the database: `$ mysql -u arch -p`. <br>
Then, enter the password. <br>
Display all databases : `$ show databases;`. <br>
A database is called arch. <br>
The `$ use arch` command provides access to this database. <br>
Display the tables : `$ show tables;`. <br>
There are two tables : `arch` and `flag`. 
Display the the flag: `$ select * from flag;`.
