from flask import Flask , render_template, send_from_directory
import database
import json

db =database.DataBase()
app = Flask(__name__, static_url_path='')

@app.route("/")
def hello():
    return send_from_directory('frontend' ,'index.html')

@app.route("/isAvailable")
def available():

    return json.dumps({'status': 'good', 'parking': db.GetParking()  })


if __name__ == "__main__":
    app.run()
