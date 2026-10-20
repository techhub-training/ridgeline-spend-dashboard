"""Ridgeline Home & Tool: third-quarter vendor spend dashboard (TechHub challenge 409).

Run it:  streamlit run app.py
The TODO comments are your tasks. README.md has the details."""
import sqlite3
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Ridgeline Q3 vendor spend", layout="wide")
st.title("Ridgeline Home & Tool: Q3 2026 vendor spend")

DB = "data/ridgeline_ap.db"   # read-only copy of Ridgeline's accounts payable


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
st.caption(f"{len(invoices)} invoices loaded")
st.dataframe(invoices.head(20))

# TODO 1: in the sidebar, let the user pick months (July, August, September 2026; all three by default)
#         and keep only the invoices in those months.
# TODO 2: show two metrics: total spend and number of invoices for the selected months.
# TODO 3: summarize spend by category: columns Category, Invoices, Spend (rounded to cents), largest Spend first.
# TODO 4: draw a bar chart of Spend by Category.
# TODO 5: show the summary table and add a "Download summary (CSV)" button that downloads it.
