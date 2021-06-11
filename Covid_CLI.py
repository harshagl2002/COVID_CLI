from plumbum import cli 
from pyfiglet import Figlet
from questionary import prompt
from termcolor import colored
import questionary
import Covid_News
import Country_CovidTracker
import Province_CovidTracker
import World_CovidTracker
import World_CovidGraph
import Country_CovidGraph
import Province_CovidGraph


def print_banner(text: str):
    print(colored(Figlet(font='starwars').renderText(text), 'yellow'))


class FancyGitAdd(cli.Application):
    VERSION = "1.3"

    def main(self):
        print_banner("COVID UPDATES")

        files = ['Get the latest Covid-19 related news', 'Get Covid-19 related updates about a specific country', 'Get Covid-19 related updates about a specific province/state/region',
         'Get worldwide updates related to Covid-19']
        
        ask = True
        while ask:

            question = questionary.select("What would you like to search for ?", choices=files).ask()
        
            if question == files[0]:
                Covid_News.news()
            elif question == files[1]:
                Country_CovidTracker.country()
                print()
                graph_question = questionary.confirm("Would you like to check the graph showing the number of Covid-19 cases world wide? (Kindly allow roughly 10 minutes for the graph to be processed)").ask()
                if graph_question == True:
                    print()
                    Country_CovidGraph.country_graph()
            elif question == files[2]:
                Province_CovidTracker.province()
                print()
                graph_question = questionary.confirm("Would you like to check the graph showing the number of Covid-19 in a province? (Kindly allow roughly 10 minutes for the graph to be processed)").ask()
                if graph_question == True:
                    print()
                    Province_CovidGraph.province_graph()
            else:
                World_CovidTracker.world()
                print()
                graph_question = questionary.confirm("Would you like to check the graph showing the number of Covid-19 cases worldwide? (Kindly allow roughly 10 minutes for the graph to be processed)").ask()
                if graph_question == True:
                    print()
                    World_CovidGraph.world_graph()
            
            print()
            continue_question = questionary.confirm("Would you like to go back to the main menu ?").ask()
            if continue_question == False:
                ask = False
            
            print()




if __name__ == "__main__":
    FancyGitAdd()