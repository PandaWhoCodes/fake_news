from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import requests
import json

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/dorequest", methods=["GET"])
def responses():
    data = request.args.get('url')
    response = requests.get("http://www.fakenewsai.com/detect?url=http%3A%2F%2F" + data)
    response = json.loads(response.text)
    if response["error"] == True:
        print("Error HO gaya rey")
        return jsonify({'data': response})
    else:
        return jsonify({'data': response})
    # print(data)


if __name__ == "__main__":
    app.run(debug=True)
