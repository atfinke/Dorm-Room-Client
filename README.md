# Dorm Room

Enabled anyone to adjust and set my Nanoleaf Aurora lights on my dorm room window from outside by going to the website.
Super inspired by the [Panic Sign](https://sign.panic.com).

**Video of early light setup**<br>
[![Dorm Room - Lights](https://img.youtube.com/vi/e6EfWWHYnic/0.jpg)](https://www.youtube.com/watch?v=e6EfWWHYnic)

1. [Dorm Room Server](https://github.com/atfinke/Dorm-Room-Server): Runs on Google App Engine. Generates the public website based on the published effects in the client repo. Then creates issues in the dorm repo when lights should update.
2. [Dorm Room Client](https://github.com/atfinke/Dorm-Room-Client): Runs on local iMac. Checks for new issues in the dorm repo and updates lights accordingly.
3. [Dorm Public](https://github.com/AndrewDorm/Public): Repo used to track light updates. Yes, I used GitHub issues as a free database service. Yes, I'm a little crazy, why do you ask?
