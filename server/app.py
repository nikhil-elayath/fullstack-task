
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

@app.route("/create-university-entry",methods=["POST"])

def  createUniversityDetailsEntry():
    print("createUniversityDetailsEntry")
    try:
        cur.execute("INSERT INTO university_details(alpha_two_code, country, domain, university_name, web_page, university_description, university_image) VALUES (%s,%s,%s,%s,%s,%s,%s)",[data['alpha_two_code'],data['country'],data['domain'],data['university_name'],data['web_page'],data['university_description'],data['university_image'] ])
        msg = {"msg": "Success"}
        return msg
    except Exception as e:
        print(e)
        response = {'statusCode':'500', 'msg':'Data not retrieved successfully'} 
        return (response) 

@app.route("/update-university-entry",methods=["POST"])

def  updateUniversityDetailsEntry():
    data = json.loads(request.data)

    try:
        cur.execute("INSERT INTO university_details(alpha_two_code, country, domain, university_name, web_page, university_description, university_image) VALUES (%s,%s,%s,%s,%s,%s,%s)",[data['alpha_two_code'],data['country'],data['domain'],data['university_name'],data['web_page'],data['university_description'],data['university_image'] ])
        response = {'statusCode':'200', 'msg':'Data updated sucessfully'} 
        return (response)
    except Exception as e:
        response = {'statusCode':'500', 'msg':'Data not updated'} 
        return (response)

# delete
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


@app.route("/search",methods=["POST"])

def  getSearchResults():
    print("getSearchResults")
    data = json.loads(request.data)

    try:
        cur.execute("SELECT * FROM university_details WHERE  university_name ILIKE (%s) AND alpha_two_code = (%s) ", [data['searchQuery']+"%",data['country']])
        msg = {"msg": "Sucess"}
        code=200
        row_headers=[x[0] for x in cur.description] #this will extract row headers
        rv = cur.fetchall()
        json_data=[]
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
        return (json.dumps(json_data))
        
        
    except Exception as e:
        print("SS",e)
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



