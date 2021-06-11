import requests
import json
import datetime
import matplotlib.pyplot as plt
from datetime import timedelta

def province_graph():
    url = "https://covid-19-statistics.p.rapidapi.com/reports"

    ISO = input("Enter the ISO code of the country that you would like to search for.(ISO code of India is IND. ISO code of New Zealand is NZ): ")
    province = input("Enter the province you would like to search for: ")

    date_string = '2020-04-01'
    date = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()

    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)

    case_list = []
    date_list = []

    while date <= yesterday:
        querystring = {"date":date,"iso":ISO,"region_province":province}

        headers = {
            'x-rapidapi-key': "574d25f133msh5c58c65e8a4c944p1e6b8fjsnee1da55d91cd",
            'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        data = response.text
        parsed = json.loads(data)

        if len(parsed["data"]) == 0:
            date += timedelta(days=1)
            continue

        #if parsed["data"] == 0:
        #    date += timedelta(days=1)
        #    continue
        else:
            data_dict = parsed["data"][0]
            if data_dict["confirmed_diff"] is None:
                date += timedelta(days=1)
                continue
            else:
                case_list.append(int(data_dict["confirmed_diff"]))
                date_list.append(data_dict["date"])
                #print(data_dict["date"])
                date += timedelta(days=1)


    plt.plot(date_list, case_list)
    plt.xlabel("Date")
    plt.ylabel("Cases")
    plt.title("Covid-19 graph")
    plt.show()