#!/usr/bin/env python3
import sqlite3
id = 1
type = ['door', 'temperature', 'door', 'motion', 'temperature']
zone = ['kitchen', 'kitchen', 'garage', 'garage', 'garage']
#connect to database file
dbconnect = sqlite3.connect("exercise4db.db");
dbconnect.row_factory = sqlite3.Row;
cursor = dbconnect.cursor();
#cursor.execute('CREATE TABLE sensors (id integer, type text, zone text)')
#Delete table to repopulate
cursor.execute('DELETE FROM sensors');

for i in range(5): 
    #execute insert statement
    cursor.execute('''INSERT INTO sensors VALUES (?, ?, ?)''',(id, type[id-1] , zone[id-1]));
    id += 1;
dbconnect.commit();
cursor.execute("SELECT * FROM sensors WHERE zone = 'kitchen'");
print('All sensors in the ktichen');
for row in cursor:
    print(row['id'],row['type'],row['zone'] );
print('\nAll door sensors')
cursor.execute("SELECT * FROM sensors WHERE type = 'door'");
for row in cursor:
    print(row['id'],row['type'],row['zone'] );
dbconnect.close();