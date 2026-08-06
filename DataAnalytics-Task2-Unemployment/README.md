# 📉 Unemployment Analysis with Python

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-EDA-150458?logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![OIBSIP](https://img.shields.io/badge/OIBSIP-Data%20Analytics%20Track-purple)

> **OIBSIP Data Analytics Internship — Task 2**
> Explore regional and temporal unemployment trends in India, with a focus on the impact of COVID-19.

**Author:** Letsoenyo Clen Bongane · [MordecaiTechSolutions](#)

---

## 📑 Table of Contents
- [Overview](#-overview)
- [Tech Stack](#-tech-stack)
- [Dataset](#-dataset)
- [Approach](#-approach)
- [Key Visualizations](#-key-visualizations)
- [Results](#-results)
- [Conclusion](#-conclusion)
- [Files](#-files)
- [How to Run](#-how-to-run)

---

## 🔍 Overview

This analysis digs into India's state-level unemployment data from 2019–2020 to answer two questions: which regions consistently run the highest unemployment, and how sharply did COVID-19's onset disrupt the national labour market. The headline finding — unemployment nearly doubled nationally in the immediate lockdown period — is explored down to the state level and cross-checked against employment and labour participation trends, not just the headline rate alone.

## 🧰 Tech Stack

| Tool | Purpose |
|---|---|
| Python 3 | Core language |
| pandas / numpy | Data cleaning & aggregation |
| matplotlib / seaborn | Visualization |
| Jupyter Notebook | Analysis environment |

## 📊 Dataset

**Source:** ["Unemployment in India"](https://www.kaggle.com/datasets/gokulrejithr/unemployment-in-india) — Kaggle. Not redistributed in this repo per Kaggle's terms; download it yourself and place it at `data/Unemployment in India.csv`.

| Property | Value |
|---|---|
| Rows (post-cleaning) | 740 |
| Time range | May 2019 – June 2020 |
| Frequency | Monthly |
| Coverage | 28 Indian states/UTs |
| Key columns | Unemployment Rate (%), Employed, Labour Participation Rate (%), Area (Rural/Urban) |

## 🛠 Approach

<details>
<summary><b>1. Data Loading & Cleaning</b></summary>
<br>

Stripped whitespace from column names and string values (a known quirk of this dataset), dropped fully-empty rows, converted `Date` to a proper datetime column, and renamed long column headers for readability.
</details>

<details>
<summary><b>2. Exploratory Data Analysis</b></summary>
<br>

Computed region-wise average unemployment rate and month-wise national trend to establish a baseline before visualizing anything.
</details>

<details>
<summary><b>3. Time-Series & Regional Analysis</b></summary>
<br>

Charted the 3 highest-unemployment states over time to see how their trajectories compare, and ranked all states by average unemployment rate in a bar chart.
</details>

<details>
<summary><b>4. Correlation Analysis</b></summary>
<br>

Built a correlation heatmap across Unemployment Rate, Employed count, and Labour Participation Rate to check for a linear relationship across the full dataset.
</details>

<details>
<summary><b>5. Pre-COVID vs. Post-COVID Comparison</b></summary>
<br>

Split the data at March 2020 (India's lockdown onset) and compared mean values across all three key metrics, with percentage change calculated for each.
</details>

## 🖼 Key Visualizations

<details>
<summary><b>Click to view: Unemployment Rate Over Time — Top 3 States</b></summary>
<br>

![Time series — top 3 states](screenshots/Screenshot_from_2026-08-06_13-29-30.png)

Tripura, Haryana, and Jharkhand — the three highest-average states — all spike sharply around April 2020, with Jharkhand peaking above 60%.
</details>

<details>
<summary><b>Click to view: Top 10 States by Average Unemployment Rate</b></summary>
<br>

![Top 10 states bar chart](screenshots/Screenshot_from_2026-08-06_13-29-36.png)
</details>

<details>
<summary><b>Click to view: Correlation Heatmap</b></summary>
<br>

![Correlation heatmap](screenshots/Screenshot_from_2026-08-06_13-29-40.png)

Weak correlations across the board (-0.22 max) — expected, since these are state-month snapshots rather than a single continuous series; the COVID shock shows up far more clearly in the time-series view.
</details>

<details>
<summary><b>Click to view: Pre-COVID vs. Post-COVID Comparison Table</b></summary>
<br>

![Pre/post-COVID comparison](screenshots/Screenshot_from_2026-08-06_13-29-30.png)
</details>

## 📈 Results

| Metric | Pre-COVID Mean | Post-COVID Mean | % Change |
|---|---|---|---|
| Unemployment Rate (%) | 9.51 | 17.77 | **+86.9%** |
| Employed | 7,466,028 | 6,517,203 | -12.7% |
| Labour Participation Rate (%) | 43.89 | 39.33 | -10.4% |

**Top 5 states by average unemployment rate:** Tripura (28.4%), Haryana (26.3%), Jharkhand (20.6%), Bihar (18.9%), Himachal Pradesh (18.5%)

## 🏆 Conclusion

<details>
<summary><b>Click to expand full conclusion</b></summary>
<br>

This analysis confirms COVID-19's severe, measurable impact on India's labour market: national unemployment nearly doubled (9.5% → 17.8%) in the immediate lockdown period, with the worst-hit states — Jharkhand, Tripura, and Haryana — seeing unemployment spike above 60% for a single month before partially recovering.

Critically, the data shows this wasn't only a story of layoffs: both employment count and labour force participation dropped simultaneously, indicating many people were pushed out of the labour market entirely rather than just left unemployed within it. For a policymaker, this suggests recovery support needs to address not just job creation, but also re-engagement of workers who exited the labour force — reskilling and outreach programs, not just vacancy postings, since a lower participation rate means fewer people were even actively looking.
</details>

## 📂 Files

DataAnalytics-Task2-Unemployment/
├── unemployment_analysis.ipynb # Full executed notebook
├── unemployment_analysis.py # Source (VS Code # %% cell format)
├── data/ # Downloaded CSV (not committed to git)
├── screenshots/ # Visual evidence
└── README.md # This file


## ▶️ How to Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pandas numpy matplotlib seaborn jupyter jupytext
jupytext --to notebook unemployment_analysis.py
jupyter nbconvert --to notebook --execute --inplace unemployment_analysis.ipynb
```

---

<p align="center"><i>Part of the OIBSIP Data Analytics Track — see the full <a href="../">OIBSIP repository</a> for other completed tasks.</i></p>