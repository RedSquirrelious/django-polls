#testitall.py

with open('.env-dbk') as d:
	DATABASE_KEY = d.read().strip()
	print(DATABASE_KEY)
