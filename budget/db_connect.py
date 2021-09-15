import psycopg2
from psycopg2 import Error, connect

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="postgres",
                                  password="asad1",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="budget")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    cursor.execute("SELECT version();")
    cursor.execute("CREATE TABLE budget1 (\
        food text );")


    connection.commit()
    # cursor.execute("INSERT INTO budget1 (food)\
    #     VALUES ('doofs');")

    # Fetch result
    # record = cursor.fetchall()
    # print("You are connected to - ", record, "\n")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL: \n", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
