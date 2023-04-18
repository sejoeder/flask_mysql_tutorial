from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Geiler Typ Vollzeit',
    'location': 'bei mir, Wien',
  },
  {
    'id': 2,
    'title': 'Rambo Ramon Rainer Vollzeit',
    'location': 'bei mir, Wien',
  },
  {
    'id': 3,
    'title': 'Hure der Reichen',
    'location': 'OEVP, Wien',
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Sewe')

if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug=True)