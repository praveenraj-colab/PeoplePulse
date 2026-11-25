-- =====================================================
-- PEOPLEPULSE
-- FILE 04: ATTRITION ANALYSIS
-- =====================================================

-- 1. Overall attrition summary
SELECT
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    COUNT(*) FILTER (WHERE attrition = 'No') AS active_employees,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0
        / COUNT(*), 2
    ) AS attrition_percentage
FROM employees;


-- 2. Attrition by age group
SELECT
    CASE
        WHEN age < 25 THEN 'Under 25'
        WHEN age < 35 THEN '25-34'
        WHEN age < 45 THEN '35-44'
        WHEN age < 55 THEN '45-54'
        ELSE '55 and Above'
    END AS age_group,
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0
        / COUNT(*), 2
    ) AS attrition_percentage
FROM employees
GROUP BY age_group
ORDER BY
    CASE age_group
        WHEN 'Under 25' THEN 1
        WHEN '25-34' THEN 2
        WHEN '35-44' THEN 3
        WHEN '45-54' THEN 4
        ELSE 5
    END;


-- 3. Attrition by job role
SELECT
    job_role,
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0
        / COUNT(*), 2
    ) AS attrition_percentage
FROM employees
GROUP BY job_role
ORDER BY attrition_percentage DESC;


-- 4. Attrition by monthly income range
SELECT
    CASE
        WHEN monthly_income < 3000 THEN 'Below 3K'
        WHEN monthly_income < 6000 THEN '3K-5,999'
        WHEN monthly_income < 9000 THEN '6K-8,999'
        WHEN monthly_income < 12000 THEN '9K-11,999'
        ELSE '12K and Above'
    END AS income_range,
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0
        / COUNT(*), 2
    ) AS attrition_percentage
FROM employees
GROUP BY income_range
ORDER BY
    CASE income_range
        WHEN 'Below 3K' THEN 1
        WHEN '3K-5,999' THEN 2
        WHEN '6K-8,999' THEN 3
        WHEN '9K-11,999' THEN 4
        ELSE 5
    END;


-- 5. Attrition by years at company
SELECT
    years_at_company,
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0
        / COUNT(*), 2
    ) AS attrition_percentage
FROM employees
GROUP BY years_at_company
ORDER BY years_at_company;


-- 6. Attrition by job satisfaction
SELECT
    job_satisfaction,
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0
        / COUNT(*), 2
    ) AS attrition_percentage
FROM employees
GROUP BY job_satisfaction
ORDER BY job_satisfaction;


-- =====================================================
-- ATTRITION ANALYSIS COMPLETED
-- =====================================================