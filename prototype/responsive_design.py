```python
import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data-display')
def data_display():
    return render_template('data_display.html')

@app.route('/user-input-field')
def user_input_field():
    return render_template('user_input_field.html')

@app.route('/submit-button')
def submit_button():
    return render_template('submit_button.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
```