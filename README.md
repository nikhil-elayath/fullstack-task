# fullstack-task
# Setting up client
Go to fullstack-stack folder and do npm i to install all the necesssary node modules
# Setting up DB
Go to server->db-init-> run the command - psql -U "your username" -f CreateDB.sql
This will create the table
After that run psql -U "your username" -f InsertData.sql
This will insert  some dummy data in to the table

# Setting up Server
Run the server by python app.py

