# Stock Price Forecasting & Decision Support System

## Overview



The goal is not only to predict future price trends, but also to translate model outputs into actionable investment signals.

## Problem Statement
In financial markets, price movements are influenced by historical trends and patterns.  
Accurate forecasting can support data-driven decision-making, but raw predictions alone are not sufficient for real-world use.  
This project aims to bridge the gap between prediction and decision.

## Approach
The system follows a structured machine learning workflow:

1. Data Collection  
   - Retrieve historical stock data via Yahoo Finance API  

2. Data Preprocessing  
   - Clean and structure time-series data  
   - Generate features for modeling  

3. Model Development  
   - Train a regression-based forecasting model  
   - Capture trends in historical price movements  

4. Model Evaluation  
   - Evaluate performance using RMSE (Root Mean Squared Error)  
   - Assess prediction reliability  

5. Decision Layer  
   - Convert predictions into actionable signals:  
     - BUY (upward trend)  
     - HOLD (stable trend)  
     - SELL (downward trend)  

## Tech Stack
- Python  
- Pandas  
- Scikit-learn  
- Matplotlib  
- yfinance API  

## Output
The system produces:
- Forecasted stock price trends  
- Model performance metrics  
- Decision signals based on predicted trends  

## Key Value
This project highlights the transition from traditional data analysis to applied AI systems by:
- Integrating machine learning into real-world workflows  
- Translating predictions into business decisions  
- Demonstrating end-to-end system thinking  

## Future Improvements
- Incorporate advanced time-series models (e.g., ARIMA, LSTM)  
- Integrate multiple financial indicators  
- Deploy as an automated pipeline or API service  

## Results

- RMSE: ~103  
- Current Price: ~248  
- Predicted Price: ~353  
- Decision: BUY  

The model predicts an upward trend, demonstrating how machine learning outputs can be translated into actionable decision signals.