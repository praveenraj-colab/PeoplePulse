# PeoplePulse – Workforce Intelligence & Employee Retention Analytics Platform

<p align="center">
  <strong>Turning HR Data into Workforce Intelligence</strong>
</p>

<p align="center">
Developed by <strong>Praveenraj M </strong>
</p>
<p align="center">
  PostgreSQL · SQL · Python · Statistical Analysis · Power BI
</p>

---

## 1. Project Overview

**PeoplePulse** is an end-to-end HR analytics project designed to analyse employee workforce patterns and understand factors associated with employee attrition.

The project uses SQL, Python, statistical techniques and Power BI to transform employee data into meaningful workforce insights.

It examines employee demographics, departments, job roles, compensation, overtime, job satisfaction, work-life balance and tenure to identify workforce segments with relatively higher attrition.

The final output is a five-page interactive Power BI dashboard supported by SQL analysis, Python scripts, statistical testing and a business insights report.

## 2. Business Problem Statement

Employee attrition is an important workforce management challenge. Frequent employee departures can increase recruitment and training costs, disrupt workforce planning and affect organisational productivity.

HR teams need more than basic employee headcounts to understand workforce trends. They need analytical evidence to identify which employee groups experience higher attrition and which workplace factors are associated with employee departures.

PeoplePulse addresses this analytical problem by examining employee workforce data and presenting findings through SQL queries, Python analysis and interactive Power BI dashboards.

**Primary objective:** Identify employee attrition patterns and provide evidence-based insights that can support better HR workforce planning and retention decisions.

## 3. Project Objectives

- Analyse employee demographics and workforce composition.
- Measure overall employee attrition and retention proportions.
- Identify departments and job roles with higher attrition.
- Examine the relationship between overtime and attrition.
- Compare income and tenure patterns between employees who stayed and left.
- Investigate job satisfaction and work-life balance patterns.
- Perform statistical tests to evaluate selected relationships and differences.
- Develop an interactive Power BI dashboard for HR decision support.

## 4. Dataset Information

| Attribute | Details |
|---|---|
| Dataset | IBM HR Analytics Employee Attrition & Performance |
| Records | 1,470 employees |
| Columns | 35 |
| Dataset type | Synthetic / fictional employee data |
| Target variable | Attrition |
| Attrition categories | Yes / No |

**Important:** This dataset is synthetic and does not represent actual employee records from a real organisation. The findings are analytical observations from the supplied dataset.

## 5. Technology Stack

| Technology | Purpose |
|---|---|
| PostgreSQL 17 | Database management |
| SQL | Data validation and workforce analysis |
| Python | Data validation, EDA and statistical analysis |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| SciPy | Statistical hypothesis testing |
| Matplotlib | Data visualisation |
| Seaborn | Statistical visualisation |
| Power BI Desktop | Interactive dashboard development |
| DAX | Measures and calculated columns |
| Visual Studio Code | Development environment |
| pgAdmin 4 | PostgreSQL database administration |

## 6. Project Workflow

The project follows an end-to-end analytical workflow:

1. Dataset acquisition and database preparation.
2. Data validation and quality checks.
3. SQL-based workforce and attrition analysis.
4. Python exploratory data analysis.
5. Statistical testing and effect-size analysis.
6. Python visualisation.
7. Power BI dashboard development.
8. Business interpretation and reporting.

## 7. SQL Analysis

PostgreSQL was used to organise and analyse the employee dataset.

Key analytical areas:

- Database and table verification.
- Employee record and duplicate checks.
- Missing-value validation.
- Workforce distribution by department.
- Attrition by department and job role.
- Attrition by overtime.
- Attrition by age and income ranges.
- Job satisfaction analysis.
- Employee retention by tenure.
- Retention by promotion history and work-life balance.

Five SQL scripts organise the database verification, data quality checks, workforce analysis, attrition analysis and retention analysis.

## 8. Python Analysis

Python was used to perform five stages of analysis.

### Data Validation
- Dataset dimensions and column inspection.
- Missing-value checks.
- Duplicate record checks.
- Employee identifier validation.
- Attrition distribution.

### Exploratory Data Analysis
- Employee age and demographic distribution.
- Department and job-role distribution.
- Attrition comparisons across employee groups.
- Monthly income and tenure comparisons.
- Correlation analysis of selected numerical variables.

### Data Visualisation

Five analytical visualisations were generated:

1. Attrition Rate by Department.
2. Attrition Rate by Overtime.
3. Monthly Income Distribution by Attrition.
4. Years at Company by Attrition.
5. Workforce Variable Correlation Heatmap.

### Statistical Analysis

Four statistical tests were performed:

| Statistical test | Variables examined |
|---|---|
| Chi-square test | Overtime and attrition |
| Chi-square test | Department and attrition |
| Mann–Whitney U test | Monthly income by attrition |
| Mann–Whitney U test | Years at company by attrition |

Effect sizes and Holm multiple-testing correction were also incorporated into the final business insights script.

## 9. Power BI Dashboard

PeoplePulse contains five interactive dashboard pages.

### Page 1 – Executive Overview

Provides a high-level view of workforce composition, employee headcount, attrition and key HR metrics.

### Page 2 – Workforce Demographics

Examines workforce distribution by:
- Age group.
- Education level.
- Marital status.
- Job role.
- Gender across departments.

### Page 3 – Attrition Analysis

Investigates attrition patterns across:
- Age groups.
- Job roles.
- Monthly income ranges.
- Years at company.
- Job satisfaction levels.

### Page 4 – Retention Intelligence

Examines retention-related patterns across:
- Business travel.
- Work-life balance.
- Years since last promotion.
- Job involvement.
- Environment satisfaction.

### Page 5 – Attrition Rate Analysis

Compares attrition proportions across:
- Age groups.
- Job roles.
- Income ranges.
- Years at company.
- Job satisfaction levels.

## 10. Key Analytical Findings

The following findings were identified from the 1,470 employee records.

| Metric | Finding |
|---|---:|
| Total employees | 1,470 |
| Employees who stayed | 1,233 |
| Employees who left | 237 |
| Overall dataset attrition proportion | 16.12% |
| Sales department attrition | 20.63% |
| Human Resources attrition | 19.05% |
| Research & Development attrition | 13.84% |
| Overtime employees' attrition | 30.53% |
| Non-overtime employees' attrition | 10.44% |

### Additional observations

- Sales Representatives had the highest attrition rate among job roles.
- Laboratory Technicians accounted for the highest number of employee departures by job role.
- Employees who left had lower median monthly income than employees who stayed.
- Employees who left had shorter median tenure.
- Employees with job satisfaction level 1 showed the highest attrition proportion among the four satisfaction levels.

These observations describe patterns in the dataset; they do not establish that any particular factor caused employee departures.

## 11. Business Recommendations

Based on the observed patterns, the following areas deserve further HR investigation:

1. **Overtime management:** Examine workload allocation, scheduling and employee experience among overtime workers.
2. **Department-level retention:** Investigate the higher observed attrition proportions in Sales and Human Resources.
3. **Compensation review:** Examine pay progression and compensation patterns across employee groups.
4. **Early-tenure engagement:** Review onboarding, training and employee support during the initial years of employment.
5. **Employee experience:** Investigate job satisfaction, work-life balance and workplace conditions.

These are recommendations for further investigation, not proven solutions to employee attrition.

## 12. Project Structure

```text
PeoplePulse/
│
├── data/
│   ├── raw/
│   │   └── HR-Employee-Attrition.csv
│   └── processed/
│
├── sql/
│   ├── 01_database_setup.sql
│   ├── 02_data_quality_checks.sql
│   ├── 03_workforce_analysis.sql
│   ├── 04_attrition_analysis.sql
│   └── 05_retention_analysis.sql
│
├── python/
│   ├── 01_data_validation.py
│   ├── 02_exploratory_data_analysis.py
│   ├── 03_data_visualization.py
│   ├── 04_statistical_analysis.py
│   └── 05_business_insights.py
│
├── power bi/
│   └── PeoplePulse.pbix
│
├── reports/
│   ├── visualizations/
│   ├── statistical_results.csv
│   └── PeoplePulse_Business_Insights.md
│
└── README.md
```

## 13. How to Run the Project

### Prerequisites

- PostgreSQL 17
- pgAdmin 4
- Python 3
- Power BI Desktop
- Visual Studio Code

### Python Environment

Install the required libraries:

```bash
python -m pip install pandas numpy scipy matplotlib seaborn
```

### Execute Python Scripts

Run the scripts from the project root directory:

```bash
python python/01_data_validation.py

python python/02_exploratory_data_analysis.py

python python/03_data_visualization.py

python python/04_statistical_analysis.py

python python/05_business_insights.py
```

### SQL

1. Create or connect to the PostgreSQL database named `PeoplePulse`.
2. Ensure the employee table is available in the `public` schema.
3. Execute the SQL scripts using pgAdmin 4.

### Power BI

Open `power bi/PeoplePulse.pbix` using Power BI Desktop.

The PostgreSQL connection may need to be configured for the local environment.

## 14. Limitations

- The project uses synthetic employee data rather than live organisational records.
- The dataset represents a snapshot and does not establish annual turnover.
- Statistical associations do not establish causation.
- The analysis is descriptive and does not constitute a validated employee attrition prediction system.
- Findings should be validated using actual organisational data before operational HR decisions are made.

## 15. Future Improvements

- Develop a predictive employee attrition model.
- Build advanced workforce segmentation.
- Incorporate additional statistical techniques.
- Explore employee retention trends using longitudinal data.
- Develop automated dashboard refresh and reporting workflows.

## 16. Conclusion

PeoplePulse demonstrates an end-to-end HR analytics workflow combining PostgreSQL, SQL, Python, statistical analysis and Power BI.

The project transforms employee data into structured workforce insights and interactive dashboards, demonstrating how analytical tools can support HR professionals in understanding attrition patterns and making more informed workforce decisions.

---

**Project:** PeoplePulse – Workforce Intelligence & Employee Retention Analytics Platform

**Developed by Praveenraj M**

**Domain:** HR Analytics / People Analytics / Workforce Intelligence

**Developed as an end-to-end analytics portfolio project.**