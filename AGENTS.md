# Agent Instructions

## Product And Keyword Scan Batches

When continuing the product scan and keyword selection from the persistent
category database, process and publish exactly one bounded batch at a time:

```bash
python3 scripts/run_pipeline.py --start-from 2 --max-categories 5
```

After each batch:

1. Identify the five categories updated by that run from their `last_updated`
   values in `results/json/categories.json`.
2. Verify the generated persistent outputs:
   `results/json/categories.json` and `results/html/report.html`.
3. Commit the batch results and push `main` so the public page is refreshed.
4. Do not include unrelated or legacy result-file changes in the commit.
5. In the final output, list every updated category and report its product and
   keyword counts. Also include the commit hash and push result.

Do not start another five-category batch until the current batch has been
committed, pushed, and reported.
