from app import app

@app.route('/signup')
def signup():
  return "this is signup, from Flask"