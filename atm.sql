create database atm;
use atm;
drop table user_data;

CREATE TABLE user_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    my_name VARCHAR(255) NOT NULL,
    accn  INT NOT NULL,
    de_po INT NOT NULL,
    pass_word VARCHAR(255) NOT NULL
);

SELECT * FROM user_data;




