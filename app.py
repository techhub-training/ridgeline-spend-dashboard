"""Ridgeline Home & Tool: third-quarter vendor spend dashboard (TechHub challenge 409, solution)."""
import sqlite3
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Ridgeline Q3 vendor spend", layout="wide")
st.title("Ridgeline Home & Tool: Q3 2026 vendor spend")

DB = "data/ridgeline_ap.db"   # read-only copy of Ridgeline's accounts payable
MONTHS = {"July 2026": "2026-07", "August 2026": "2026-08", "September 2026": "2026-09"}


@st.cache_data
def load_invoices() -> pd.DataFrame:
    """Every vendor invoice (not credit memos) dated July 1 to September 30, 2026, with the vendor's category."""
    with sqlite3.connect(f"file:{DB}?mode=ro", uri=True) as db:
        return pd.read_sql_query(
            """SELECT i.invoice_id, i.invoice_date, v.name AS vendor, v.category, i.amount
               FROM invoices i JOIN vendors v ON v.vendor_id = i.vendor_id
               WHERE i.type = 'invoice' AND i.invoice_date BETWEEN '2026-07-01' AND '2026-09-30'""",
            db,
        )


invoices = load_invoices()

# 1. month filter
picked = st.sidebar.multiselect("Months", list(MONTHS), default=list(MONTHS))
selected = invoices[invoices["invoice_date"].str[:7].isin([MONTHS[m] for m in picked])]

# 2. metrics
left, right = st.columns(2)
left.metric("Spend", f"${selected['amount'].sum():,.2f}")
right.metric("Invoices", f"{len(selected):,}")

# 3. summary by category
summary = (selected.groupby("category", as_index=False)
           .agg(Invoices=("invoice_id", "count"), Spend=("amount", "sum"))
           .rename(columns={"category": "Category"}))
summary["Spend"] = summary["Spend"].round(2)
summary = summary.sort_values("Spend", ascending=False, ignore_index=True)

# 4. chart
st.subheader("Spend by vendor category")
st.bar_chart(summary, x="Category", y="Spend", horizontal=True, sort="-Spend")

# 5. table and download
st.subheader("Summary")
st.dataframe(summary, hide_index=True, column_config={"Spend": st.column_config.NumberColumn(format="$%.2f")})
st.download_button("Download summary (CSV)", summary.to_csv(index=False), "q3_spend_by_category.csv", "text/csv")

with st.expander("Invoices in the selection"):
    st.dataframe(selected.sort_values("invoice_date"), hide_index=True)
