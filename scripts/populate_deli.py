import psycopg2

connstring = "dbname='postgres' user='postgres' host='127.0.0.1' password='dbpassword' port='5433'"

try:
    conn = psycopg2.connect(connstring)
except:
	print "couldnt connect to the database you idiot"

cur = conn.cursor()

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Melvins Deli Comfort', 9, 'monday-sunday', 4, '501 E 53rd St')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Little Deli and Pizzeria', 9, 'monday-sunday', 4, '7101-A Woodrow Ave')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Fricanos Deli', 9, 'monday-sunday', 4, '2405 Nueces St')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('NeWorlDeli', 9, 'monday-sunday', 3, '4101 Guadalupe St')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('NeWorld Cafe', 9, 'monday-sunday', 4, '3742 Far W Blvd')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Gs Dynamite Deli', 9, 'monday-sunday', 3, '2312 S 1st St')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Tam Deli and Cafe', 9, 'monday-sunday', 3, '8222 N Lamar Blvd')");

conn.commit()

cur.execute("SELECT * from migrations_restaurant WHERE type_id = 9 ORDER by derrscore DESC")

rows = cur.fetchall()

for row in rows:
	print " ", row



