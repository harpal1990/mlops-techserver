# Fundamentals

### What Is Machine Learning?

Think of machine learning as teaching a computer to learn patterns from data instead of programming every rule manually.

With normal programming, you write rules yourself.
With machine learning, you give the computer examples, and it figures out the rules.

Example : Student Score Prediction Project
Throughout this series, we will build a Student Score Prediction system that predicts a student's final score based on study hours, sleep hours, attendance, and previous marks.
Dataset Example

study_hours,sleep_hours,attendance,previous_marks,final_score

2,6,70,50,55
3,7,75,55,60
4,7,80,60,68
5,8,85,70,75
6,8,90,75,82
7,7,92,80,88
Features vs Target
Features (Inputs):
- Study Hours
- Sleep Hours
- Attendance
- Previous Marks

Target (Prediction):
- Final Score
How the Model Learns
The model starts without any knowledge. During training, it analyzes historical data and assigns weights to each feature. For our sample project, study hours, attendance, and previous marks positively influence the prediction, while sleep hours have a negative coefficient due to the limited dataset.

