# TransactionLens

A personal adaptation of an inherited transaction anomaly detection project, using the same public ULB / Worldline credit card fraud benchmark. Original transaction values are preserved. This is not a personally collected dataset or a claim of sole authorship of inherited code.

The dashboard now provides a TransactionLens review workspace with single-transaction assessment, bounded batch review, directional feature contributions, and data/methodology notes. Scores come from the configured API; no inherited demo fallback remains.

## Current status

The full `creditcard.csv` is missing. Inherited sample data, screenshots, trained models, registry, and generated scores have been removed from the active checkout. Fresh training and full pipeline verification are pending. No model performance or deployment success is claimed.

## Provenance and attribution

Inherited from [Gretchen Kolthoff's repository](https://github.com/GretchenK20/Financial-Transaction-Anomaly-Detection-System-). Git authorship is preserved. The user confirmed permission to modify the code; no license text was found in this checkout, so no MIT license is asserted here. Retain any applicable notices supplied with permission before redistribution.

Dataset: [ULB / Worldline Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud). The source page identifies database and contents terms as Open Database / Database Contents. Retain source attribution and consult the linked terms for the downloaded version before redistribution. The dataset has not been downloaded or substituted during this adaptation.

## Local development

Install Python and the dependencies in `requirements-full.txt` for the pipeline/API, and `requirements.txt` for the dashboard. Keep the source dataset outside Git. Supply its absolute path to ingestion; do not use the removed demo database as a substitute.

```sh
python scripts/pipeline.py /absolute/path/to/creditcard.csv
uvicorn api.main:app --reload --port 8000
streamlit run streamlit_app.py
pytest tests -q
```

The inherited pipeline runner currently performs ingestion and dbt, then prints training commands. It does not yet execute training. The inherited training/evaluation code requires leakage corrections before results can be reported; see [PROJECT_STATUS.md](PROJECT_STATUS.md). These commands document entry points, not verified completion.

`STREAMLIT_API_URL` configures the dashboard's API address. Keep credentials in local environment variables. Dataset, databases, models, generated results, and logs are excluded from future Git additions; exclusions do not erase previously committed content.

See [PROJECT_STATUS.md](PROJECT_STATUS.md) for the contribution record and [DATASET.md](DATASET.md) for the data contract and limitations.
