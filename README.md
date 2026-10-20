# Ridgeline Q3 spend dashboard: solution

The worked solution to TechHub challenge 409, **Publish a Spend Dashboard with Streamlit** (https://techhub.byuaccounting.net/t/409-streamlit-publish-a-spend-dashboard-with-streamlit/9409/).
The starter that students copy is on the `main` branch of https://github.com/techhub-training/ridgeline-spend-dashboard.

Run it: open a codespace on this branch, or `pip install -r requirements.txt` and `streamlit run app.py`.

What the solution does, TODO by TODO:

1. `st.sidebar.multiselect` with the three months, all selected by default; the data frame is filtered with `isin`.
2. `st.metric` twice, side by side in `st.columns(2)`.
3. `groupby("Category")` with `agg(Invoices=("invoice_id", "count"), Spend=("amount", "sum"))`, `round(2)`, sorted by `Spend` descending.
4. `st.bar_chart(summary, x="Category", y="Spend", horizontal=True, sort="-Spend")`.
5. `st.dataframe` and `st.download_button(..., summary.to_csv(index=False), "q3_spend_by_category.csv")`.

All three months: 375 invoices, 791,972.86. Lumber is the largest category (137,598.17); Lighting the smallest (3,609.88).

To publish: share.streamlit.io › Create app › this repository, branch `main`, file `app.py`. No secrets needed.
