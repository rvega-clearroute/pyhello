from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>version 1.0.5</h1>'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=80)

