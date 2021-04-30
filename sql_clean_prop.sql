DELETE FROM properties 
WHERE field2 <> 'UPPER WEST SIDE (59-79)';

SELECT DISTINCT field3 FROM properties;

UPDATE properties
SET field3 = 'RESIDENTIAL' 
WHERE 
field3 = '17  CONDO COOPS' OR
field3 LIKE '01%' OR
field3 LIKE '02%' OR 
field3 LIKE '03%' OR 
field3 = '10  COOPS - ELEVATOR APARTMENTS' OR
field3 LIKE '13%' OR
field3 LIKE '09 %' OR 
field3 LIKE '11%' OR
field3 LIKE '07%' OR
field3 LIKE '08%' OR
field3 LIKE '16%' OR
field3 = '10 COOPS - ELEVATOR APARTMENTS' OR
field3 = '17 CONDO COOPS' OR
field3 = '15  CONDOS - 2-10 UNIT RESIDENTIAL' OR
field3 = '14 RENTALS - 4-10 UNIT' OR
field3 LIKE '12%' OR
field3 = '15 CONDOS - 2-10 UNIT RESIDENTIAL' OR
field3 = '14  RENTALS - 4-10 UNIT';

SELECT DISTINCT field3 FROM properties;