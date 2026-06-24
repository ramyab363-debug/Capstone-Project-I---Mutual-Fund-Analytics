# Data Dictionary

## 02_nav_history.csv

| Column    | Data Type | Description                   |
| --------- | --------- | ----------------------------- |
| amfi_code | TEXT      | Unique fund identifier        |
| date      | DATE      | NAV date                      |
| nav       | REAL      | Net Asset Value of the scheme |

## 07_scheme_performance.csv

| Column            | Data Type | Description                       |
| ----------------- | --------- | --------------------------------- |
| amfi_code         | TEXT      | Unique fund identifier            |
| scheme_name       | TEXT      | Mutual fund scheme name           |
| fund_house        | TEXT      | Fund management company           |
| category          | TEXT      | Fund category                     |
| return_1yr_pct    | REAL      | One-year return percentage        |
| return_3yr_pct    | REAL      | Three-year return percentage      |
| return_5yr_pct    | REAL      | Five-year return percentage       |
| expense_ratio_pct | REAL      | Annual expense ratio percentage   |
| sharpe_ratio      | REAL      | Risk-adjusted performance metric  |
| aum_crore         | REAL      | Assets Under Management (₹ Crore) |

## 08_investor_transactions.csv

| Column           | Data Type | Description                 |
| ---------------- | --------- | --------------------------- |
| investor_id      | TEXT      | Unique investor identifier  |
| transaction_date | DATE      | Transaction date            |
| amfi_code        | TEXT      | Fund identifier             |
| transaction_type | TEXT      | SIP, Lumpsum, or Redemption |
| amount_inr       | REAL      | Transaction amount in INR   |
| state            | TEXT      | Investor state              |
| city             | TEXT      | Investor city               |
| gender           | TEXT      | Investor gender             |
| kyc_status       | TEXT      | KYC verification status     |

## Source

All datasets were provided as part of the Mutual Fund Analytics Capstone Project.
