import json
import logging
import os
import requests

import support

from datetime import datetime
from nanoleaf_effect_updater import update_effect

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

def successfully_processed_issue(issue):
    file = open(support.last_issue_time_path(),"w")
    file.write(issue["created_at"])
    file.close()

    file = open(support.last_issue_number_path(),"w")
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
        actual_effect_name = None

        for effect in support.get_all_effect_names():
            if effect.lower() == light_effect_name.lower():
                actual_effect_name = effect
                break

        if not actual_effect_name or actual_effect_name not in support.get_all_effect_names():
            notify("Dorm Room Client", "Unknown Effect: " + light_effect_name)
            logging.error("Unknown Effect: " + light_effect_name)
        else:
            update_effect(actual_effect_name)
            logging.info("Updated Effect: " + actual_effect_name)
            notify("Dorm Room Client", "Updated Effect: " + actual_effect_name)

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
    last_issue_time = support.get_last_issue_time()
    if last_issue_time:
        url += '?since=' + support.get_last_issue_time()

    response = requests.get(url, timeout=10)
    response_json = response.json()

    if len(response_json) > 0:
        issue = response_json[0]
        issue_title = issue["title"]
        issue_number = issue["number"]

        last_issue_number = support.get_last_issue_number()
        if last_issue_number and int(last_issue_number) is issue_number:
            logging.info("Already processed last issue")
            return

        logging.info("Processing issue: " + str(issue_number))

        components = issue_title.split("|")
        if components[0] == "LightUpdate":
            process_light_issue(issue)
        else:
            logging.error("Unknown issue type: " + str(components[0]))

if __name__ == '__main__':
    support.prepare_directory()

    log_file = support.directory() + "output.log"

    logging.basicConfig(filename=log_file, level=logging.INFO)

    # check_issues()
    scheduler = BlockingScheduler()
    trigger = IntervalTrigger(seconds=15)
    scheduler.add_job(check_issues, trigger)
    try:
        notify("Dorm Room Client", "Started")
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        notify("Dorm Room Client", "Killed")
        pass
