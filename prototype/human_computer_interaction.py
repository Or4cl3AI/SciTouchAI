```python
import json
from flask import Flask, request
from prototype.authentication import authenticateUser
from prototype.touchscreen_input import processInput

app = Flask(__name__)

# Shared Variables
user_input = None
user = None

# Shared Schemas
UserSchema = {
    "type": "object",
    "properties": {
        "username": {"type": "string"},
        "password": {"type": "string"},
    },
    "required": ["username", "password"]
}

@app.route('/user-input', methods=['POST'])
def capture_user_input():
    global user_input
    user_input = request.json['user_input']
    processInput(user_input)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route('/login', methods=['POST'])
def login():
    global user
    user = request.json
    if authenticateUser(user):
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
    else:
        return json.dumps({'success':False}), 403, {'ContentType':'application/json'} 

if __name__ == '__main__':
    app.run(debug=True)
```