

def calculate(payload):
    try:
        load = payload["load"]
        fuels = payload["fuels"]
        co2 = fuels["co2(euro/ton)"]
        wind = fuels["wind(%)"]
        powerplants = payload["powerplants"]

        # Calculate cost of the fuels of each powerplan
        # And cost of the CO2
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

        # Sort powerplants by efficiency then cost then co2
        powerplants = sorted(
                powerplants, 
                key = lambda x: (x["efficiency"], -x["cost"], -x["co2"]),
                reverse=1
            )

        total = 0
        value = 0
        result = []

        # Identify which powerplants we will use 
        # Calculate Quantity for each one
        for i in range(len(powerplants)):
            # Multiply the pmax by the percentage of wind
            # to calculate the exact power can be produced
            value = powerplants[i]["pmax"]
            if powerplants[i]["type"] == "windturbine":
                value = round(value * (wind/100),2)
            # Use the powerplant if the pmax is not above the load
            if (total + value) <= load:
                powerplants[i]["use"] = True
                powerplants[i]["quantity"] = value
                total += value
                # Add a new item that contains the name and the quantity p
                item = {
                    "name" : powerplants[i]["name"],
                    "p": value
                }
                result.append(item)
            # Use the powerplant if the pmin >= the rest to reach the load
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
            # Unusefull powerplant
            else:
                powerplants[i]["use"] = False
                powerplants[i]["quantity"] = 0
                item = {
                    "name" : powerplants[i]["name"],
                    "p": 0
                }
                result.append(item)
        return result
    except Exception as ex:
        response = {
            'status_code': 500,
            'status': 'Internal Server Error'
        }
        return response
        
