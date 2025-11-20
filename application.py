from flask import Flask

# Elastic Beanstalk Python platform by default looks for "application" WSGI object
application = Flask(__name__)

@application.route("/")
def index():
    return "<h1>Hello from Elastic Beanstalk Python App 🚀</h1>"

@application.route("/health")
def health():
    # EB health check ke liye simple OK route
    return "OK", 200


if __name__ == "__main__":
    # Local run ke liye
    application.run(host="0.0.0.0", port=5000, debug=True)
