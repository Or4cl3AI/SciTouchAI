```python
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return render_template('index.html')

def optimize_for_mobile():
    # Use Flask-Bootstrap to ensure that the app is mobile responsive
    # The 'index.html' file should be designed with Bootstrap classes for responsiveness
    pass

if __name__ == '__main__':
    app.run(debug=True)
```