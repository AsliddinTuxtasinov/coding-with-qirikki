from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return f"Welcome to Home page"


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'GET':
        return render_template('add.html')

    if request.method == 'POST':
        a = int(request.form.get('a', 0))
        b = int(request.form.get('b', 0))

        summ = a + b
        return render_template('add.html', summ=summ)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
