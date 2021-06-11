import requests
import json
import datetime

def province():
    url = "https://covid-19-statistics.p.rapidapi.com/reports"

    ISO = input("Enter the ISO code of the country that you would like to search for.(ISO code of India is IND. ISO code of New Zealand is NZ): ")
    province = input("Enter the province you would like to search for: ")
    date = input("Enter the date (yyyy-mm-dd) you would like to search for: ")

    year,month,day = date.split('-')

    isValidDate = True
    try :
        datetime.datetime(int(year),int(month),int(day))
    except ValueError :
        isValidDate = False

    if(isValidDate) :

        querystring = {"date":date,"iso":ISO,"region_province":province}

        headers = {
            'x-rapidapi-key': "574d25f133msh5c58c65e8a4c944p1e6b8fjsnee1da55d91cd",
            'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        data = response.text
        parsed = json.loads(data)
        if len(parsed["data"]) == 0:
            print("Data not available")
        else:
            data_dict = parsed["data"][0]
            print()
            print("NEW CASES in", province, "on", date, "is", data_dict["confirmed_diff"])
            print("TOTAL number of cases in", province, "till", date, "is", data_dict["confirmed"])
            print("ACTIVE number of cases in", province, "on,", date, "is", data_dict["active"])
            print("Number of DEATHS recored in", province, "on", date, "is", data_dict["deaths_diff"])
            print("Number of RECOVERIES recorded in", province, "on", date, "is", data_dict["recovered_diff"])

    else:
        print("You have entered an invalid date. Kindly enter a valid date")
        date = input("Enter the date (yyyy-mm-dd) you would like to search for: ")
        querystring = {"date":date,"iso":ISO,"region_province":province}

        headers = {
            'x-rapidapi-key': "574d25f133msh5c58c65e8a4c944p1e6b8fjsnee1da55d91cd",
            'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        data = response.text
        parsed = json.loads(data)
        if len(parsed["data"]) == 0:
            print("Data not available")
        else:
            data_dict = parsed["data"][0]
            print()
            print("NEW CASES in", province, "on", date, "is", data_dict["confirmed_diff"])
            print("TOTAL number of cases in", province, "till", date, "is", data_dict["confirmed"])
            print("ACTIVE number of cases in", province, "on,", date, "is", data_dict["active"])
            print("Number of DEATHS recored in", province, "on", date, "is", data_dict["deaths_diff"])
            print("Number of RECOVERIES recorded in", province, "on", date, "is", data_dict["recovered_diff"])


