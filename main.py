import json
import logging
import os
import requests

from datetime import datetime
from nanoleaf_updater import update_effect

from apscheduler.schedulers.blocking import BlockingScheduler

def effects_path():
    return "./Effects.txt"

def last_issue_time_path():
    return "./support/last_issue_time.txt"

def last_issue_number_path():
    return "./support/last_issue_number.txt"

def get_effects():
    path = effects_path()
    if not os.path.exists(path):
        return None

    file = open(path, "r")
    return file.readline()

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
    logging.info("process_light_issue")
    issue_title = issue["title"]
    components = issue_title.split("|")
    if len(components) is not 3:
        logging.error("Incorrect number of components")
        return

    light_update_type = components[1]
    if light_update_type == "Effect":
        light_effect_name = components[2]

        if light_effect_name not in get_effects():
            notify("Dorm Room Client", "Unknown Effect: " + light_effect_name)
            logging.error("Unknown Effect: " + light_effect_name)
        else:
            update_effect(light_effect_name)
            logging.info("Updated Effect: " + light_effect_name)
            notify("Dorm Room Client", "Updated Effect: " + light_effect_name)

        successfully_processed_issue(issue)
    else:
        logging.error("Unknown Light Effect")

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

def check_issues():
    logging.info("Checking issues...")
    url = "https://api.github.com/repos/AndrewDorm/Public/issues"
    last_issue_time = get_last_issue_time()
    if last_issue_time:
        url += '?since=' + get_last_issue_time()

    response = requests.get(url, timeout=10)
    response_json = response.json()

    if len(response_json) > 0:
        issue = response_json[0]
        issue_title = issue["title"]
        issue_number = issue["number"]

        last_issue_number = get_last_issue_number()
        if last_issue_number and int(last_issue_number) is issue_number:
            logging.warning("Already processed last issue")
            return

        logging.info("Processing issue: " + str(issue_number))

        components = issue_title.split("|")
        if components[0] == "LightUpdate":
            process_light_issue(issue)
        else:
            logging.error("Unknown issue type: " + str(components[0]))

if __name__ == '__main__':
    support_directory = "./support"
    if not os.path.exists(support_directory):
        os.makedirs(support_directory)

    logging.basicConfig(filename='support/output.log', level=logging.DEBUG)

    # check_issues()
    scheduler = BlockingScheduler()
    scheduler.add_job(check_issues, 'interval', seconds=15)
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
