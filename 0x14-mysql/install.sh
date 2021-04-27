#!/usr/bin/env bash
# install mysql 5.7
sudo apt-get install mysql-server-5.7
mysql -hlocalhost -uroot -p
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE nexus6;

CREATE TABLE nexus6(id INT AUTO_INCREMENT, PRIMARY KEY (id), name VARCHAR(100));

INSERT INTO nexus6 (name) values ('Leon');
DROP TABLE tablename;
USE tyrell_corp;
select * from nexus6;
GRANT type_of_permission ON database_name.table_name TO 'username'@'localhost';
GRANT ALL PRIVILEGES ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';

CREATE USER 'replica_user'@'localhost' IDENTIFIED BY 'password';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%' IDENTIFIED BY 'password';
SELECT user, Repl_slave_priv FROM mysql.user

**
DROP USER 'replica_user'@'localhost';

GRANT ALL PRIVILEGES ON * . * TO 'holberton_user'@'localhost';

mysqldump -u root -p --opt tyrell_corp > newdatabase.sql
scp newdatabase.sql ubuntu@54.209.19.247:

CHANGE MASTER TO MASTER_HOST='35.231.210.244',MASTER_USER='replica_user', MASTER_PASSWORD='password', MASTER_LOG_FILE='mysql-bin.000001', MASTER_LOG_POS=  107;
CHANGE MASTER TO MASTER_HOST='35.231.210.244',MASTER_USER='replica_user', MASTER_PASSWORD='password', MASTER_LOG_FILE='mysql-bin.000003', MASTER_LOG_POS=  597;
SELECT user, Repl_slave_priv FROM mysql.user
SHOW MASTER STATUS\G

On MASTER
*************************** 1. row ***************************
             File: mysql-bin.000001
         Position: 712
     Binlog_Do_DB: tyrell_corp
 Binlog_Ignore_DB: 
Executed_Gtid_Set: 
1 row in set (0.00 sec)

select host, user from mysql.user;

ufw allow 3306
mysql -u replica -h 35.231.210.244 -p