import json
import os
import requests

from datetime import datetime

def last_issue_time_path():
    return "./support/last_issue_time.txt"

def last_issue_number_path():
    return "./support/last_issue_number.txt"

def get_last_issue_time():
    path = last_issue_time_path()
    if not os.path.exists(path):
        return None

    file = open(path, "r")
    return file.readline()

def get_last_issue_number():
    path = last_issue_number_path()
    if not os.path.exists(path):
        return None

    file = open(path, "r")
    return file.readline()

def successfully_processed_issue(issue):
    file = open(last_issue_time_path(),"w")
    file.write(issue["created_at"])
    file.close()

    file = open(last_issue_number_path(),"w")
    file.write(str(issue["number"]))
    file.close()

def process_light_issue(issue):
    # if len(components) is not 3:
    #     print("Inccorrect number of components")
    #     return


    successfully_processed_issue(issue)

def check_issues():
    url = "https://api.github.com/repos/AndrewButtonChecker/Button/issues"
    last_issue_time = get_last_issue_time()
    if last_issue_time:
        url += '?since=' + get_last_issue_time()

    response = requests.get(url, timeout=10)
    response_json = response.json()

    if len(response_json) > 0:
        issue = response_json[0]
        issue_title = issue["title"]
        issue_number = issue["number"]

        last_issue_number = int(get_last_issue_number())
        if last_issue_number and last_issue_number is issue_number:
            print("Already processed last issue")
            # return

        print("Processing issue: " + str(issue_number))

        components = issue_title.split("|")
        if components[0] == "LightUpdate":
            process_light_issue(issue)
        else:
            print("Unknown issue type: " + str(components[0]))
            
if __name__ == '__main__':
    support_directory = "./support"
    if not os.path.exists(support_directory):
        os.makedirs(support_directory)

    check_issues()
