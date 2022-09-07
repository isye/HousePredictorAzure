# Overview

In this project, CI/CD is built for Boston house price predictor. The machine learning model as in [this udacity repository](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/tree/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn).
This document describes:
1. The project plan in trello and spreadsheet
2. Architectural diagram
3. Clone the github repository in azure cloud shell
4. Create and activate the azure webapp
5. Create a CI/CD pipeline in azure

## Project Plan

* A Trello board for the project is available in [here](https://trello.com/b/H2mm9fFZ/iaproject6)


* A link to a spreadsheet is [here](https://docs.google.com/spreadsheets/d/1W1Klxw6skLYuTXelZlfwf3atL4qEqZfJKpQLq5uDQoQ/edit?usp=sharing)

## Instructions

#### Architectural Diagram (Shows how key parts of the system work)
![image](https://user-images.githubusercontent.com/6762596/188955851-6f6c3a36-f683-495a-83e0-7fd44ecde82f.png)


### Instructions for running the Python project on Azure App Service

#### Project cloned into Azure Cloud Shell

**1. First, create github repository with scaffolding code (simple code with test, makefile and requirements.txt to install flas, pytest and pylint). Test using github action**

![image](https://user-images.githubusercontent.com/6762596/188678474-25bfba53-818b-4091-a21d-7fac77bc1a64.png)

![image](https://user-images.githubusercontent.com/6762596/188678614-71025444-a7c5-4aae-bc0d-c76e7555228f.png)

**2. Login to azure cloud shell, generate ssh key**

![image](https://user-images.githubusercontent.com/6762596/188676218-ffb4b4ef-11e0-40ab-bb4a-abcc82756c5a.png)

**3. Put the ssh key in github repo**

![image](https://user-images.githubusercontent.com/6762596/188676505-25795be5-b4a9-4fc2-91e3-ebc45085d04d.png)

**4. Connect to github actions, and generate github actions badge**

[![Actions Status](https://github.com/isye/HousePredictorAzure/workflows/Python%20application%20test%20with%20Github%20Actions/badge.svg)](https://github.com/isye/HousePredictorAzure/actions)

**5. Clone the github repo in Azure Cloud Shell**
![image](https://user-images.githubusercontent.com/6762596/188676779-8085a878-5643-4e15-a795-3483150d2752.png)

### Deploy to azure webapp 
**1. Run Makefile to install the requirement, test, lint. Create and deploy azure webapp** 
![image](https://user-images.githubusercontent.com/6762596/188957496-b6306428-c8da-4e65-a4ae-5107469ab429.png)

![image](https://user-images.githubusercontent.com/6762596/188957629-42f2cbde-f0bc-49a7-8216-eb02019f64f5.png)

**2. Check in browser the web app is running**
![image](https://user-images.githubusercontent.com/6762596/188957852-7032c396-a838-4202-9611-5ec76729ffdf.png)

**3. Test to call the prediction API**
![image](https://user-images.githubusercontent.com/6762596/188958124-28edef47-ff3f-4381-8973-19a595e730dc.png)

#### Successful deploy of the project in Azure Pipelines.

**1. Create devops project.** 

![image](https://user-images.githubusercontent.com/6762596/188680250-1107026c-1463-42a0-9b7f-dd096209186e.png)

**2. Create service connection**

![image](https://user-images.githubusercontent.com/6762596/188680536-c2be4243-4e1b-4d49-8fbd-527608ff2418.png)

**3. Create Pipeline**

![image](https://user-images.githubusercontent.com/6762596/188680753-52f45a30-bca7-4ba8-b938-471e4da5820a.png)

#### Running Azure App Service from Azure Pipelines automatic deployment

![image](https://user-images.githubusercontent.com/6762596/188680912-afebf0c2-0597-475f-8fd8-b1d4f3640860.png)

![image](https://user-images.githubusercontent.com/6762596/188681019-23df7dc3-fad5-4e35-93b3-16866a859305.png)


## Enhancements

**Planning to improve the project:**
1. In current project, the machine learning predict the house price in Boston city. In the future, the project can be developed for another city in US or worldwide
2. Current project limited to python3.7. In the future it can be developed with newer Python version so we can use newer machine learning packages.
3. The deployment may use docker.
4. Develop web and application to use the current api.


## Demo 
https://youtu.be/EMR2yrgqwQs
