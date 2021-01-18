# import psycopg2
import time as time
# # Connect to an existing database
# conn = psycopg2.connect("dbname=testing user=postgres password=password")

# # Open a cursor to perform database operations
# cur = conn.cursor()

# # Execute a command: this creates a new table
# # cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

# # Pass data to fill a query placeholders and let Psycopg perform
# # the correct conversion (no more SQL injections!)
# cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",(100, "abc'def"))

# # Query the database and obtain data as Python objects
# cur.execute("SELECT * FROM test;")
# cur.fetchall()
# cur.description

# # Make the changes to the database persistent
# conn.commit()

# # Close communication with the database
# cur.close()
# conn.close()

animation = "|/-\\"
idx = 0
thing_not_complete = True
while thing_not_complete:
    print(animation[idx % len(animation)], end="\r")
    idx += 1
    time.sleep(0.1)