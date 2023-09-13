from flask import Flask, request, jsonify
from src import calculate
import logging

app = Flask(__name__)


@app.route(rule="/productionplan", methods=['POST'])
def post_api():
    try:
        logging.info('productionplan end point called')
        payload = request.json
        result = calculate(payload)
        return jsonify(result)
    except Exception as ex:
        logging.exception("Exception occurred")
        response = {
                'status_code': 500,
                'status': 'Internal Server Error'
        }
        return jsonify(response), 500
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)

