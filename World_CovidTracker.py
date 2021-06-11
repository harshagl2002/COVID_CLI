import requests
import json
import datetime

def world():

    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)

    url = "https://covid-19-statistics.p.rapidapi.com/reports/total"

    querystring = {"date":yesterday}

    headers = {
        'x-rapidapi-key': "574d25f133msh5c58c65e8a4c944p1e6b8fjsnee1da55d91cd",
        'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    parsed = json.loads(response.text)

    print()
    print("NEW COVID cases in the world on", parsed["data"]["date"], "is", parsed["data"]["confirmed_diff"])
    print("TOTAL NUMBER of COVID cases in the world till", parsed["data"]["date"], "is", parsed["data"]["confirmed"])
    print("Total number of DEATHS in the world till", parsed["data"]["date"], "is", parsed["data"]["deaths"])
    print("ACTIVE number of COVID cases in the world till", parsed["data"]["date"], "is", parsed["data"]["active"])
    print("Total number of RECOVERIES in the world till", parsed["data"]["date"], "is", parsed["data"]["recovered"])



