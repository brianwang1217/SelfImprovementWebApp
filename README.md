# Send Me Junk: CS 196 Honors Project

## Members
Shreyas Mohan, David Wang, Brain Wang, Ruiyi Wang, Alex Szymanski, Alex Yu.
Project Managers: Justin Yang and Sahil Bhatt

## What is Send Me Junk?
Send Me Junk is a Flask-based website that uses the Twilio APi, Flask Mail along with many other APIs to bring its users the information that matter most to them, while reminding them to keep up with school work and assignments etc.

## Tech Stack
HTML and CSS for Front End
Flask for Backend
Sqlite for Database

## Setup

Download virtual environment and download our requirements.txt file:

```bash
$ pip3 install virtualenv
$ virtualenv -p python3 venv
$ source venv/bin/activate
(venv)$ pip install -r requirements.txt
```

Download Sqlite from https://www.sqlite.org/ and DB Browser for Sqlite from http://sqlitebrowser.org/ (a GUI to look at schema and data in the database"

## How to Run

After this, you are all set to run and start using our application!
Simply

```bash
$ cd Backend/
$ python run.py
```

And it will load the website in a localhost.

## Testing Backend

    GET /test/backend
At this endpoint you can test the email and sms functions with different messages.
