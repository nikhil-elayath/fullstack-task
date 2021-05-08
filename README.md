# fullstack-task
# Setting up client
Go to fullstack-stack folder and do npm i to install all the necesssary node modules
npm start command will get the client up and running
# Setting up DB
Go to server->db-init-> run the command - psql -U "your username" -f CreateDB.sql
This will create the table
After that run psql -U "your username" -f InsertData.sql
This will insert  some dummy data in to the table

# Setting up Server
Run the server by python app.py

# Development process
Created feature branches for each feature locally and merged it directly into development merge.
After developing all the features and merging it to the development branch. Made sure the development branch is bug free and everything is working fine.
Then merged the development branchwith main

