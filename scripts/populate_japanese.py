import psycopg2

connstring = "dbname='postgres' user='postgres' host='127.0.0.1' password='dbpassword' port='5433'"

try:
    conn = psycopg2.connect(connstring)
except:
	print "couldnt connect to the database you idiot"

cur = conn.cursor()

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Lucky Robot', 7, 'monday-sunday', 3, '1303 S Congress')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Kome', 7, 'monday-sunday', 3, '4917 Aiport Blvd')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Ryu of Japan', 7, 'monday-sunday', 2, '11101 Burnet Rd')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Love Balls', 7, 'monday-sunday', 3, '2908 Fruth St')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Lavaca Teppan', 7, 'monday-sunday', 3, '1712 Lavaca St')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Uchi', 7, 'monday-sunday', 4, '801 S Lamar Blvd')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Uchiko', 7, 'monday-sunday', 4, '4200 N Lamar Blvd')");

conn.commit()

cur.execute("SELECT * from migrations_restaurant WHERE type_id = 7 ORDER by derrscore DESC")

rows = cur.fetchall()

for row in rows:
	print " ", row



