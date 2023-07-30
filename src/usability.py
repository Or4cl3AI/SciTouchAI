```python
import time
from src.responsive_design import applyResponsiveDesign
from src.touchscreen_input import handleTouchscreenInput

def optimizeUsability(dataSet, userInput):
    start_time = time.time()
    
    # Apply responsive design principles
    applyResponsiveDesign(dataSet, userInput)
    
    # Handle touchscreen input
    handleTouchscreenInput(userInput)
    
    # Calculate usability score based on time taken and user input
    usability_score = calculateUsabilityScore(start_time, userInput)
    
    return usability_score

def calculateUsabilityScore(start_time, userInput):
    # Calculate time taken for user to input data
    time_taken = time.time() - start_time
    
    # Calculate score based on time taken and length of user input
    usability_score = len(userInput) / time_taken
    
    return usability_score
```