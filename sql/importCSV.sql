LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/caso.csv' 
INTO TABLE casofullcovid 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;