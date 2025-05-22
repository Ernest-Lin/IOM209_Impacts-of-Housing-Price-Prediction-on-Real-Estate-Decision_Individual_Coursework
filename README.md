# IOM209_Impacts-of-Housing-Price-Prediction-on-Real-Estate-Decision_Individual_Coursework

# Beijing Housing Price Prediction under the “Three Red Lines” Policy

## 📌 Project Overview
This repository presents a machine learning-based predictive framework for estimating second-hand housing prices in Beijing. The study is conducted in the context of China’s “Three Red Lines” policy, which introduced strict regulatory constraints on real estate firms. Our model helps companies optimize pricing, target high-growth locations, and assess risks under policy volatility.

## 🧠 Methodology
We trained and evaluated multiple models including:
- **Linear Regression**
- **Random Forest** (with Top-N feature selection)
- **XGBoost** (with optimized hyperparameters)
- **Stacking Ensemble** (integrating all three base learners)

The best-performing model—stacking ensemble—achieved:
- **R² Score:** 0.9128
- **Key Features:** `CommunityAverage`, `TradeTime`, and `Government Investment`

All models used engineered spatial and temporal variables, including geodesic distance to Tiananmen Square and a north-south urban indicator based on geographic coordinates.

## 📊 Data
- **Source:** Kaggle open real estate dataset (~310,000 entries)
- **Attributes:** 26 fields per record (area, price, floor, coordinates, etc.)
- **Preprocessing Highlights:**
  - Log transformation of target variable
  - Z-score and rule-based outlier removal
  - Feature construction (distance, policy indicators, floor encoding)

> ⚠️ Due to file size limitations, intermediate CSVs and large datasets are **not included** in this repository.  
> If you are interested in accessing full data or pipeline artifacts, please contact me at:

- 📧 **3050139891@qq.com**
- 📧 **ernestlin2004@163.com**

## ✅ Key Outcomes
- **Accurate Pricing:** 16.4% improvement over traditional heuristics
- **Location Targeting:** 73% alignment with actual price trends
- **Risk Forecasting:** Policy-aware modeling of investment response

## 📚 Citation
If you use this codebase or insights in your research, please cite the project or reach out for collaboration.

---

© 2025 Ernest Lin. All rights reserved.
