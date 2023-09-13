from flask import Flask, request


app = Flask(__name__)


@app.route(rule="/productionplan", methods=['POST'])
def post_api():
    print(request.json)
    data = request.json
    return data

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8889)

