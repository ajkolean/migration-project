import psycopg2

connstring = "dbname='postgres' user='postgres' host='127.0.0.1' password='dbpassword' port='5433'"

try:
    conn = psycopg2.connect(connstring)
except:
	print "couldnt connect to the database you idiot"

cur = conn.cursor()

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Fonda San Miguel', 4, 'monday-sunday', 3, '2330 W N Loop Blvd')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Julios cafe', 4, 'monday-sunday', 3, '4230 Duval St')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Curras Grill', 4, 'monday-sunday', 2, '614 E Oltorf St')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Habanero Mexican Cafe', 4, 'monday-sunday', 3, '501 W Oltorf St')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Hecho En Mexico', 4, 'monday-sunday', 3, '6001 William Cannon Dr')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Las Cazuelas', 4, 'monday-sunday', 2, '1701 E Cesar Chavez St')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('La Cocina de Consuelo', 4, 'monday-sunday', 3, '4516 Burnet Rd')");

conn.commit()

cur.execute("SELECT * from migrations_restaurant WHERE type_id = 4 ORDER by derrscore DESC")

rows = cur.fetchall()

for row in rows:
	print " ", row



