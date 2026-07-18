# Introduction to MLOps

## What is AI?

Artificial Intelligence (AI) is the ability of machines to mimic human
intelligence and perform tasks such as understanding language, making
decisions, and recognizing patterns.

**Examples:** - ChatGPT - Siri - Alexa - Tesla Autopilot

## What is Machine Learning?

Machine Learning (ML) is a subset of AI where systems learn from
historical data instead of relying solely on hard-coded rules. ML models
identify patterns and use them to make predictions or decisions.

## What is MLOps?

Before understanding MLOps, it's important to understand where it comes
from.

> MLOps is directly inspired by DevOps.

Just like DevOps transformed how we build and operate software, MLOps
brings those same principles into the Machine Learning world.

**MLOps (Machine Learning Operations)** combines Machine Learning,
DevOps, and Operations practices to build, deploy, monitor, and manage
ML models in production.

It can be thought of as:

> **"DevOps for Machine Learning"**

## Why Do We Need MLOps?

After a model is trained, organizations need to:

-   Deploy it
-   Version it
-   Monitor its performance
-   Retrain it when data changes
-   Scale it efficiently

MLOps provides the processes and tools required to automate these
activities across the entire machine learning lifecycle.

## Real-World Use Cases

  Company/Domain   Use Case
  ---------------- -------------------------
  Netflix          Movie recommendations
  Amazon           Product recommendations
  Gmail            Spam detection
  Banking          Fraud detection
  Healthcare       Disease prediction

------------------------------------------------------------------------

## Student Score Prediction Project

Throughout this series, we will build a **Student Score Prediction
System** that predicts a student's final score based on:

-   Study Hours
-   Sleep Hours
-   Attendance
-   Previous Marks

### Dataset Example

``` csv
study_hours,sleep_hours,attendance,previous_marks,final_score
2,6,70,50,55
3,7,75,55,60
4,7,80,60,68
5,8,85,70,75
6,8,90,75,82
7,7,92,80,88
```

### Features vs Target

#### Features (Inputs)

-   Study Hours
-   Sleep Hours
-   Attendance
-   Previous Marks

#### Target (Prediction)

-   Final Score

------------------------------------------------------------------------

## How the Model Learns

The model starts without any knowledge. During training, it analyzes
historical data and assigns weights to each feature.

For our sample project:

-   Study Hours positively influence the prediction.
-   Attendance positively influences the prediction.
-   Previous Marks positively influence the prediction.
-   Sleep Hours have a negative coefficient due to the limited dataset.

------------------------------------------------------------------------

## DevOps vs MLOps

  DevOps Concept           MLOps Equivalent
  ------------------------ ------------------------------------
  Source Code Versioning   Data + Model Versioning
  CI Pipelines             Model Training Pipelines
  CD Pipelines             Automated Model Deployment
  Monitoring Services      Monitoring Model Performance
  Rollbacks                Model Version Rollback
  Automation               End-to-End ML Lifecycle Automation

------------------------------------------------------------------------

## Summary

MLOps bridges the gap between machine learning development and
production operations. By applying DevOps principles to machine
learning, organizations can build reliable, scalable, and maintainable
AI systems.

In this series, we will continue building our Student Score Prediction
project while exploring the complete MLOps lifecycle, including:

-   Data Versioning
-   Model Training
-   CI/CD Pipelines
-   Docker
-   Kubernetes
-   Monitoring
-   Model Retraining
-   Production Deployment
