import pandas as pd
import joblib

from utils import load_config

config = load_config()

model = joblib.load(
    "../" + config["paths"]["model"]
)

student = pd.DataFrame([
    {
        "study_hours": 9,
        "sleep_hours": 7,
        "attendance": 85,
        "previous_marks": 75
    }
])

prediction = model.predict(student)

print(
    f"Predicted Final Score: {prediction[0]:.2f}"
)