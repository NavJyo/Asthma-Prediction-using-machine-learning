Chronic Kidney Disease Prediction:

Table of Content

Demo
Overview
Motivation
Installation
Deployement on Heroku
Directory Tree
Bug / Feature Request
Demo

Link: https://stinkyasthma.herokuapp.com

Asthma

Overview

This is a simple Flask web app which predicts whether a patient is having asthma or not.

Motivation

With the amount of new diseases coming up every day, there is a need for an effective method to diagnose diseases. This was one of the disease prediction used for my B.tech major project.

Installation

The Code is written in Python 3.6.10. If you don't have Python installed you can find it here . If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after cloning the repository:

pip install -r requirements.txt

Deployement on Heroku

Login or signup in order to create virtual app. You can either connect your github profile or download ctl to manually deploy this project. Our next step would be to follow the instruction given on Heroku Documentation to deploy a web app.

Directory Tree

├── static

│ ├── css

├── template

│ ├── kidney.html

├── Procfile

├── README.md

├── app.py

├── kidney.pkl

├── requirements.txt

Bug / Feature Request If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue here by including your search query and the expected result

Technologies Used

![flask1](https://user-images.githubusercontent.com/36689965/117607201-17991680-b179-11eb-9f93-ae1b813809f6.jpg)
![python](https://user-images.githubusercontent.com/36689965/117607228-297ab980-b179-11eb-9fd4-2f05d44d7e3a.jpg)
![sklearn](https://user-images.githubusercontent.com/36689965/117607239-2da6d700-b179-11eb-819b-812dfa8defe4.png)
![heroku](https://user-images.githubusercontent.com/36689965/117607250-339cb800-b179-11eb-9f11-f2e11772313e.png)
