```python
import os
from prototype.cyber_security import authenticate_user
from prototype.data_analysis import analyze_data
from prototype.machine_learning import process_input
from prototype.ai_module import render_visualization

class SoftwareEngineering:
    def __init__(self, data_set, user_input):
        self.data_set = data_set
        self.user_input = user_input

    def run_application(self):
        # Authenticate user
        user_authenticated = authenticate_user(self.user_input)
        if not user_authenticated:
            print("User authentication failed.")
            return

        # Process user input
        processed_input = process_input(self.user_input)
        if not processed_input:
            print("Input processing failed.")
            return

        # Analyze data
        analyzed_data = analyze_data(self.data_set, processed_input)
        if not analyzed_data:
            print("Data analysis failed.")
            return

        # Render visualization
        visualization = render_visualization(analyzed_data)
        if not visualization:
            print("Visualization rendering failed.")
            return

        print("Application run successfully.")

if __name__ == "__main__":
    data_set = os.getenv("DATA_SET")
    user_input = os.getenv("USER_INPUT")
    app = SoftwareEngineering(data_set, user_input)
    app.run_application()
```