import requests
import json
import datetime

def country():
    url = "https://covid-193.p.rapidapi.com/history"


    country = input("Enter the country you would like to search for: ")
    date = input("Enter the date (yyyy-mm-dd) you would like to search for: ")

    year,month,day = date.split('-')

    isValidDate = True
    try :
        datetime.datetime(int(year),int(month),int(day))
    except ValueError :
        isValidDate = False

    if(isValidDate) :

        querystring = {"country":country,"day":date}

        headers = {
            'x-rapidapi-key': "574d25f133msh5c58c65e8a4c944p1e6b8fjsnee1da55d91cd",
            'x-rapidapi-host': "covid-193.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.text
        parsed = json.loads(data)
        if parsed["results"] == 0:
            print("The requested data is currently not availible. Sorry")
        else:
            response_dict = parsed["response"][0]
            cases_dict = response_dict["cases"]
            print()
            print("NEW CASES in", parsed["parameters"]["country"], "on", response_dict["day"], "is", cases_dict["new"])
            print("TOTAL number of cases in", parsed["parameters"]["country"], "till", response_dict["day"], "is", cases_dict["total"])
            print("ACTIVE CASES in", parsed["parameters"]["country"], "on", response_dict["day"], "is", cases_dict["active"])
            print("Number of DEATHS recorded in", parsed["parameters"]["country"], "on", response_dict["day"], "is", response_dict["deaths"]["new"])
            print("Number of RECOVERIES recorded in", parsed["parameters"]["country"], "till", response_dict["day"], "is", cases_dict["recovered"])
            print("Total number of TESTS conducted in", parsed["parameters"]["country"], "till", response_dict["day"], "is", response_dict["tests"]["total"])

    else:
        print("You have entered an invalid date. Kindly enter a valid date")
        date_new = input("Enter the date (yyyy-mm-dd) you would like to search for: ")
        querystring = {"country":country,"day":date_new}

        headers = {
            'x-rapidapi-key': "574d25f133msh5c58c65e8a4c944p1e6b8fjsnee1da55d91cd",
            'x-rapidapi-host': "covid-193.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.text
        parsed = json.loads(data)
        if parsed["results"] == 0:
            print("The requested data is currently not availible. Sorry")
        else:
            response_dict = parsed["response"][0]
            cases_dict = response_dict["cases"]
            print()
            print("NEW CASES in", parsed["parameters"]["country"], "on", response_dict["day"], "is", cases_dict["new"])
            print("TOTAL number of cases in", parsed["parameters"]["country"], "till", response_dict["day"], "is", cases_dict["total"])
            print("ACTIVE CASES in", parsed["parameters"]["country"], "on", response_dict["day"], "is", cases_dict["active"])
            print("Number of DEATHS recorded in", parsed["parameters"]["country"], "on", response_dict["day"], "is", response_dict["deaths"]["new"])
            print("Number of RECOVERIES recorded in", parsed["parameters"]["country"], "till", response_dict["day"], "is", cases_dict["recovered"])
            print("Total number of TESTS conducted in", parsed["parameters"]["country"], "till", response_dict["day"], "is", response_dict["tests"]["total"])
