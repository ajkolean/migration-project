import psycopg2

connstring = "dbname='postgres' user='postgres' host='127.0.0.1' password='dbpassword' port='5433'"

try:
    conn = psycopg2.connect(connstring)
except:
	print "couldnt connect to the database you idiot"

cur = conn.cursor()

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Maryes Gourmet Pizza', 1, 'monday-sunday', 4, '3663 Bee Cave Rd')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Patrizis', 1, 'monday-sunday', 3, '2307 Manor Rd')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Mandolas Italian Market', 1, 'monday-sunday', 2, '4700 W Guadalupe St')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Milano Cafe', 1, 'monday-sunday', 3, '4601 Southwest Pkwy')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Andiamo Ristorante', 1, 'monday-sunday', 3, '2521 Rutland Dr')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('La Travista', 1, 'monday-sunday', 3, '314 Congress Ave')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Reales Pizza and Cafe', 1, 'monday-sunday', 3, '13450 N Hwy 183')");

conn.commit()

cur.execute("SELECT * from migrations_restaurant WHERE type_id = 1 ORDER by derrscore DESC")

rows = cur.fetchall()

for row in rows:
	print " ", row



