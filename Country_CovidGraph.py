import requests
import json
import datetime
import matplotlib.pyplot as plt
from datetime import timedelta

def country_graph():

    url = "https://covid-193.p.rapidapi.com/history"
    date_string = '2020-04-01'
    date = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()

    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)

    country = input("Enter the country you would like to search for: ")

    case_list = []
    date_list = []

    while date <= yesterday:

        querystring = {"country":country,"day":date}

        headers = {
            'x-rapidapi-key': "574d25f133msh5c58c65e8a4c944p1e6b8fjsnee1da55d91cd",
            'x-rapidapi-host': "covid-193.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.text
        parsed = json.loads(data)
        if parsed["results"] == 0:
            date += timedelta(days=1)
            continue
        else:
            response_dict = parsed["response"][0]
            cases_dict = response_dict["cases"]
            if cases_dict["new"] is None:
                date += timedelta(days=1)
                continue
            else:
                case_list.append(int(cases_dict["new"]))
                date_list.append(response_dict["day"])
                #print(response_dict["day"])
                date += timedelta(days=1)


    plt.plot(date_list, case_list)
    plt.xlabel("Date")
    plt.ylabel("Cases")
    plt.title("Covid-19 graph")
    plt.show()

