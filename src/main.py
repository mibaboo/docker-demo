from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def get_pod_name():
    pod_name = os.environ.get('HOSTNAME')
    return f'This is the Kubernetes pod name: {pod_name}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

