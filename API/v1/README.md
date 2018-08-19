#StackOverFlow-Lite- API
This is a simple flask API that has provisions for viewing all questions, selecting a particular question, creating a question and also answering an available question.question

#API Breakdown:
The api users can:

View all the questions

View a particular question based on the uri(id)

Add a question

Answer a particular question


#Guide:
Users can either clone from github using git or download a zipped folder:

Downloading
Download the zipped file of this repository branch. Extract and go to the v1 directory. Run app.py from its root directory in terminal or favourite editor (PyCharm, Atom, Vscode)

Cloning
Open git and issue this command:

$ git clone https://github.com/matokefred/StackOverflow-Lite.git

Locate the StackOverflow-lite folder in your pc.

Navigate the App/v1 folder and run app.py in terminal or favourite editor (PyCharm, Atom, Vscode)

#Deployment steps
To use this api:

Ensure to copy the cURL.exe file in the directory with the app.py file. Otherwise, use Postman to issues requests and obtain responses.
 
(python app.py) - in the OS or editor terminal to open the server on which the api will 'sit'

On a new terminal window, access the api:

#To view all the questions: 

curl -i http://localhost:5000/questions

#To view a specific question: 

curl -i http://localhost:5000/questions/<uri>

# To post a question: 

curl -i -H "Content-Type: application/json" -X POST -d "{"""category""": """sports""", """content""": """Who is the best player in the world"""}" http://localhost:5000/questions

# To answer a question:

curl -i -H "Content-Type: application/json" -X POST -d "{"""answer""": """Modelling computers to make decisions independently"""}" http://localhost:5000/questions/3/answers

# To delete a question

curl -i -X DELETE http://localhost:5000/questions/1

#Development tools
Flask (server side configuration)

Travis CI (Continuous Integration)

Git (Version Control)

Pivotal Tracker (Agile Project Management)

To make any contributions:
On github, fork the repository. Either clone or download the repository to your local computer,for cloning on git:

$ git clone https://github.com/matokefred/StackOverflow-Lite.git

$ cd StackOverflow-Lite

$ git fetch --all

$ git pull --all

#Current Travis CI Status because of a failed test
[![Build Status](https://travis-ci.org/matokefred/StackOverFlow-Lite.svg?branch=api)](https://travis-ci.org/matokefred/StackOverFlow-Lite)

#The relative code coverage
[![Coverage Status](https://coveralls.io/repos/github/matokefred/StackOverFlow-Lite/badge.svg?branch=master)](https://coveralls.io/github/matokefred/StackOverFlow-Lite?branch=master)

#Special thanks

Andela Bootcamp Preparation - cohort 31