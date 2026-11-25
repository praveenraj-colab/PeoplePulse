
-- =====================================================
-- PEOPLEPULSE - RETENTION ANALYSIS
-- Dataset: IBM HR Analytics Employee Attrition
-- =====================================================

-- 1. Average tenure: Active vs Former Employees

SELECT
    attrition,
    COUNT(*) AS total_employees,
    ROUND(AVG(years_at_company), 2) AS average_tenure,
    ROUND(AVG(years_in_current_role), 2) AS average_years_in_role,
    ROUND(AVG(years_since_last_promotion), 2) AS average_years_since_promotion
FROM employees
GROUP BY attrition
ORDER BY attrition;

-- 2. Retention by Years at Company

SELECT
    years_at_company,
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (WHERE attrition = 'No') AS active_employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'No') * 100.0
        / COUNT(*), 2
    ) AS retention_percentage
FROM employees
GROUP BY years_at_company
ORDER BY years_at_company;

-- 3. Retention by Years in Current Role

SELECT
    years_in_current_role,
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (WHERE attrition = 'No') AS active_employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'No') * 100.0
        / COUNT(*), 2
    ) AS retention_percentage
FROM employees
GROUP BY years_in_current_role
ORDER BY years_in_current_role;

-- 4. Retention by Years Since Last Promotion

SELECT
    years_since_last_promotion,
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (WHERE attrition = 'No') AS active_employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'No') * 100.0
        / COUNT(*), 2
    ) AS retention_percentage
FROM employees
GROUP BY years_since_last_promotion
ORDER BY years_since_last_promotion;

-- 5. Retention by Relationship Satisfaction

SELECT
    relationship_satisfaction,
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (WHERE attrition = 'No') AS active_employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'No') * 100.0
        / COUNT(*), 2
    ) AS retention_percentage
FROM employees
GROUP BY relationship_satisfaction
ORDER BY relationship_satisfaction;

-- 6. Retention by Work-Life Balance

SELECT
    work_life_balance,
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (WHERE attrition = 'No') AS active_employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'No') * 100.0
        / COUNT(*), 2
    ) AS retention_percentage
FROM employees
GROUP BY work_life_balance
ORDER BY work_life_balance;

-- =====================================================
-- RETENTION ANALYSIS COMPLETED
-- =====================================================