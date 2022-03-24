
# VTH-Hacks

![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-3670A0?style=for-the-badge&logo=flask&logoColor=ffdd54)


## What is Applytics ?

Applytics is an open-source web application bridging the gap between Users and Developers. Applytics is responsible for automatically matching Patch notes with the Bug reports reported by the Users. Often User finds it difficult to solve an issue and at times their issues remain unsolved. Developers on the other hand spend approximately about 42% of their time trying to solve bugs. Our goal is to notify the developers of the issues that are important but unsolved. Furthermore, we wish to apply this app as a tool to the pre-existing software Jira which is a proprietary issue tracking product developed by Atlassian that allows bug tracking and agile project management.

## Features:

- Applytics provides two different types of account: 
(i) General account :  General account users on log in/ sign up are sent to an analytics page where they could choose the app of their liking to explore its advanced analytics.
(ii) Developer account: Developer account users can log in/ sign up with their company email ex: zeeshan@slack.com and our code will smartly direct the user to the user's app analytics page, in this case Slack.

- Both accounts can view visual data analytics of the App which depicts various statistics like: sentiment distribution, bug topics distribution etc.

- Developer accounts have access to the Reviews Analyzer Page which segregate all negative reviews in the major bug topic clusters identified with LDA topic modeling

- Developer accounts have access to the Bug Tracker Page which maps negative reviews to patch notes to keep track of bugs fixed and unattended.

## Challenges we ran into:
We ran into multiple challenges along with the development phase and were dealt with accordingly. For Front-End we had challenges with aligning placeholders that were used to display the results from our Machine Learning model. For Back-End we ran into time-bounded challenges as the Machine learning model takes a considerable amount of time to create the tensor file of our embeddings. Employing a Machine Learning model also posed challenges as the packages to be downloaded were conflicting with existing packages, resolving dependencies also required a lot of time dedication. Our API choice was another thing we struggled with as we wanted to ensure we were using the best and more reliable technologies for development and debugging.

## What we learnt:

Hackathons are a great way to meet new people, network with industry professionals, learn new things, flex your problem-solving muscles, and maybe even win some great prizes.
VTHacks IX presented us with the opportunity to work on a real-life problem that is highly complex yet often overlooked in the Software Development Community.
Several Apps on App Stores, such as Google Play or the Apple Store, allow users to provide constructive or positive feedback on apps by posting their personalized reviews.
From our research, it has been clear that users reviews include bug reports, feature requests, that can assist app developers to accomplish software maintenance and evolution tasks. According to several statistics, it has been proven that several important bugs and technical issues with the advancing technology are often not noticed by the developers. This is when we decided to create a web application that helps solve this cause.

## Plans for the Future:
-We wish to apply this app as a tool to the pre-existing software Jira which is a proprietary issue tracking product developed by Atlassian that allows bug tracking and agile    project management. 


## Technologies Used:

| Stack     | Technologies Used                    |
|-----------|--------------------------------------|
| Front-End | React , HTML, JavaScript, CSS        |
| Back-End  | Python, Flask                        |
| Database  | MySQL                                | 
| Machine Learning | JupyterNotebook               |


## Machine Learning :

| Technique           | Purpose                                        |
|---------------------|------------------------------------------------|
| LDA Topic Modelling | Clustering the Data (Unsupervised Learning)    |
| Specter Model       | Generating Tensor Embeddings for textual data  |


## API's used :


| API           | Purpose                                       |
|---------------------|-----------------------------------------|
| Google_play_scraper | Scrapping App Reviews from Play Store   |
| App Annie           | Scrapping App Patch/Release Notes       |


## Project Technologies Flowcharts

![first](https://user-images.githubusercontent.com/72998580/155883978-25f92a35-610a-4e4d-84dd-fb22f2f1318a.PNG)
![second](https://user-images.githubusercontent.com/72998580/155883545-59c8c457-e894-4764-98e2-c25ee2aa4c36.PNG)

## Interface 

![image](https://user-images.githubusercontent.com/72998580/155882015-385be487-e1a7-4005-9311-20961883cfc7.png)
![image](https://user-images.githubusercontent.com/72998580/155882148-8265c4d1-8077-4bc6-a692-c679e210a1f5.png)
![image](https://user-images.githubusercontent.com/72998580/155882215-ed344b5f-92f8-4177-9af6-c94ad9062daa.png)
![image](https://user-images.githubusercontent.com/72998580/155881825-adcf9e02-d962-4515-a060-0a662e9d63cd.png)
![image](https://user-images.githubusercontent.com/72998580/155881970-86d2b66a-fa43-45c1-a6fd-de39966e1822.png)

  
## ML model integration
- The reviews gathered from the Google-Scrapper API were clustered into groups of major bugs detected. This was done using LDA Topic Modelling.
- These Major Bugs are mapped to reviews using SPECTRE.
- SPECTRE model in Applytics is built using allenai-specter model with SentenceTransformers.
- Patch Notes and Negative Reviews are generated using the App Annie API and then passed these notes to the Spectre model to create embeddings.
- Proceeding to perform Cosine-Similarity to map patches to reviews and display results on Flask.
  
## Prequisites to run the ML Model
```
pip install regex
pip install torch
pip install pickle5
pip install sentence-transformers
pip install pandas
pip install neattext
pip install transformers requests beautifulsoup4 pandas numpy
```
## License
