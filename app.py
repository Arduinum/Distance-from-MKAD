from flask import Flask
from api_geocoder import api_geo

app = Flask(__name__)
app.register_blueprint(api_geo)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.1.1')
