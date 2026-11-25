SELECT
    department,
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (
        WHERE attrition = 'Yes'
    ) AS employees_left,

    ROUND(
        COUNT(*) FILTER (
            WHERE attrition = 'Yes'
        ) * 100.0 / COUNT(*),
        2
    ) AS attrition_percentage

FROM employees

GROUP BY department

ORDER BY attrition_percentage DESC;
SELECT
    COUNT(*) AS total_employees,

    COUNT(*) FILTER (
        WHERE attrition = 'Yes'
    ) AS employees_left,

    ROUND(
        COUNT(*) FILTER (
            WHERE attrition = 'Yes'
        ) * 100.0 / COUNT(*),
        2
    ) AS overall_attrition_percentage

FROM employees;
SELECT
    overtime,
    COUNT(*) AS total_employees,

    COUNT(*) FILTER (
        WHERE attrition = 'Yes'
    ) AS employees_left,

    ROUND(
        COUNT(*) FILTER (
            WHERE attrition = 'Yes'
        ) * 100.0 / COUNT(*),
        2
    ) AS attrition_percentage

FROM employees

GROUP BY overtime

ORDER BY attrition_percentage DESC;
SELECT
    job_role,
    COUNT(*) AS total_employees,

    COUNT(*) FILTER (
        WHERE attrition = 'Yes'
    ) AS employees_left,

    ROUND(
        COUNT(*) FILTER (
            
            WHERE attrition = 'Yes'
        ) * 100.0 / COUNT(*),
        2
    ) AS attrition_percentage

FROM employees

GROUP BY job_role

ORDER BY attrition_percentage DESC;
SELECT
    job_satisfaction,
    COUNT(*) AS total_employees,

    COUNT(*) FILTER (
        WHERE attrition = 'Yes'
    ) AS employees_left,

    ROUND(
        COUNT(*) FILTER (
            WHERE attrition = 'Yes'
        ) * 100.0 / COUNT(*),
        2
    ) AS attrition_percentage

FROM employees

GROUP BY job_satisfaction

ORDER BY job_satisfaction;