from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Log username and password
        username = request.form.get('username')
        password = request.form.get('password')
        print(f"Username: {username}, Password: {password}")

        return 'Login Successful'

    return 'This is the login page.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
