import psycopg2

connstring = "dbname='postgres' user='postgres' host='127.0.0.1' password='dbpassword' port='5433'"

try:
    conn = psycopg2.connect(connstring)
except:
	print "couldnt connect to the database you idiot"

cur = conn.cursor()

cur.execute("UPDATE migrations_restaurant set website = 'http://www.traceaustin.com/' where id=1")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.eastsidecafeaustin.com/' where id=2")
cur.execute("UPDATE migrations_restaurant set website = 'http://barleyswine.com/' where id=3")
cur.execute("UPDATE migrations_restaurant set website = 'http://oddduckaustin.com/' where id=4")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.winkrestaurant.com/' where id=5")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.apothecaryaustin.com/' where id=6")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.galaxycafeaustin.com/' where id=7")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.chickenlollypop.com/' where id=36")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.asiamarketaustin.com/restaurantHome.html' where id=37")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.yelp.com/biz/888-pan-asian-restaurant-austin' where id=38")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.hohochinesebbq.com/common/template/default.jsp?href=index.jsp' where id=39")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.yelp.com/biz/chens-noodle-house-austin' where id=40")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.firstwokaustin.com/' where id=41")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.dinhochinesebbq.com/' where id=42")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.melvinsdelicomfort.com/' where id=57")
cur.execute("UPDATE migrations_restaurant set website = 'http://littledeliandpizza.com/' where id=58")
cur.execute("UPDATE migrations_restaurant set website = 'http://fricanosdeli.com/' where id=59")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.neworldeli.com/' where id=60")
cur.execute("UPDATE migrations_restaurant set website = 'http://neworldcafe.com/' where id=61")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.gsdynamitedeli.com/' where id=62")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.yelp.com/biz/tam-deli-and-cafe-austin' where id=63")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.santoriniaustin.com/' where id=64")
cur.execute("UPDATE migrations_restaurant set website = 'http://athenianbargrill.com/' where id=65")
cur.execute("UPDATE migrations_restaurant set website = 'http://arpeggiogrill.com/' where id=66")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.bigfatgreekgyros.com/' where id=67")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.zorbagreekrestaurant.com/' where id=68")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.tinosgreekcafe.com/' where id=69")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.mylittlegreek.com/' where id=70")
cur.execute("UPDATE migrations_restaurant set website = 'http://maryesgourmetpizza.com/' where id=22")
cur.execute("UPDATE migrations_restaurant set website = 'http://patrizis.com/' where id=23")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.mandolasmarket.com/' where id=24")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.milanoaustin.com/' where id=25")
cur.execute("UPDATE migrations_restaurant set website = 'http://andiamoitaliano.com/' where id=26")
cur.execute("UPDATE migrations_restaurant set website = 'http://latraviata.net/' where id=27")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.realespizza.com/' where id=28")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.sarahsmediterranean.com/' where id=50")
cur.execute("UPDATE migrations_restaurant set website = 'http://arpeggiogrill.com/' where id=51")
cur.execute("UPDATE migrations_restaurant set website = 'http://themedchef.com/' where id=52")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.dimassi.com/' where id=53")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.yelp.com/biz/pars-mediterranean-supermarket-and-deli-austin' where id=54")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.pharas.com/' where id=55")
cur.execute("UPDATE migrations_restaurant set website = 'http://zoeskitchen.com/' where id=56")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.luckyrobotrestaurant.com/' where id=43")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.kome-austin.com/' where id=44")
cur.execute("UPDATE migrations_restaurant set website = 'http://ryuofjapan.com/' where id=45")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.loveballsbus.com/' where id=46")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.lavacateppan.com/' where id=47")
cur.execute("UPDATE migrations_restaurant set website = 'http://mail.uchikoaustin.com/uchi' where id=48")
cur.execute("UPDATE migrations_restaurant set website = 'http://mail.uchikoaustin.com/uchiko' where id=49")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.fondasanmiguel.com/' where id=29")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.juliosaustin.com/' where id=30")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.currasgrill.com/' where id=31")
cur.execute("UPDATE migrations_restaurant set website = 'http://habanerocafe.com/' where id=32")
cur.execute("UPDATE migrations_restaurant set website = 'http://hechoenmexico-restaurant.com/' where id=33")
cur.execute("UPDATE migrations_restaurant set website = 'http://www.austintxmexicanfood.com/' where id=34")
cur.execute("UPDATE migrations_restaurant set website = 'http://consueloskitchen.com/' where id=35")


conn.commit()





