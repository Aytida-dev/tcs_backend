from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
  return "Hello World, from Flask"


import db
# import user_controller

import APPLICATION_DETAILS_TABLE
import SERVER_STATUS_TABLE
import USER_LOGIN_ELAPSED_TIME
import USER_SESSIONS_TABLE
# import MAX_VALUE_TABLE