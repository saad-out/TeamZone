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
To run the app locally for testing purposes, follow these steps:
1. Clone the repository to your local machine:
  ```
  git clone https://github.com/saad-out/TeamZone.git
  ```
2. Create a Python virtual environment and activate it:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```
3. Install the required packages:
  ```
  pip install -r requirements.txt
  pip install mysqlclient
  ```
4. Create the MySQL database and user by running the following command after changing the default password inside the file setup_mysql_dev.sql to a strong one:
  ```
  cat setup_mysql_dev.sql | sudo mysql
  ```
5. Create a `.env` file in the main directory and include the values for the following variables:
  ```
  TZ_MYSQL_USER=<your_mysql_username>
  TZ_MYSQL_PWD=<your_mysql_password>
  TZ_MYSQL_HOST=<your_mysql_host>
  TZ_MYSQL_DB=<your_mysql_database>
  ```
  Optionally, you can also include the following variables if you want the forgot password feature to work using Flask-Mail:
  ```
  MAIL_USER=<your_email_username>
  MAIL_PASS=<your_email_password>
  ```
  Otherwise, you can remove the following code from `web/app.py`:
  ```
  app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
  app.config['MAIL_PORT'] = 587
  app.config['MAIL_USE_TLS'] = True
  app.config['MAIL_USERNAME'] = os.environ['MAIL_USER']
  app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASS']
  mail = Mail(app)
  ```
6. Start the web and API servers by running the following commands separately in two different terminal windows from the main directory:
  ```
  python3 -m web.app
  ```
  In a separate shell:
  ```
  python3 -m api.v1.app
  ```
7. Access the web app at `http://localhost:5000` and the API at `http://localhost:5001`. The web app communicates with the API through the JavaScript code.

Alternatively, you could use SQLite instead of MySQL. In this case, you can skip steps 4 and 5 of the installation process, and change the instantiation of the engine in `models/engine/storage.py` to the following:
```
self.__engine = create_engine('sqlite:///site.db')
```
This will create a local SQLite database file named `site.db` in the project directory, and the app will use it instead of a MySQL database. Keep in mind that SQLite has some limitations compared to MySQL, such as concurrency and scalability, so make sure it fits your needs before choosing it as a database solution.

## Architecture

### Pages Flow Diagram

<p align="center">
  <img src="https://github.com/saad-out/TeamZone/blob/main/web/static/images/architecture.png" style="width:80%;"/>
</p>

This diagram shows the flow of pages in the app, from the landing page to the search and filter page, and also the pages accessible to logged-in users.

### Data Flow Diagram (excluding search page)

<p align="center">
  <img src="https://github.com/saad-out/TeamZone/blob/main/web/static/images/data_flow_archi.png" style="width:80%;"/>
</p>

This diagram shows the flow of data in the app, from the client's HTTP requests to the Flask views, and from the views to the data layer where data is fetched and returned to the client.

### Data Flow Diagram (for search page)

<p align="center">
  <img src="https://github.com/saad-out/TeamZone/blob/main/web/static/images/Search_archi.png" style="width:80%;"/>
</p>

This diagram shows the flow of data in the search page, where the JS code fetches data from the API endpoint `/filter_teams` and populates the DOM.
