from flask import Flask

app = Flask(__name__)
@app.route('/')
def main():
    return '<h1>Пошел нахуй</h1>'

app.run(port=5000)
