# Overview

In this project, CI/CD is built for Boston house price predictor. The machine learning model as in this repository:
https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/tree/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn   

## Project Plan

* A Trello board for the project is available in: https://trello.com/b/H2mm9fFZ/iaproject6
https://trello.com/invite/b/H2mm9fFZ/b726975f6ff339c83baacbb7da10e779/iaproject6

* A link to a spreadsheet link: 
https://docs.google.com/spreadsheets/d/1W1Klxw6skLYuTXelZlfwf3atL4qEqZfJKpQLq5uDQoQ/edit?usp=sharing

## Instructions

* Architectural Diagram (Shows how key parts of the system work)
![image](https://user-images.githubusercontent.com/6762596/188674403-653ec27f-cd98-411b-8004-d673b141780e.png)

Instructions for running the Python project on Azure App Service

* Project cloned into Azure Cloud Shell
1. First, create github repository with scaffolding code (simple code with test, makefile and requirements.txt to install flas, pytest and pylint). Test using github action
![image](https://user-images.githubusercontent.com/6762596/188678474-25bfba53-818b-4091-a21d-7fac77bc1a64.png)
![image](https://user-images.githubusercontent.com/6762596/188678614-71025444-a7c5-4aae-bc0d-c76e7555228f.png)

2. Login to azure cloud shell, generate ssh key
![image](https://user-images.githubusercontent.com/6762596/188676218-ffb4b4ef-11e0-40ab-bb4a-abcc82756c5a.png)

3. Put the ssh key in github repo
![image](https://user-images.githubusercontent.com/6762596/188676505-25795be5-b4a9-4fc2-91e3-ebc45085d04d.png)

4. Clone the github repo in Azure Cloud Shell
![image](https://user-images.githubusercontent.com/6762596/188676779-8085a878-5643-4e15-a795-3483150d2752.png)

* Passing tests that are displayed after running the `make all` command from the `Makefile`
Run makefile
in local:
![image](https://user-images.githubusercontent.com/6762596/188678234-4c7a657b-a74b-461f-9d83-b47d512653f8.png)
in azure cloud shell:
![image](https://user-images.githubusercontent.com/6762596/188677624-4b807bc3-7d59-40d0-8b2c-adcdcfe7711d.png)

* Install web app and run the web app:
1. Install web app in Azure Cloud Shell
![image](https://user-images.githubusercontent.com/6762596/188678877-5aa6cbd0-7485-4784-a899-3c7e6a6c58d5.png)

2. Check in browser the web app is running
![image](https://user-images.githubusercontent.com/6762596/188679049-5a76fa4d-d8f4-484f-aff4-7118205916b1.png)

3. Test to call the prediction API
![image](https://user-images.githubusercontent.com/6762596/188679428-cb765311-81ed-488f-8441-2095fdb0f583.png)

* Successful deploy of the project in Azure Pipelines.
1. Create devops project. 
![image](https://user-images.githubusercontent.com/6762596/188680250-1107026c-1463-42a0-9b7f-dd096209186e.png)

2. Create service connection
![image](https://user-images.githubusercontent.com/6762596/188680536-c2be4243-4e1b-4d49-8fbd-527608ff2418.png)

3. Create Pipeline
![image](https://user-images.githubusercontent.com/6762596/188680753-52f45a30-bca7-4ba8-b938-471e4da5820a.png)

* Running Azure App Service from Azure Pipelines automatic deployment
![image](https://user-images.githubusercontent.com/6762596/188680912-afebf0c2-0597-475f-8fd8-b1d4f3640860.png)
![image](https://user-images.githubusercontent.com/6762596/188681019-23df7dc3-fad5-4e35-93b3-16866a859305.png)

* Successful prediction from deployed flask app in Azure Cloud Shell.  
![image](https://user-images.githubusercontent.com/6762596/188681999-4e1383d9-bf80-4497-962b-49104b4dc86a.png)

* Output of streamed log files from deployed application
![image](https://user-images.githubusercontent.com/6762596/188683141-54cd2eb0-de26-4c20-8d9a-e11632f173d0.png)



## Enhancements

Improvement can be made by using docker or kubernetes for this project.

## Demo 

<TODO: Add link Screencast on YouTube>

