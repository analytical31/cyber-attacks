create database cybersecurity_DB;
use cybersecurity_db;

CREATE TABLE security_logs
(
log_id INT PRIMARY KEY,
user_id INT,
user_name VARCHAR(50),
country VARCHAR(50),
ip_address VARCHAR(50),
login_time DATETIME,
status VARCHAR(20)
);



select * from security_logs;  

select * from security_logs
where status= "Failed";

select country,
count(*) as failed_attempts from security_logs
where status= "Failed"
group by country;

