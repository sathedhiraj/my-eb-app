from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Elastic Beanstalk!"

# Elastic Beanstalk looks for application variable
application = app

if __name__ == "__main__":
    app.run(debug=True)
