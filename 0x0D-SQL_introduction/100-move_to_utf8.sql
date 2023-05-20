-- converts hbtn_0c_0 database to UTF8
ALTER DATABASE hbtn_0c_0
	CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- convert the table first_table to UTF8
ALTER TABLE hbtn_0c_0.first_table
	CONVERT TO CHARACTER SET utf8mb4
	COLLATE utf8mb4_unicode_ci;
-- convert the field name in first_table to UTF8
ALTER TABLE hbtn_0c_0.first_table
	MODIFY name varchar(256)
	COLLATE utf8mb4_unicode_ci;
