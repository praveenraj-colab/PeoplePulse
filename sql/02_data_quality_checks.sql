-- =====================================================
-- PROJECT: PeoplePulse
-- FILE: 02_data_quality_checks.sql
-- PURPOSE: Data quality validation
-- DATABASE: PostgreSQL
-- =====================================================

-- 1. TOTAL RECORDS

SELECT
    COUNT(*) AS total_records
FROM public.employees;


-- 2. DUPLICATE EMPLOYEE NUMBERS

SELECT
    employee_number,
    COUNT(*) AS duplicate_count
FROM public.employees
GROUP BY employee_number
HAVING COUNT(*) > 1;


-- 3. MISSING VALUES ACROSS ALL 35 COLUMNS

SELECT
    column_name,
    COUNT(*) FILTER (
        WHERE column_value = 'null'::jsonb
           OR column_value = '""'::jsonb
    ) AS missing_values
FROM public.employees AS e
CROSS JOIN LATERAL jsonb_each(to_jsonb(e))
    AS fields(column_name, column_value)
GROUP BY column_name
ORDER BY missing_values DESC, column_name;


-- 4. UNIQUE EMPLOYEE NUMBERS

SELECT
    COUNT(DISTINCT employee_number) AS unique_employee_numbers
FROM public.employees;


-- 5. NULL EMPLOYEE NUMBERS

SELECT
    COUNT(*) AS null_employee_numbers
FROM public.employees
WHERE employee_number IS NULL;


-- 6. ATTRITION DISTRIBUTION

SELECT
    attrition,
    COUNT(*) AS employee_count,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM public.employees),
        2
    ) AS percentage
FROM public.employees
GROUP BY attrition
ORDER BY attrition;


-- 7. CHECK INVALID ATTRITION VALUES

SELECT
    attrition,
    COUNT(*) AS record_count
FROM public.employees
WHERE attrition NOT IN ('Yes', 'No')
   OR attrition IS NULL
GROUP BY attrition;


-- 8. DUPLICATE COMPLETE RECORDS

SELECT
    COUNT(*) AS duplicate_rows
FROM (
    SELECT *
    FROM public.employees
    GROUP BY
        employee_number,
        age,
        attrition,
        business_travel,
        daily_rate,
        department,
        distance_from_home,
        education,
        education_field,
        employee_count,
        environment_satisfaction,
        gender,
        hourly_rate,
        job_involvement,
        job_level,
        job_role,
        job_satisfaction,
        marital_status,
        monthly_income,
        monthly_rate,
        num_companies_worked,
        over18,
        overtime,
        percent_salary_hike,
        performance_rating,
        relationship_satisfaction,
        standard_hours,
        stock_option_level,
        total_working_years,
        training_times_last_year,
        work_life_balance,
        years_at_company,
        years_in_current_role,
        years_since_last_promotion,
        years_with_curr_manager
    HAVING COUNT(*) > 1
) AS duplicates;


-- =====================================================
-- DATA QUALITY CHECKS COMPLETED
-- =====================================================