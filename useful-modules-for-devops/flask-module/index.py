from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome..."

@app.route("/helloworld")
def helloworld():
    user = request.args.get('user')
    if(user):
        return "Hello "+ user
    return "Hello Stranger"

if __name__ == "__main__":
    app.run(host="localhost", port=int("3423"), debug = True)