# Traffic Accident Analysis

## Project Overview

This project analyzes traffic accident data to identify patterns related to:

- Weather conditions
- Time of day
- Accident severity
- Day of the week
- Road and traffic factors
- Geographic accident hotspots
- Accident distribution across states

The project uses Python, Pandas, Matplotlib, and Seaborn for data analysis and visualization.

---

## Objectives

The main objectives of this project are:

1. Analyze accident patterns based on weather conditions.
2. Identify accident-prone times of the day.
3. Analyze accident severity.
4. Compare accidents across different days of the week.
5. Examine road and traffic factors.
6. Visualize geographic accident hotspots.
7. Identify states with high accident counts.

---

## Dataset

The project uses the US Accidents dataset.

The original dataset contains millions of accident records.

For this GitHub project, a 100,000-row sample is used for efficient analysis and demonstration.

The sample dataset is stored in:

`data/accidents_sample.csv`

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- VS Code
- Git
- GitHub

---

## Project Structure

```text
SCT_DS_4/
│
├── data/
│   └── accidents_sample.csv
│
├── SRC/
│   └── analysis.py
│
├── outputs/
│   ├── weather_accidents.png
│   ├── accidents_by_time_of_day.png
│   ├── accidents_by_hour.png
│   ├── severity_distribution.png
│   ├── accidents_by_day.png
│   ├── weather_vs_severity.png
│   ├── road_traffic_factors.png
│   ├── accident_hotspots.png
│   └── top_10_states.png
│
├── README.md
├── requirements.txt
└── .gitignore