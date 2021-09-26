# Stock Price Profit Calculator

**Author:** Syed Adnan

**Email:** dani.syed@gmail.com

**Web:** [www.SyedAdnan.com](https://syedadnan.com)

<p align="center">
<img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png" width="150px">   

<img src="https://www.docker.com/sites/default/files/social/docker_facebook_share.png" width="150px">   

<img src="https://blog.iron.io/wp-content/uploads/2019/04/Google-Cloud-Run.jpg" width="150px">

</p>

<p align="center">
<a href="https://travis-ci.org/laravel/framework"><img src="https://travis-ci.org/laravel/framework.svg" alt="Build Status"></a>
</p>

## Intro

This demo application is written in Python3, takes an array of stock prices and returns the best profit you could have made from 1 purchase and 1 sale of 1 Financial stock from yesterday. There are few other requirements as well that are included in the logic. Main requirements are you must buy before you sell. Also you may not buy and sell in the same time step (at least 1 minute must pass).


## Tech Stack

Following tech stack has been used to develop this application:

- **Python 3.7** 
- **PyTest for Unit Testing** 
- **Docker Containers** 
- **GitHub Workflow** 
- **CloudBuild for CI/CD Pipeline** 
- **Google Artifact Registory for Container Builds** 
- **Cloud Run for Serverless Architecture** 


## Steps to install / Run the application

- *Clone the code from GitHub*
- *Install the dependencies using pip install -r requirements.txt*
- *Build using Docker build command*
- *Docker file will use the python3 image*
- *Configure the service accounts & Permissions over Google Cloud*
- *Configure CloudBuild to listen to any commit in the GitHub repo*
- *UnitTests will be executed before pushing the container build*
- *Ci/CD pipeline will automatically build the container and push it to GCR*
- *This container will be deployed to Google serverless architecture called Cloud Run* 


## Unit/Feature Testing with PyTest

You can run the following unit tests in this application:

- *test_integer_return: Will test if function will return profit in integer*
- *test_empty_list - Will test output by providing empty list*
- *test_int_list - Will test the output if stock price is string*
- *test_profit_random - Will test a random list of stock prices*
- *test_loss - Will test the list having a loss*
- *test_max_profit - Will test the set with maximum profit*
- *test_zero_profit - Will test where all stock prices are same*
- *test_indiv_function - Will test the individual function for int validation*

<img src="https://ibb.co/GkbVj19" width="650">

*Steps to run UnitTests:* Follow the below steps to execute the unit tests:

- **pytest -v test.py** *[Use this to run all of the test cases]*
- **pytest -v test.py::test_integer_return** *[Use this to run a particular function]*

## GitHub Branch Protection

I am using GitHub branch permission rules, so that this branch is protected. You need to create a pull request before pusing any changes in the codebase.

## CI/CD Pipeline

CI/CD pipeline for automated deployment is written in CloudBuild (A managed service from Google Cloud Platform). This CloudBuild trigger will be configured in GCP console, by providing the Github repo/branch and a trigger. This trigger will be listening to any change in the code resulting by code merge to a particular branch. 

Once the code is merged, Pipeline will be triggered automatically and do the following steps:

- *Install all the dependencies*
- *Perform the unit tests - SendGrid can be configured to notify if unitTests are failed*
- *After passing all the unit tests, Docker container will be build and tagged*
- *This docker container will be pushed to Google Artifact Registory*
- *This container will be deployed on a serverless architecture called Cloud Run*




