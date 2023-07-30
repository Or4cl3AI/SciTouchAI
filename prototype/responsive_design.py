```python
import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return render_template('index.html')

def optimizeDisplay():
    if os.environ.get('IS_HEROKU', None):
        app.config.update(
            SERVER_NAME=os.environ['SERVER_NAME'],
            PREFERRED_URL_SCHEME=os.environ['PREFERRED_URL_SCHEME']
        )

    @app.before_request
    def before_request():
        if request.url.startswith('http://'):
            url = request.url.replace('http://', 'https://', 1)
            return redirect(url, code=301)

    return app

if __name__ == '__main__':
    optimizeDisplay()
    app.run(debug=True)
```
This Python script uses Flask and Flask-Bootstrap to create a web application with a responsive design. The `optimizeDisplay` function checks if the application is running on Heroku and configures the server name and URL scheme accordingly. It also redirects all HTTP requests to HTTPS to ensure secure communication. The script then runs the application in debug mode.