-- Top 5 funds by AUM
SELECT amfi_code, aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Average NAV per fund
SELECT amfi_code, AVG(nav) AS avg_nav
FROM nav_history
GROUP BY amfi_code;

-- Monthly NAV trend
SELECT strftime('%Y-%m', date) AS month, AVG(nav) AS avg_nav
FROM nav_history
GROUP BY month
ORDER BY month;

-- SIP vs Lumpsum transactions
SELECT transaction_type, COUNT(*) AS total
FROM investor_transactions
GROUP BY transaction_type;

-- Transactions by state
SELECT state, COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- Top 5 funds by 3-year return
SELECT amfi_code, return_3yr_pct
FROM scheme_performance
ORDER BY return_3yr_pct DESC
LIMIT 5;

-- Funds with expense ratio < 1%
SELECT amfi_code, expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;

-- Average investment amount
SELECT AVG(amount_inr) AS avg_investment
FROM investor_transactions;

-- Transactions by gender
SELECT gender, COUNT(*) AS total
FROM investor_transactions
GROUP BY gender;

-- Top 5 high NAV funds
SELECT amfi_code, MAX(nav) AS max_nav
FROM nav_history
GROUP BY amfi_code
ORDER BY max_nav DESC
LIMIT 5;