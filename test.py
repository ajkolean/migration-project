import psycopg2

connstring = "dbname='postgres' user='postgres' host='127.0.0.1' password='dbpassword' port='5433'"

try:
    conn = psycopg2.connect(connstring)
except:
	print "couldnt connect to the database you idiot"

cur = conn.cursor()

# cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
# VALUES ('Santorini Cafe', 10, 'monday-sunday', 4, '11800 N Lamar Blvd')");
#
# cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
# VALUES ('Athenian Bar and Grill', 10, 'monday-sunday', 3, '600 Congress Ave')");
#
# cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
# VALUES ('Arpeggio Grill', 10, 'monday-sunday', 3, '6619 Airport Blvd')");
#
# cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
# VALUES ('Big Fat Greek Gyros', 10, 'monday-sunday', 4, '74 Rainey St')");
#
# cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
# VALUES ('Zorba Greek Diner', 10, 'monday-sunday', 3, '9600 S I-35')");
#
# cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
# VALUES ('Tinos Greek Cafe', 10, 'monday-sunday', 3, '9901 Brodie Ln')");
#
# cur.execute("INSERT INTO migrations_restaurant (name, type_id, daysopen, derrscore, location) \
# VALUES ('Little Greek', 10, 'monday-sunday', 3, '2422 Ranch Rd 620 S')");
#
# conn.commit()

cur.execute("SELECT * from migrations_restaurant WHERE type = 'american' ORDER by derrscore DESC")

rows = cur.fetchall()

for row in rows:
	print " ", row



