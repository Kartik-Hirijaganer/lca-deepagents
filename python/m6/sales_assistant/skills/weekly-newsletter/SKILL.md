---
name: weekly-newsletter
description: Draft the weekly sales newsletter for Jane Peacock's team, covering top-selling tracks and artists, revenue by genre, and notable customer activity from the past week. Use whenever someone asks for the weekly newsletter or a weekly sales recap.
---

# Weekly newsletter

The weekly newsletter summarizes the past week's sales activity and breaks it
down by genre and top artist. Work in the sandbox, then save the result.

## 1. Pick the window

The sample data ends in 2013, so "the past week" is relative to the newest
invoice, not to today:

```python
import sqlite3
import pandas as pd

con = sqlite3.connect("chinook.db")
latest = pd.read_sql_query("SELECT MAX(InvoiceDate) AS d FROM Invoice", con)["d"][0]
```

Use the seven days ending on that date. State the window in the newsletter so
the reader knows which dates it covers.

## 2. Pull the numbers

For that window, gather:

- **Revenue total**, and how it compares with the previous seven days.
- **Top 5 tracks** by quantity sold, with their artist.
- **Top 5 artists** by revenue.
- **Revenue by genre**, as a small table.
- **Notable customers**: the three largest invoices, with customer name and country.

Join through `InvoiceLine` to reach `Track`, then `Album` to `Artist`, and
`Genre` from `Track`. Compute every total with pandas, not by hand.

## 3. Assemble

Write one Markdown document:

- `# This Week in Music` title
- a one-sentence intro naming the date window and the revenue total
- `## Top tracks`, `## Top artists`, `## Revenue by genre`, `## Notable customers`
- a closing line flagging anything that looks worth Jane's attention, such as a
  genre that moved sharply against the prior week

Keep it to something Jane can skim in under a minute.

## 4. Save

Write the document to `artifacts/newsletter-<end-of-window-date>.md`, for example
`artifacts/newsletter-2013-12-05.md`.

## Done

Tell Jane the file path, the date window you used, and the revenue total. Do not
email it unless she asks.
