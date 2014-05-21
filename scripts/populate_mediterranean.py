import psycopg2

connstring = "dbname='postgres' user='postgres' host='127.0.0.1' password='dbpassword' port='5433'"

try:
    conn = psycopg2.connect(connstring)
except:
	print "couldnt connect to the database you idiot"

cur = conn.cursor()

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Sarahs Grill and Market', 8, 'monday-sunday', 4, '5222 Burnet Rd')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Arpeggio Grill', 8, 'monday-sunday', 3, '6619 Airport Blvd')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('The Mediterranean Chef', 8, 'monday-sunday', 4, '5908 Aurora Dr')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Dimassis Mediterranean Buffet', 8, 'monday-sunday', 3, '12636 Research Blvd')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Pars Mediterranean Deli', 8, 'monday-sunday', 3, '8820 Burnet Rd')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Pharas', 8, 'monday-sunday', 3, '111 E N Loop Blvd')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Zoes Kitchen', 8, 'monday-sunday', 4, '5601 Brodie Ln')");

conn.commit()

cur.execute("SELECT * from migrations_restaurant WHERE type_id = 8 ORDER by derrscore DESC")

rows = cur.fetchall()

for row in rows:
	print " ", row



