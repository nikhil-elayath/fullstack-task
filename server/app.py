
# coding: utf-8

# In[1]:

# Required Imports
from flask import Flask
from flask import request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# from plotly.subplots import make_subplots
# from flask_pymongo import PyMongo
# import requests
# # import plotly.express as px
# import pandas as pd
# import chart_studio
# import chart_studio.tools as tls
# import plotly.graph_objs as go
# import chart_studio.plotly as py
# import os, sys
# import matplotlib
# import base64
# from matplotlib import cm
# import math
# from matplotlib import pyplot as plt
# import numpy as np
# from matplotlib.patches import Circle, Wedge, Rectangle
# # py.sign_in('nikhile' ,'OkrregXQ8kgWtuZEcuOI')
# py.sign_in('nikhilnikhil','9qEyahleVGoflQq6YbTe')


# In[ ]:

# Establishing connection with MongoDB with specified database
app = Flask(__name__)
CORS(app)
db = SQLAlchemy()



# Plotting OHLC graph for indices
@app.route("/ohlcindices",methods=["GET"])
def ohlc_indices():
    print("from api")
    return ("url")

if __name__ == '__main__':
    app.run(debug=False,port=5000)






