```python
import os
from flask import Flask, render_template
from flask_mobility import Mobility

app = Flask(__name__)
Mobility(app)

def applyResponsiveDesign():
    @app.route('/')
    def home():
        if os.name == 'posix':  # Check if the operating system is mobile
            return render_template('mobile_home.html')
        else:
            return render_template('desktop_home.html')

if __name__ == "__main__":
    applyResponsiveDesign()
    app.run(debug=True)
```