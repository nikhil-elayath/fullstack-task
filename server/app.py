
# coding: utf-8

# In[1]:

# Required Imports
from flask import Flask
from flask import request
from flask_cors import CORS
import psycopg2
from flask import jsonify




# In[ ]:

# Establishing connection with MongoDB with specified database
app = Flask(__name__)
CORS(app)
conn_string = "host='localhost' dbname='university' user='postgres' password='password'"
conn = psycopg2.connect(conn_string)
cur = conn.cursor()


        
@app.route("/get-university-details",methods=["GET"])

def  getUniversityDetails():
    print("getUniversityDetails")
    try:
        cur.execute("SELECT * FROM university_details")
        return jsonify(items=cur.fetchall())

    except Exception as e:
        print(e)
        msg = {"msg": "Failed to update the userdetails! please contact your administartor."}
        code=500
        return jsonify(msg)

@app.route("/create-university-entry",methods=["POST"])

def  createUniversityDetailsEntry():
    print("createUniversityDetailsEntry")
    try:
        cur.execute("INSERT INTO university_details(alpha_two_code, country, domain, university_name, web_page, university_description, university_image) VALUES (%s,%s,%s,%s,%s,%s,%s)",('fname','lname','username','password','cpassword','email','selection'))
        msg = {"msg": "Success"}

        return msg
    except Exception as e:
        print(e)
        msg = {"msg": "Failed to update the userdetails! please contact your administartor."}
        code=500
        return jsonify(msg) 

@app.route("/update-university-entry",methods=["POST"])

def  updateUniversityDetailsEntry():
    print("createUniversityDetailsEntry")
    try:
        cur.execute("INSERT INTO university_details(alpha_two_code, country, domain, university_name, web_page, university_description, university_image) VALUES (%s,%s,%s,%s,%s,%s,%s)",('fname','lname','username','password','cpassword','email','selection'))
    except Exception as e:
        print(e)
        msg = {"msg": "Failed to update the userdetails! please contact your administartor."}
        code=500

    return msg

        
if __name__ == '__main__':
    app.run(debug=False,port=5000)


# In[ ]:


# get_ipython().system('pip install flask_cors')


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



