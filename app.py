from flask import Flask, render_template, jsonify
from database import engine

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': ' Maputo, Mozambique',
    'salary': ' 120.000,00 MT'
}, {
    'id': 2,
    'title': 'Frontend Engineer',
    'location': ' Remote',
}, {
    'id': 3,
    'title': 'Backend Engineer',
    'location': ' JHB, South Africa',
    'salary': ' R 100.000,00'
}, {
    'id': 4,
    'title': 'Data Scientist',
    'location': ' Lisbo, Portugal',
    'salary': ' Eur 130.000,00'
}]

def load_jobs_from_db():
with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_dicts = []
    for row in result.all():
     result_dicts.append(dict(row))


@app.route("/")
def hello_justino():
    return render_template('home.html', jobs=JOBS, company_name='Infordata')


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
