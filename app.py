from flask import Flask, request, jsonify
from src import calculate

app = Flask(__name__)


@app.route(rule="/productionplan", methods=['POST'])
def post_api():
    try:
        payload = request.json
        result = calculate(payload)
        return jsonify(result)
    except Exception as ex:
        response = {
                'status_code': 500,
                'status': 'Internal Server Error'+ ex
        }
        return jsonify(response), 500
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)

