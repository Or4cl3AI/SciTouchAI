```python
import os
from flask import Flask, render_template, request
from prototype.touchscreen_input import TouchScreenInput

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

class ResponsiveDesign:
    def __init__(self):
        self.touchScreenInput = TouchScreenInput()

    def renderUI(self):
        screenWidth = self.touchScreenInput.getScreenWidth()
        screenHeight = self.touchScreenInput.getScreenHeight()

        if screenWidth < 600:
            return render_template('mobile.html')
        elif screenWidth < 1200:
            return render_template('tablet.html')
        else:
            return render_template('desktop.html')

if __name__ == '__main__':
    rd = ResponsiveDesign()
    rd.renderUI()
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
```