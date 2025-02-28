from flask import Flask, render_template

print('my name is anthony')
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

app.run(port=7000)
