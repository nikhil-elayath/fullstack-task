
# coding: utf-8

# In[1]:

# Required Imports
from flask import Flask
from flask import request
from flask_cors import CORS
import psycopg2



# In[ ]:

# Establishing connection with MongoDB with specified database
app = Flask(__name__)
CORS(app)
conn_string = "host='localhost' dbname='university' user='postgres' password='password'"
conn = psycopg2.connect(conn_string)
cur = conn.cursor()


        
@app.route("/voltality",methods=["GET"])

def  voltality():
    print("ajajaj")
    cur.execute("SELECT * FROM university_details")
    items = cur.fetchall()
    print(items)


   
    return("slsl")

        
if __name__ == '__main__':
    app.run(debug=False,port=5000)


# In[ ]:


# get_ipython().system('pip install flask_cors')


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



