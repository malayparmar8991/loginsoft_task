SELECT
	e.emp_id emp_id,
	e.emp_name emp_name,
	m.emp_name manager_name
FROM
	emr_employee e
LEFT JOIN emr_employee m ON m.emp_id = e.manager_name_id