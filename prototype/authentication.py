```python
import hashlib
from flask import Flask, request
from flask_login import LoginManager, UserMixin, login_user

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/login', methods=['POST'])
def login():
    user_input = request.form['user_input']
    user = UserSchema.validate(user_input)
    if user is None:
        return "Invalid user credentials", 401

    password_hash = hashlib.sha256(user['password'].encode()).hexdigest()
    if password_hash != user['password_hash']:
        return "Invalid user credentials", 401

    login_user(user)
    return "Logged in successfully"

if __name__ == "__main__":
    app.run(debug=True)
```