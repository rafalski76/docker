from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello():
    return "Test strony we Flask - " + os.environ["MY_VAR"]

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9085)
