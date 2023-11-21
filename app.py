from flask import Flask,render_template
# from database import load_jobs_from_db
from db import load_jobs_from_db
app = Flask(__name__)




@app.route('/')

def home():
    jobs = load_jobs_from_db()
    return render_template("home.html",jobs = jobs,company_name="Jawan")


print(__name__)
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True )