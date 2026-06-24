CREATE TABLE nav_history (
    amfi_code TEXT,
    date TEXT,
    nav REAL
);

CREATE TABLE scheme_performance (
    amfi_code TEXT,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    return_3yr_pct REAL,
    aum_crore REAL,
    expense_ratio_pct REAL
);

CREATE TABLE investor_transactions (
    investor_id TEXT,
    transaction_date TEXT,
    amfi_code TEXT,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    gender TEXT
);