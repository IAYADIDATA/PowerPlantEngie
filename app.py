from flask import Flask, request
from src import calculate

app = Flask(__name__)


@app.route(rule="/productionplan", methods=['POST'])
def post_api():
    payload = request.json
    result = calculate(payload)
    return result

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)

