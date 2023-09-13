# *PowerPlantEngie*
This is a Flask project to solve the Powerplant Coding Challenge.

### *Run project*

To expose api in port :8888 please follow the setps:
  
   - Clone this repository
   - Create a virtual environment and activate the environment (venv, virtualenv, conda...)
     (example: python3 -m venv venv | source venv/bin/activate)
     PS: You should use python version >= 3.8
   - Install required packages: pip install -r requirements.txt
   - Run the following command: python app.py or flask run --port=8888
   - To call the api endpoint please use a post http call to http://127.0.0.1:8888/productionplan
   
### *Algorithm explanation*

There is a function in the src\findBestPowerPlants module named calculate, this function contains the algorithm used calculate how much power each of a multitude of different powerplants need to produce (a.k.a. the production-plan) when the load is given and taking into account the cost of the underlying energy sources (gas, kerosine) and the Pmin and Pmax of each powerplant.

At first, it takes all the provided data to calculate the cost (including CO2) and the amount of power the powerplant can generate.

After that, it sorts the the list of powerplants by efficiency DESC then cost ASC then co2 ASC.

Finally, it identifies which powerplat we should use and the specified quantity to reach the load.
