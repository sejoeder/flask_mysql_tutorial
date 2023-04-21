from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Test Scientist',
    'location': 'Test1, Vienna',
  },
  {
    'id': 2,
    'title': 'Rambo Ramon Rainer Vollzeit',
    'location': 'bei mir, Wien',
  },
  {
    'id': 3,
    'title': 'Test Analyst',
    'location': 'Test2, Vienna',
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Sewe')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug=True)