--  lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).
CREATE IF NOT EXISTS DATABASE hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhots';
GRANT SELECT PRIVILEGE ON 'hbtn_0d_2' to 'user_0d_2'@'localhots';2 