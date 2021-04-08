## Infectious Spread Simulation in University Environment (ISSUE)

> **Description**

Infectious Spread Simulation in University Environment (ISSUE) is an interactive online web-based desktop analytical tool that will model the spread of COVID-19 at the University of Calgary. The tool will support decision makers, such as school administration, by simulating infection spread and risk for a variety of seating arrangements within lecture spaces on campus. The result of the simulation will show a simple layout of the desired room with an overlap of a heat map. Using this visualization, users can adjust infection parameters and the location of each individual “agent”, in order to create a safe environment for students and staff to return to post-pandemic life.

<br />

## How to use it

```bash
$ # Get the code
$ git clone https://github.com/abhijeetjagdev/Infectious_Spread_Simulation_Tool.git
$ cd Infectious_Spread_Simulation_Tool
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules - SQLite Storage
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in browser: http://127.0.0.1:8000/
```

> Note: To use the app, please access the registration page and create a new user. After authentication, the app will unlock the private pages.

<br />

## Code-base Structure

The project is coded using a simple and intuitive structure presented bellow:

```bash
< Infectious_Spread_Simulation_Tool >
   |
   |-- core/                                          # Implements app logic and serve the static assets
   |    |-- settings.py                               # Django app bootstrapper
   |    |-- wsgi.py                                   # Start the app in production
   |    |-- urls.py                                   # Define URLs served by all apps/nodes
   |    |
   |    |-- static/
   |    |    |-- assets/
   |    |    |    |-- css/                            # Dashboard CSS
   |    |    |    |-- dist/                           # Leaflet.js files
   |    |    |    |-- fonts/                          # Fonts and Bootstrap icons
   |    |    |    |-- images/                         # Room floorplan images, favicons
   |    |    |    |-- js/                             # JavaScript plugins
   |    |    |    |-- json/                           # Seat position data
   |    |    |    |-- src/                            # Leaflet.js files
   |    |    |    |-- seat_position_extractor.ipynb   # Seat position extraction Jupyter notebook
   |    |    |    |-- Web Application User Manual.pdf # User manual for app
   |    |
   |    |-- templates/                                # Templates used to render pages
   |         |
   |         |-- includes/                            # HTML chunks and components
   |         |    |-- navigation.html                 # Top menu component
   |         |    |-- sidebar.html                    # Sidebar component
   |         |    |-- scripts.html                    # Scripts common to all pages
   |         |
   |         |-- layouts/                             # Master pages
   |         |    |-- base-fullscreen.html            # Used by Authentication pages
   |         |    |-- base.html                       # Used by common pages
   |         |
   |         |-- accounts/                            # Authentication pages
   |         |    |-- login.html                      # Login page
   |         |    |-- password_reset_complete.html    # Password reset request complete page
   |         |    |-- password_reset_confirm.html     # Enter new passwords page
   |         |    |-- password_reset_done.html        # Password reset request accepted page
   |         |    |-- password_reset_email.txt        # Password reset email template
   |         |    |-- password_reset.html             # Password reset page
   |         |    |-- register.html                   # Register page
   |         |
   |      index.html                                  # The default page
   |     page-404.html                                # Error 404 page
   |     page-500.html                                # Error 404 page
   |       *.html                                     # All other HTML pages
   |
   |-- authentication/                                # Handles auth routes (login and register)
   |    |
   |    |-- urls.py                                   # Define authentication routes  
   |    |-- views.py                                  # Handles login and registration  
   |    |-- forms.py                                  # Define auth forms  
   |
   |-- app/                                           # A simple app that serve HTML files
   |    |
   |    |-- views.py                                  # Serve HTML pages for authenticated users
   |    |-- urls.py                                   # Define some super simple routes
   |    |-- admin.py                                  # Admin data models
   |    |-- agent_based_infection_probability.py      # Python script to calculate COVID-19 attack rates
   |    |-- models.py                                 # Representation of tables in database
   |    |-- urls.py                                   # Routing HTML requests
   |    |-- views.py                                  # Functions to POST/GET data to and from database
   |
   |-- requirements.txt                               # Essential libraries and packages needed to run the app
   |
   |-- .env                                           # Inject Configuration via Environment
   |-- manage.py                                      # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

> The bootstrap flow

- Django bootstrapper `manage.py` uses `core/settings.py` as the main configuration file
- `core/settings.py` loads the app magic from `.env` file
- Redirect the guest users to Login page
- Unlock the pages served by *app* node for authenticated users

<br />

## Deployment

The app is provided with a basic configuration to be executed in [Docker](https://www.docker.com/), [Gunicorn](https://gunicorn.org/), and [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/).


## Credits & Links

- [Django](https://www.djangoproject.com/) - The offcial website
- [Boilerplate Code](https://appseed.us/boilerplate-code) - Index provided by **AppSeed**
- [Boilerplate Code](https://github.com/app-generator/boilerplate-code) - Index published on Github

<br />

---
[Django Dashboard - GradientAble Design](https://appseed.us/admin-dashboards/django-dashboard-gradientable) - Provided by **AppSeed** [Web App Generator](https://appseed.us/app-generator).
