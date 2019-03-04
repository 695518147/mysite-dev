use mysql;
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'rootroot';
# update user set host = '%' where user = 'root';

CREATE DATABASE IF NOT EXISTS mysite  DEFAULT CHARSET utf8 COLLATE utf8_general_ci;

