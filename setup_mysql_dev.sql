-- check is the database exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- check if the user exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant select previleges 
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- select PRIVILEGES
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- apply changes
FLUSH PRIVILEGES;