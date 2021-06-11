import requests
import json
import datetime
import matplotlib.pyplot as plt
from datetime import timedelta

def world_graph():
    date_string = '2020-04-01'
    date = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()


#yesterday = today - datetime.timedelta(days=1)

    url = "https://covid-19-statistics.p.rapidapi.com/reports/total"

    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
 
    case_list = []  
    date_list = []

    while date <= yesterday:

        querystring = {"date":date}

        headers = {
            'x-rapidapi-key': "574d25f133msh5c58c65e8a4c944p1e6b8fjsnee1da55d91cd",
            'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        parsed = json.loads(response.text)

        if parsed["data"]["confirmed"] is None:
            date += timedelta(days=1)
            continue
        else:
            case_list.append(int(parsed["data"]["confirmed_diff"]))
            date_list.append(parsed["data"]["date"])
            #print(parsed["data"]["date"])
            date += timedelta(days=1)


    plt.plot(date_list, case_list)
    plt.xlabel("Date")
    plt.ylabel("Cases")
    plt.title("Graph showing the number of Covid-19 cases world wide")
    plt.show()



