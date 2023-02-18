import sqlite3

sqliteConnection = sqlite3.connect('Students_data.db')
cursor = sqliteConnection.cursor()

sql_query1 =""" SELECT * FROM Students"""
sql_query2 = """SELECT * FROM Students WHERE Fee == 45000"""
sql_query3 = """ SELECT * FROM Students WHERE Fee > 24000"""
sql_query4 = """SELECT Fee FROM Students""" 
sql_query5 = """UPDATE Students SET Fee = 2500"""
sql_query6 = """SELECT * FROM Students WHERE Fee == 45000"""

cursor.execute(sql_query6)
result = cursor.fetchall()

print(result)
# for students in result:
#    print(students[0], students[1], students[2], students[3])
