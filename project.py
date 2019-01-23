from flask import Flask
app = Flask(__name__)
@app.route('/')
def my_sample_project():
    return 'my sample project'