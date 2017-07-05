#!/home/ubuntu/.env/bin/python
# -*- coding: utf-8 -*-

import sys
import MySQLdb
import MySQLdb.cursors

try:
    r_conn = MySQLdb.connect(host='127.0.0.1',
                            user='root',
                            passwd='root1234',
                            charset='utf8')
except:
    print("Can't Connect Database via root: ", sys.exc_info()[0])
    sys.exit()

# drop db and user if exist
r_cursor = r_conn.cursor()

# create user and db, and grant privileges
r_cursor.execute("CREATE USER 'demouser'@'localhost' IDENTIFIED BY 'demo1234'")
r_cursor.execute("CREATE DATABASE demo CHARACTER SET UTF8")
r_cursor.execute("GRANT ALL PRIVILEGES ON demo.* to 'demouser'@'localhost'")
r_cursor.execute("FLUSH PRIVILEGES")
r_cursor.close()
r_conn.close()

# connect demo db
try:
    conn = MySQLdb.connect(host='127.0.0.1',
                            user='demouser',
                            passwd='demo1234',
                            db='demo',
                            charset='utf8')
except:
    print("Can't Connect Database via demouser: ", sys.exc_info()[0])
    sys.exit()

# create schema
cursor = conn.cursor()
# cursor.execute("DROP TABLE if EXISTS a136")
cursor.execute("USE demo")
cursor.execute("""CREATE TABLE a136 (
                pk INT(12) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                name CHAR(10) NOT NULL,
                sid CHAR(5) NOT NULL,
                t_10m FLOAT(6,1) DEFAULT NULL,
                t_1h FLOAT(6,1) DEFAULT NULL,
                t_3h FLOAT(6,1) DEFAULT NULL,
                t_6h FLOAT(6,1) DEFAULT NULL,
                t_12h FLOAT(6,1) DEFAULT NULL,
                t_24h FLOAT(6,1) DEFAULT NULL,
                t_today FLOAT(6,1) DEFAULT NULL,
                t_yday FLOAT(6,1) DEFAULT NULL,
                t_2d FLOAT(6,1) DEFAULT NULL,
                update_time DATETIME NOT NULL
                ) ENGINE=InnoDB""")
cursor.close()
conn.close()

