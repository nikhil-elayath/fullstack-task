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
# Running images
![homepage](https://user-images.githubusercontent.com/25564806/117542425-39d64b80-b036-11eb-9b6a-68ca109c7d71.png)
![searchResult](https://user-images.githubusercontent.com/25564806/117542428-3b077880-b036-11eb-9af3-b168a3880f39.png)
![searchFilter](https://user-images.githubusercontent.com/25564806/117542429-3b077880-b036-11eb-88c0-2333f585e5de.png)

