from flask import Flask, render_template, jsonfy

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


@app.route("/")
def hello_justino():
    return render_template('home.html', jobs=JOBS, company_name='Infordata')


@app.route("/jobs")
def list_jobs():
    return jsonfy(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
