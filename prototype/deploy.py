```python
import os
from flask import Flask, render_template
from prototype import app, data_analysis, machine_learning, ai_module, mobile_interface, responsive_design, touchscreen_input, human_computer_interaction, natural_language_processing, software_engineering, cyber_security, encryption, authentication, aesthetics, usability, journalism, music_theory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```