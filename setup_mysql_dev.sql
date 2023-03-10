-- prepares a MySQL server for the project

DROP DATABASE IF EXISTS tz_dev_db;
CREATE DATABASE IF NOT EXISTS tz_dev_db;
CREATE USER IF NOT EXISTS 'tz_dev'@'localhost' IDENTIFIED BY 'tz_dev_pwd';
GRANT ALL PRIVILEGES ON `tz_dev_db`.* TO 'tz_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'tz_dev'@'localhost';
FLUSH PRIVILEGES;
