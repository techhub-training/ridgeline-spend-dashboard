# Ridgeline Q3 spend dashboard

TechHub challenge 409: **Publish a Spend Dashboard with Streamlit**. Full instructions, data dictionary and hints: https://techhub.byuaccounting.net/t/409-streamlit-publish-a-spend-dashboard-with-streamlit/9409/

*Ridgeline series:* you work in accounting at Ridgeline Home & Tool, a home-improvement retailer with eleven stores
in Utah and Idaho and a distribution center.

The controller wants a dashboard of third-quarter vendor spend (July to September 2026) that anyone on the team can open in a browser, without Python or a copy of the data. `app.py` already loads the quarter's invoices from `data/ridgeline_ap.db` and shows the first rows. You'll finish it and publish it.

## Get your own copy

Click **Use this template › Create a new repository**. Keep the name `ridgeline-spend-dashboard` and make it **Public**.
(Or open it straight in a codespace: https://codespaces.new/techhub-training/ridgeline-spend-dashboard?quickstart=1.) Work in your copy, not this one.

## Open it

On your copy of this repository, click **Code › Codespaces › Create codespace on main**. Everything runs in the
codespace, in your browser: Python, the packages and Claude Code are already installed, the app starts by itself,
and a preview opens in a few minutes. Type `claude` in the terminal to work with Claude Code (sign in the first time).
Stop the codespace when you're done (github.com/codespaces › ••• › Stop) so it doesn't use your free hours.

## Where your data goes (Level 2, Processing on a server)

| Question | Answer |
|---|---|
| Who runs the code? | Streamlit Community Cloud runs `app.py`. |
| Where does the data go? | The invoices ship with the app in `data/ridgeline_ap.db`, opened read-only. Filters, totals and charts are worked out in memory for each visitor and kept nowhere. A download is the visitor's own copy. |
| Who can reach it? | Anyone with the link sees the same made-up data. There is no key, so nothing to protect but the data itself. |

## Your task

Finish the five `TODO`s in `app.py` (an AI assistant is welcome; check what it writes):

1. A month filter in the sidebar: July, August and September 2026, all three selected to start.
2. Two metrics for the selected months: total spend and number of invoices.
3. A summary by category with the columns `Category`, `Invoices`, `Spend` (rounded to cents), largest `Spend` first.
4. A bar chart of `Spend` by `Category`.
5. The summary table, and a **Download summary (CSV)** button that downloads it.

Then publish the app on Streamlit Community Cloud (below). With all three months selected, the dashboard should
show total spend of **791,972.86** from **375** invoices: if it doesn't, fix that first.

## Publish it on Streamlit Community Cloud

1. Commit and push your work to GitHub.
2. Sign in at [share.streamlit.io](https://share.streamlit.io) with your GitHub account.
3. **Create app › Deploy a public app from GitHub**: pick this repository, branch `main`, main file `app.py`.
4. This app needs no secrets. Click **Deploy**. The app gets a public address like `https://<name>.streamlit.app`.

Every push to `main` redeploys the app. An app nobody visits for a while goes to sleep; the first visitor wakes it up.


## Check your answer

On your published app, select all three months, click **Download summary (CSV)**, and upload that file to the TechHub checker. Checker: https://techhub.byuaccounting.net/check/?c=409

The worked solution is on the [`solution` branch](https://github.com/techhub-training/ridgeline-spend-dashboard/tree/solution). Try it yourself first.
