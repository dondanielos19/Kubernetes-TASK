from flask import Flask
import os

app = Flask(__name__)


app_name = os.environ.get('APP_NAME')
variable = os.environ.get('VARIABLE')
@app.route('/')
def hello():
    return f'Hello! This is simple App: {app_name} {variable}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

