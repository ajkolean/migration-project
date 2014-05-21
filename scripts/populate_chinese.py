import psycopg2

connstring = "dbname='postgres' user='postgres' host='127.0.0.1' password='dbpassword' port='5433'"

try:
    conn = psycopg2.connect(connstring)
except:
	print "couldnt connect to the database you idiot"

cur = conn.cursor()

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Chicken lollypop', 6, 'monday-sunday', 4, '1005 E Braker Ln')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Asia Cafe', 6, 'monday-sunday', 3, '8650 Spicewood Springs Rd')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('888 Pan Asian Restaurant', 6, 'monday-sunday', 3, '2400 E Oltorf St')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Ho Ho Chinese BBQ', 6, 'monday-sunday', 3, '13000 N IH-35')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Chens Noodle House', 6, 'monday-sunday', 3, '8650 Spicewood Springs Rd')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('First Wok', 6, 'monday-sunday', 3, '603 W Stassney Ln')");

cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
VALUES ('Din Ho Chinese BBQ', 6, 'monday-sunday', 3, '8557 Research Blvd')");

conn.commit()

cur.execute("SELECT * from migrations_restaurant WHERE type_id = 6 ORDER by derrscore DESC")

rows = cur.fetchall()

for row in rows:
	print " ", row



