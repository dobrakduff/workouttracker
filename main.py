import requests
from datetime import datetime
api_k = "684c30e632f42d88cbd1d66cd7b7363c"
api_id= "0da98ea0"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/480e52bacd4242aa681ff567ea7e9de6/workout/workouts"
headers={
    "x-app-id": api_id,
    "x-app-key": api_k,
}
exercise_text = input("What you did")
params = {
    "query": exercise_text,
    "gender":"male",
    "weight_kg":"65",
    "height_cm":"140",
    "age":"19",
}


response = requests.post(exercise_endpoint, json=params,headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_input={
        "workout":{
            "date": today_date,
            "time":now_time,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_request = requests.post(sheet_endpoint,json=sheet_input)
print(sheet_request.text)