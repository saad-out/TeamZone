# TeamZone - The Ultimate Platform for Local Teams

<p align="center">
  <img src="https://github.com/saad-out/TeamZone/blob/main/web/static/images/app_logo.png" style="height: 250px; width:300px;"/>
</p>

## About 

Have you ever found yourself struggling to organize a sports game with your team? Maybe you were looking for new opponents but didn't know where to start. Or perhaps you've just moved to a new city and are having trouble finding a team to join. Whatever your situation may be, TeamZone is here to help.

TeamZone is a web application designed to connect local sports teams and make organizing games a breeze. Whether you're a casual player or a team manager, TeamZone has everything you need to get started. You can search and filter teams based on sport, country, city, and more, and even create your own teams and add other users as teammates. With TeamZone, finding and scheduling games has never been easier.

TeamZone offers a user-friendly platform for keeping track of your teams and communicating with other teams as well. Once you find a suitable team to play against, you can send them a game invitation with the date and time specified. The other team will receive the invitation and can accept or decline it based on their availability. TeamZone streamlines the process of scheduling games with other local teams.

So if you're tired of playing the same old opponents or struggling to find a team to join, give TeamZone a try. It's the ultimate platform for local sports teams, and it's sure to take your game to the next level.

<p align="center">
  <img src="https://github.com/saad-out/TeamZone/blob/main/web/static/images/landing.png" style="width:80%;"/>
</p>

## Features and Functionality
TeamZone offers a variety of features designed to make connecting and organizing games between local sports teams easier than ever. Here are just a few of the key features:

### Team Search and Filtering
TeamZone allows users to search and filter teams based on a variety of criteria, including sport, country, city, and more. This makes it easy to find local teams that match your preferences and interests.
<p align="center">
  <img src="https://github.com/saad-out/TeamZone/blob/main/web/static/images/search.png" style="width:50%;"/>
</p>

### Team Creation and Player Management
Users can create their own teams and add other users as players to their teams. This allows team managers to quickly and easily organize games with other local teams.
<p align="center">
  <img src="https://github.com/saad-out/TeamZone/blob/main/web/static/images/create.png" style="width:50%;"/>
</p>

### Game Invitations and RSVPs
Once a suitable team has been found, users can send game invitations with the date and time specified, along with an optional message. The other team can then RSVP to the invitation and accept or decline based on their availability.
<p align="center">
  <img src="https://github.com/saad-out/TeamZone/blob/main/web/static/images/RSVP.png" style="width:50%;"/>
</p>

### Team info
With TeamZone, users can easily manage their own teams. Each team has a profile page where users can view and edit team information and add players. Team managers can quickly organize games with other local teams, and sending team invites to other users to join their teams.
<p align="center">
  <img src="https://github.com/saad-out/TeamZone/blob/main/web/static/images/myteams.png" style="width:50%;"/>
</p>


## Technologies Used
![HTML Badge](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white) ![CSS Badge](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white) ![Bootstrap Badge](https://img.shields.io/badge/Bootstrap-563D7C?style=flat&logo=bootstrap&logoColor=white) ![Python Badge](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) ![Flask Badge](https://img.shields.io/badge/Flask-2.2.3-orange.svg) ![SQLAlchemy Badge](https://img.shields.io/badge/SQLAlchemy-red?style=flat&logo=python&logoColor=white) ![MySQL Badge](https://img.shields.io/badge/MySQL-00000F?style=flat&logo=mysql&logoColor=white) 

TeamZone is a web application built using a variety of technologies. The user interface is primarily developed using HTML and CSS, with a significant number of Bootstrap components for enhanced styling and responsive design.

The application's backend is developed using the Flask Python web framework. Flask provides a lightweight yet powerful foundation for developing web applications, allowing for rapid development and easy integration with other Python libraries.

Data storage for the application is provided by a MySQL database management system (DBMS), with the SQLAlchemy ORM providing an intuitive and flexible way to interact with the database.

Together, these technologies form a robust and reliable foundation for TeamZone, allowing for seamless integration between the frontend and backend components of the application.

## Installation and Usage Instructions

### Prerequisites
Before installing the app, please make sure you have the following prerequisites installed:

*`MySQL`*: The app requires a MySQL database to store data. If you don't have MySQL installed, you can download and install it from the official MySQL website: https://www.mysql.com/downloads/

*`Python`*: The app requires Python as it is build using *Flask Python Web Framework*. You can download and install Python from the official Python website: https://www.python.org/downloads/

### Usage
To run the app locally for testing purposes, follow these steps:
1. Clone the repository to your local machine:
  ```
  git clone https://github.com/saad-out/TeamZone.git
  ```
2. Step into the directory:
  ```
  cd TeamZone
  ```
3. Create a Python [virtual environment](https://docs.python.org/3/library/venv.html) and activate it:
  ```
  # For Unix-based Systems
  python3 -m venv venv
  source venv/bin/activate
  
  # For Windows Users
  python -m venv venv
  venv\Scripts\activate.bat
  ```
4. Install the required packages:
  ```
  pip install -r requirements.txt
  ```
5. Create the MySQL database and user by running the following command (You can customize the values in `setup_mysql_dev.sql`, *USE A STRONG PASSWORD FOR THE USER*):
  ```
  # For Unix-based Systems
  cat setup_mysql_dev.sql | sudo mysql
  
  # For Windows Users
  type setup_mysql_dev.sql | mysql -u root -p
  ```
6. Create a `.env` file in the main directory and include the values for the following variables:
  ```
  APP_KEY=<your_flask_app_secret_key>
  
  MAIL_USER=<your_app_email_username>
  MAIL_PASS=<your_app_email_password>
  
  TZ_MYSQL_USER=<your_mysql_username>
  TZ_MYSQL_PWD=<your_mysql_password>
  TZ_MYSQL_HOST=<your_mysql_host>
  TZ_MYSQL_DB=<your_mysql_database>
  
  RECAPTCHA_SITE_KEY=<your_reCAPTCHA_site_key>
  RECAPTCHA_SECRET_KEY=<your_reCAPTCHA_secret_key>
  
  API_URL=<api_url>
  ```
  Here's what each variable means:
  
  `APP_KEY`: Flask app secret key. You can generate one by running `python -c 'import os; print(os.urandom(16))'` and copying the output to the .env file.
  
  `TZ_MYSQL_USER, TZ_MYSQL_PWD, TZ_MYSQL_HOST, TZ_MYSQL_DB`: MySQL database configuration. Change these values to match your MySQL setup in `setup_mysql_dev.sql`.
  
  `MAIL_USER, MAIL_PASS`: Gmail account configuration. Create a Gmail account for the app and use its username and password for these variables to enable the forgot     password feature to work with Flask-Mail.
  
  `RECAPTCHA_SITE_KEY, RECAPTCHA_SECRET_KEY`: Google reCAPTCHA v3 configuration. Get the keys by visiting the Google reCAPTCHA Admin Console.
  
  `API_URL`: The url to the API, if you're running on the default localhost port 5001, it should be `http://localhost:5001`
  
  
7. Start the web and API servers by running the following commands separately in two different terminal windows from the main directory:
  ```
  # python3 OR python
  python3 -m web.app
  ```
  In a separate shell:
  ```
  # python3 OR python
  python3 -m api.v1.app
  ```
8. Access the web app at `http://localhost:5000` and the API at `http://localhost:5001`. The web app communicates with the API through the JavaScript code.

## Architecture

TeamZone consists of two Flask applications: a web app and an API app. The web app is responsible for rendering the user interface and handling user interactions, while the API app provides the data and functionality for the web app to interact with.

The web app, built using Flask, serves as the front-end of the application and is responsible for rendering the web pages that users interact with. It utilizes JavaScript to fetch data from the API app and dynamically populate the pages with content.

The API app, also built using Flask, serves as the back-end of the application and provides the data and functionality required by the web app. It exposes RESTful endpoints that the web app can communicate with to retrieve or modify data. The API app is designed to handle requests from the web app and provide the necessary data for the web app to render the user interface.

It's important to note that not all features of the app require authentication. Non-logged-in users still have access to the search and filter functionality, allowing them to search and filter teams and games. However, certain features such as team creation, team management, game invites, and other functionalities are only available to logged-in users who have authenticated themselves. This approach ensures that both logged-in and non-logged-in users can benefit from the app's functionalities while maintaining appropriate access controls and security measures.

<p align="center">
  <img src="https://github.com/saad-out/TeamZone/blob/main/web/static/images/Search_archi.png" style="width:80%;"/>
</p>

## Background

This project was developed as part of the ALX Software Engineering program, specifically as a portfolio project for the Foundations section of the program. The aim of this project was to apply the skills and knowledge gained during the previous 9-month to learn the fundamentals of software engineering.

Prior to the program, the idea for this application had been in mind for a while, but lacked the necessary skills and knowledge to bring it to life. The program started with the basics of programming with no prior knowledge needed and gradually built up to more advanced topics such as web development, databases, and more. Throughout the program, a wide range of technologies and tools were covered, including Python, Flask, MySQL, SQLAlchemy, HTML/CSS, etc.

With the skills and knowledge gained from the program, this web application was developed from start to finish, covering all aspects of the development process including planning, design, implementation, testing, and deployment (Although the app is not live right now). The application serves as a showcase of the skills and knowledge gained during the program, and demonstrates the ability to develop a fully functional web application using industry-standard technologies and best practices.

## Acknowledgement
This project was made possible thanks to the following contributors: <br>
[Saad Out](https://github.com/saad-out) <br>
[Yusuf Yusuf](https://github.com/koredeycode)

We would like to thank the ALX community program for providing us with the opportunity to learn and grow our skills in software engineering. The knowledge and experience we gained during the program was invaluable and will stay with us for years to come.
