from flask import Flask, request
import json

app = Flask(__name__)


@app.route(rule="/productionplan", methods=['POST'])
def post_api():
    # payload = request.json
    file = open('files/payload3.json')
    payload = json.load(file)
    load = payload["load"]
    fuels = payload["fuels"]
    co2 = fuels["co2(euro/ton)"]
    wind = fuels["wind(%)"]
    powerplants = payload["powerplants"]

    for i in range(len(powerplants)):
        if powerplants[i]["type"] == "gasfired":
            cost = fuels["gas(euro/MWh)"]
            cost += co2 * 0.3 * powerplants[i]["pmax"]
            powerplants[i]["cost"] = cost
            powerplants[i]["co2"] = 0.3
        if powerplants[i]["type"] == "turbojet":
            powerplants[i]["cost"] = fuels["kerosine(euro/MWh)"]
            powerplants[i]["co2"] = 0
        if powerplants[i]["type"] == "windturbine":
            powerplants[i]["cost"] = 0
            powerplants[i]["co2"] = 0

    powerplants = sorted(
            powerplants, 
            key = lambda x: (x["efficiency"], -x["cost"], -x["co2"]),
            reverse=1
        )

    total = 0
    value = 0
    result = []

    for i in range(len(powerplants)):

        value = powerplants[i]["pmax"]
        if powerplants[i]["type"] == "windturbine":
            value = round(value * (wind/100),2)

        if (total + value) <= load:
            powerplants[i]["use"] = True
            powerplants[i]["quantity"] = value
            total += value
            item = {
                "name" : powerplants[i]["name"],
                "p": value
            }
            result.append(item)
        elif total + powerplants[i]["pmin"] <= load:
            value = load - total
            powerplants[i]["use"] = True
            powerplants[i]["quantity"] = value
            total = load
            item = {
                "name" : powerplants[i]["name"],
                "p": value
            }
            result.append(item)
        else:
            powerplants[i]["use"] = False
            powerplants[i]["quantity"] = 0
            item = {
                "name" : powerplants[i]["name"],
                "p": 0
            }
            result.append(item)
    
    return result

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8889)

