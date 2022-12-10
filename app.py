from flask import Flask, render_template, jsonify, make_response
from json import dumps
from mock_data import person_list
import os

app = Flask(__name__)

@app.route("/", methods=['GET'])
def main():
    return render_template("index.html")

@app.route("/persons", methods=["GET"])
def persons():
    # return make_response(dumps(person_list))
    return jsonify(person_list)

@app.route("/person", methods=['GET'])
def person():
    return jsonify({"id":"12345","surname":"Drees","firstname":"Jan"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)