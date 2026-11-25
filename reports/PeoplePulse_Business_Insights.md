# PeoplePulse - Workforce Intelligence Report

## 1. Project Overview
PeoplePulse analyses employee attrition patterns using the IBM HR Analytics Employee Attrition dataset.

- Employees analysed: 1,470
- Dataset columns: 35
- Employees who left: 237
- Overall dataset attrition proportion: 16.12%

## 2. Key Workforce Findings
- Highest department attrition: Sales (20.63%).
- Overtime attrition: 30.53%.
- Non-overtime attrition: 10.44%.
- Median monthly income among employees who stayed: 5,204.
- Median monthly income among employees who left: 3,202.
- Median tenure among employees who stayed: 6 years.
- Median tenure among employees who left: 3 years.

## 3. Statistical Test Results

### Overtime vs Attrition
- Test: Chi-square
- Test statistic: 87.5643
- Raw p-value: 8.1584237e-21
- Holm-adjusted p-value: 3.2633695e-20
- Effect size (Cramer's V): 0.2441
- Minimum expected cell count: 67.07
- Conclusion: Statistically significant after Holm correction.

### Department vs Attrition
- Test: Chi-square
- Test statistic: 10.7960
- Raw p-value: 0.0045256066
- Holm-adjusted p-value: 0.0045256066
- Effect size (Cramer's V): 0.0857
- Minimum expected cell count: 10.16
- Conclusion: Statistically significant after Holm correction.

### Monthly Income vs Attrition
- Test: Mann-Whitney U
- Test statistic: 191600.5000
- Raw p-value: 2.9508309e-14
- Holm-adjusted p-value: 8.8524928e-14
- Effect size (Rank-biserial correlation): 0.3113
- Conclusion: Statistically significant after Holm correction.

### Years at Company vs Attrition
- Test: Mann-Whitney U
- Test statistic: 189639.0000
- Raw p-value: 2.9161914e-13
- Holm-adjusted p-value: 5.8323827e-13
- Effect size (Rank-biserial correlation): 0.2979
- Conclusion: Statistically significant after Holm correction.

## 4. HR Recommendations for Further Investigation

1. Investigate workload, scheduling and overtime patterns.
2. Review department-specific employee retention challenges.
3. Examine compensation structures and pay progression.
4. Study early-tenure employee experience and onboarding.

## 5. Limitations

- This is a synthetic, cross-sectional dataset, not live company data.
- Observed associations do not establish causation.
- Statistical significance does not necessarily indicate business importance.
- Findings should be validated using real organisational data before making HR policy decisions.
- Multiple-testing correction was applied to the four statistical tests.

## 6. Conclusion
The analysis identifies workforce characteristics associated with employee attrition. These findings can guide further HR investigation, but should not be treated as causal explanations.