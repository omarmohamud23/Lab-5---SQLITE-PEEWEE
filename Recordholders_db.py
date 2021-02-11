import sqlite3 


conn = sqlite3.connect('Recordholders_db.sqlite')  #creating my database connection



conn.execute('CREATE TABLE IF NOT EXISTS record_holders(Name text, Country text, Number_of_catches int)') #creating table in our database
conn.execute('INSERT INTO record_holders VALUES("Janne Mustonen", "Finland", 98)')
conn.execute('INSERT INTO record_holders VALUES("Ian Stewart", "Canada", 94)')
conn.execute('INSERT INTO record_holders VALUES("Aaron Gregg", "Canada", 88)')
conn.execute('INSERT INTO record_holders VALUES("Chad Taylor", "USA", 78)')

for row in conn.execute('SELECT * FROM record_holders'):
    print(row)

conn.commit()


name = input("Please enter name of the record holder: ")  ## add new record 
country = input("country?: ")
number_of_catches = int(input("number of catches: "))     

conn.execute('INSERT INTO record_holders VALUES (?,?,?)', (name, country, number_of_catches))
conn.commit()


Get_record_holder_by_name="Chad Taylor"  ## searching specific record holder by their name
conn.execute("SELECT * FROM record_holders WHERE Name=?", (Get_record_holder_by_name,))
conn.commit()


sql_update_query = 'Update record_holders set Name = ? where Number_of_catches = ?'  ## updating the number of catches
data = (name, number_of_catches)   
conn.execute(sql_update_query, data)
conn.commit()
   
Record_holder_deleted = "Aaron Gregg" ## deleting a recodholder by thier name 
conn.execute('DELETE FROM record_holders WHERE Name = ?', (Record_holder_deleted,))
conn.commit()
   

conn.close()