-- =====================================================
-- PROJECT: PeoplePulse
-- FILE: 01_database_setup.sql
-- PURPOSE: Database and employee table setup
-- DATABASE: PostgreSQL
-- =====================================================

-- 1. Create database (run separately if not already created)
-- CREATE DATABASE peoplepulse;

-- 2. Connect to the PeoplePulse database in pgAdmin.
-- 3. Verify the employee table exists.

SELECT
    table_schema,
    table_name
FROM information_schema.tables
WHERE table_schema = 'public'
  AND table_name = 'employees';

-- 4. Verify the table structure.

SELECT
    column_name,
    data_type,
    is_nullable
FROM information_schema.columns
WHERE table_schema = 'public'
  AND table_name = 'employees'
ORDER BY ordinal_position;

-- 5. Verify the total number of records.

SELECT COUNT(*) AS total_employees
FROM public.employees;