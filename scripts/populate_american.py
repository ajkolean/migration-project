import psycopg2

connstring = "dbname='postgres' user='postgres' host='127.0.0.1' password='dbpassword' port='5433'"

try:
    conn = psycopg2.connect(connstring)
except:
	print "couldnt connect to the database you idiot"

cur = conn.cursor()

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Trace', 5, 'monday-sunday', 2, '200 Lavaca st')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Eastside Cafe', 5, 'monday-sunday', 3, '2113 Manor Rd')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Barley Swine', 5, 'monday-sunday', 4, '2024 S Lamar Blvd')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Odd Duck', 5, 'monday-sunday', 3, '1201 S Lamar Blvd')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Wink', 5, 'monday-sunday', 3, '1014 N Lamar Blvd')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Apothecary', 5, 'monday-sunday', 3, '4800 Burnet Rd')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Galaxy Cafe', 5, 'monday-sunday', 2, '4616 Triangle Ave')");

conn.commit()

cur.execute("SELECT * from migrations_restaurant WHERE type_id = 5 ORDER by derrscore DESC")

rows = cur.fetchall()

for row in rows:
	print " ", row



