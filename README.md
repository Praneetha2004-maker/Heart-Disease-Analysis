# Heart Disease Analysis Dashboard

An end-to-end **Heart Disease Data Analysis** project built around the Cleveland subset of the UCI Heart Disease dataset (303 patients). The project combines **Pandas for data preparation/EDA**, **Tableau for BI dashboards**, and a **React + TypeScript + Vite + Recharts** web dashboard inspired by the supplied reference project.

> **Important:** This is an educational data-analysis project. The patient-profile page is descriptive only and is not a medical diagnostic or prediction tool.

## What is included

- `python/Heart_Disease_Analysis.ipynb` — Pandas analysis notebook
- `python/heart_disease_analysis.py` — repeatable cleaning/EDA script
- `data/data_dictionary.csv` — column definitions
- `tableau/Heart_Disease_Analysis.twbx` — completed Tableau workbook
- React dashboard with:
  - Overview
  - Clinical View
  - Policy View
  - Patient Profile
  - CSV upload
  - Interactive filters and charts
- `docs/` — project documentation

## Dataset

The cleaned 303-row project file is already included at:

`data/heart_disease_clean.csv`

You can replace it with another compatible CSV if you want to reuse the dashboard.

Expected columns:

`age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, target`

The UCI Cleveland dataset contains 303 instances. The original UCI target can contain values 0–4; this project uses the common binary analysis mapping: `0 = No Disease`, `1–4 = Heart Disease`.

## Run the React dashboard

### Windows

1. Install Node.js (LTS).
2. Open PowerShell in this project folder.
3. Run:

```powershell
npm install
npm run dev
```

4. Open the local URL printed by Vite, normally `http://localhost:5173`.
5. Upload `data/heart_disease_clean.csv` on the first screen.

### Quick Windows launcher

You can also run `RUN_PROJECT.bat` after installing Node.js.

## Run the Pandas notebook

```powershell
pip install -r python/requirements.txt
jupyter notebook python/Heart_Disease_Analysis.ipynb
```

Run the notebook from top to bottom.

## Tableau

Open:

`tableau/Heart_Disease_Analysis.twbx`

The workbook contains the completed Tableau analysis dashboards and calculated fields created for the project.

## Main dashboard metrics

For the completed Tableau workbook:

- Total Patients: **303**
- Heart Disease Patients: **139**
- Heart Disease: **45.9%**
- Average Age: **54.44 years**

These are descriptive statistics for this dataset, not medical conclusions.

## Dashboard pages

### Overview
High-level KPIs, disease distribution, age distribution, and gender/disease breakdown.

### Clinical View
Age range and gender filters, cholesterol vs age, maximum heart rate vs age, chest pain breakdown, and average risk-factor comparison.

### Policy View
Exercise angina, fasting blood sugar, blood-pressure ranges, cholesterol ranges, and ST-slope distributions by disease status.

### Patient Profile
Select an individual dataset row and compare its values with dataset averages. The displayed indicator score is a descriptive visualization aid only.

## Suggested GitHub structure

```text
Heart-Disease-Analysis/
├── data/
│   ├── heart_disease_clean.csv
│   ├── data_dictionary.csv
│   └── README.md
├── python/
│   ├── Heart_Disease_Analysis.ipynb
│   ├── heart_disease_analysis.py
│   └── requirements.txt
├── src/
├── public/
├── tableau/
│   └── Heart_Disease_Analysis.twbx
├── docs/
├── package.json
├── RUN_PROJECT.bat
└── README.md
```
