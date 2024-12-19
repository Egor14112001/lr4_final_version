import requests
import time
import random

for i in range(5):
    params = {'flat_id': i}
    data = {"Car_Name":"ritz",
        "Year":(random.randint(2000,2024)),
        "Present_Price":5.59,
        "Driven_kms":random.randint(0,5000),
        "Fuel_Type":"Petrol",
        "Selling_type":"Dealer",
        "Transmission":"Manual",
        "Owner":(random.randint(0,1)),
        "Driven_run":"mid"
        }
    response = requests.post('http://localhost:8001/api/prediction', params=params, json=data)
    time.sleep(random.randint(1,5))
    print(response.json())