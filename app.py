from flask import Flask, render_template, jsonify
from database import load_jobs_from_database


app = Flask(__name__)



  
@app.route("/")
def hello_world():
  jobs = load_jobs_from_database()
  return render_template('home.html', jobs=jobs, company_name='Sewe')

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_database()
  return jsonify(jobs)

if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug=True)