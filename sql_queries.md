## Get rows from a table
SELECT * FROM {table_name};
SELECT * FROM products;
SELECT roll_number, first_name from students;


## Filter rows according to a specific field/column

SELECT * FROM {table_name} WHERE {field_name}={value}
SELECT * FROM students WHERE roll_number=14457
SELECT * FROM students WHERE roll_number=14457 AND first_name="Shahzaib"
SELECT * FROM students WHERE roll_number=14457 AND first_name="Shahzaib" ORDER BY roll_number
SELECT * FROM students WHERE roll_number=14457 AND first_name="Shahzaib" ORDER BY roll_number, first_name
SELECT * FROM students WHERE marks>=550 OR roll_number>45
