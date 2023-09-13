import pytest
import json
from src import calculate

def test_reponse3():
    file = open('../files/payload3.json')
    payload = json.load(file)
    file = open('../files/response3.json')
    response3 = json.load(file)
    assert calculate(payload) == response3

if __name__ == "__main__":
     pytest.main()  