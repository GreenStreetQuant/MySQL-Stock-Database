CREATE TABLE IF NOT EXISTS stocks.symbol (
	
	id INT NOT NULL AUTO_INCREMENT,
   	symbol_id VARCHAR(6) NOT NULL,
    	name VARCHAR(252) NOT NULL,
    	PRIMARY KEY (id),
    	UNIQUE KEY ticker (symbol_id)
	
    );

CREATE TABLE IF NOT EXISTS stocks.daily_price (

	id INT NOT NULL AUTO_INCREMENT,
    	ticker VARCHAR(32) NOT NULL,
    	date DATE NOT NULL,
    	open FLOAT DEFAULT NULL,
    	high FLOAT DEFAULT NULL,
    	low FLOAT DEFAULT NULL,
    	close FLOAT DEFAULT NULL,
    	volume INT DEFAULT NULL,
    	PRIMARY KEY (id)
	
    	);
