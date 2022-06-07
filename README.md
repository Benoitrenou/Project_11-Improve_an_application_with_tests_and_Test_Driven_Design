In the scenario of this project, an application developed for the company Güdlft with the framework Flask contains some bugs that must be corrected in a first step.

Then, in a second step, a series of tests must be built and the application eventually corrected according to these tests.

Must be created:
  - unitary tests
  - integration tests
  - fonctionals tests
  - performace tests

the evolution of the application code during the different stages can be followed via the different branches of the repository

Objectives of the project:
  - Identify bugs sources and correct them
  - Discover tests and theirs tools: Pytest, unittest, Selenium, Locust
  - Applicate Test Driven Design

Follow instructions below in order to launch the application.

## Create virtual environment

From your terminal, enter the following commands depending on your operating system

### With Linux/ MAC OS

    $ python -m venv <environment_name>
    example : python -m venv envP11
    
### With Windows:
    
    $ virtualenv <environment_name>
    example : virtualenv envP11 
    
## Activate virtual environment

### With Linux / MAC OS:

    $ source <environment_name>/bin/activate
    example : source envP11/bin/activate
   
### With Windows:

    $ source <environment_name>/Scripts/activate
    example : source envP11/Scripts/activate
    
## Installation of packages : 

    $ pip install -r requirements.txt

## Launch application

Flask asks you to define a python file as environment variable. You must define the file <code>server.py</code> as this file.

Follow the instructions given via [this link](https://flask.palletsprojects.com/en/2.0.x/quickstart/) for more details.

Then from the directory Python_Testing, launch application with the command:

    $ flask run

## Tests

To run all the tests, open a second terminal and run from the Python_Testing directory :

    $ pytest

To check and report on test coverage, complete the pytest command:

    $ pytest --cov=. --cov-report html

To start a performance test session, go to the Python_Testing/tests/performance_tests directory and run the following command:

    $ locust

The data from these tests are also available in the data_tests directory.