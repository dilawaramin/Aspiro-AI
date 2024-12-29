# backend entry pointfrom flask import Flask
from flask import Flask
from app.communications.sms.sms_recieve import sms_blueprint

# initialize flask app
app = Flask(__name__)

# Register blueprints
app.register_blueprint(sms_blueprint, url_prefix='/communications')


# running the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)