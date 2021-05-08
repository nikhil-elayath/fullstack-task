
# coding: utf-8

# In[1]:

# Required Imports
from flask import Flask
from flask import request
from flask_cors import CORS
import psycopg2
from flask import jsonify
import json

# In[ ]:

# Establishing connection with specified database
app = Flask(__name__)
CORS(app)
conn_string = "host='localhost' dbname='university' user='postgres' password='password'"
conn = psycopg2.connect(conn_string)
cur = conn.cursor()


# Get api that will retrieve all the data present in the university table
@app.route("/get-university-details",methods=["GET"])

def  getUniversityDetails():
    print("getUniversityDetails")
    try:
        cur.execute("SELECT * FROM university_detdails")
        row_headers=[x[0] for x in cur.description] #this will extract row headers
        rv = cur.fetchall()
        json_data=[]
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
        return (json.dumps(json_data))

    except Exception as e:
        print(e)
        response = {'statusCode':'500', 'msg':'Data not retrieved successfully'} 
        return (response)


# Create API that will take json object with details of the entry and will create an entry in the university_details table
# data required are
# alpha_two_code,country,domain,university_name,web_page,university_description,university_image
@app.route("/create-university-entry",methods=["POST"])

def  createUniversityDetailsEntry():
    print("createUniversityDetailsEntry")
    try:
        cur.execute("INSERT INTO university_details(alpha_two_code, country, domain, university_name, web_page, university_description, university_image) VALUES (%s,%s,%s,%s,%s,%s,%s)",[data['alpha_two_code'],data['country'],data['domain'],data['university_name'],data['web_page'],data['university_description'],data['university_image'] ])
        msg = {"msg": "Success"}
        return msg
    except Exception as e:
        print(e)
        response = {'statusCode':'500', 'msg':'Could not create an entry'} 
        return (response) 

# Update api for updating an existing entry with id
@app.route("/update-university-entry",methods=["POST"])

def  updateUniversityDetailsEntry():
    data = json.loads(request.data)
    try:
        cur.execute("UPDATE  university_details SET (alpha_two_code, country, domain, university_name, web_page, university_description, university_image) VALUES (%s,%s,%s,%s,%s,%s,%s) WHERE id=(%s)",[data['alpha_two_code'],data['country'],data['domain'],data['university_name'],data['web_page'],data['university_description'],data['university_image'], data['id'] ])
        response = {'statusCode':'200', 'msg':'Data updated sucessfully'} 
        return (response)
    except Exception as e:
        response = {'statusCode':'500', 'msg':'Data not updated'} 
        return (response)

# delete api that will delete the entry with id
@app.route("/delete-university-entry",methods=["POST"])

def  deleteUniversityDetailsEntry():
    print("createUniversityDetailsEntry")
    data = json.loads(request.data)

    try:
        cur.execute("DELETE FROM university_details WHERE id=(%s)",[data['id']])
        response = {'statusCode':'200', 'msg':'Data deleted successfully'} 
        return (response)
    except Exception as e:
        response = {'statusCode':'500', 'msg':'Data could not be deleted'} 
        return (response)


# search api that will fetch details with university name and country code
@app.route("/search",methods=["POST"])

def  getSearchResults():
    print("getSearchResults")
    data = json.loads(request.data)

    try:
        cur.execute("SELECT * FROM university_details WHERE  university_name ILIKE (%s) AND alpha_two_code = (%s) ", [data['searchQuery']+"%",data['country']])
        row_headers=[x[0] for x in cur.description] #this will extract row headers
        rv = cur.fetchall()
        json_data=[]
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
        return (json.dumps(json_data))
        
        
    except Exception as e:
        print("SS",e)
        response = {'statusCode':'500', 'msg':'Data could not be retrieved'} 
        return (response)

        
if __name__ == '__main__':
    app.run(debug=False,port=5000)


# In[ ]:


# get_ipython().system('pip install flask_cors')


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



