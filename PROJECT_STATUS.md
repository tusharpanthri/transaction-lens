# TransactionLens adaptation status

Repository inspection: October 1, 2026.

## Reuse and attribution

The configured upstream is https://github.com/GretchenK20/Financial-Transaction-Anomaly-Detection-System-. Git history identifies Gretchen Kolthoff as an author. Existing Git authorship has not been rewritten.

No LICENSE, COPYING, or NOTICE file was found in this checkout. The inherited model card lists MIT, but does not include license text or establish the scope of permission. The user confirmed permission to modify the code on October 1, 2026. No written license document has been supplied; retain the applicable permission and notices before redistribution. Preserve any required copyright and attribution notices once identified. Do not add a license on behalf of upstream contributors.

The user's description of a university team project has not yet been reconciled with the upstream repository and authorship. Personal development can build on inherited work, but does not convert inherited code into sole original authorship.

## Dataset and results

The user selected the same public benchmark as upstream; the full source CSV is missing from the workspace. The only data file found under `data/` was `demo_financial_anomaly.duckdb`; it is an inherited demo artifact. `demo_data.json`, the pretrained models, registry, anomaly scores, and screenshots also belong to the inherited implementation. They are not evidence of results on the user's data.

Dataset location, source, permitted use, schema, label definition, time semantics, currency, missing-value rules, sensitive fields, and limitations remain unknown. No substitute dataset or modified transaction values have been introduced. No model has been retrained and no performance metric has been measured for TransactionLens.

Before adaptation, record the supplied dataset's provenance and usage terms, inspect its schema without logging records, and agree which fields can be used for modeling and aggregate display. Keep the dataset outside Git, preferably outside the repository. Publish only approved aggregates and sanitized examples.

## Inherited functionality

| Component | Existing implementation and adaptation issue |
| --- | --- |
| Ingestion | DuckDB CSV loader assumes Time, V1–V28, Amount, Class and exactly 284,807 rows. |
| dbt | Bronze/silver/gold models assume PCA columns, binary labels, nonnegative amounts, and elapsed seconds. Elapsed seconds do not establish local clock time. |
| Features | Amount buckets and whole-dataset amount statistics need review; fit learned statistics only on the training split. |
| Training | PyTorch autoencoder and XGBoost scripts fit preprocessing before splitting. Review leakage, label availability, and split strategy before reporting results. |
| API | FastAPI assumes inherited numeric features, defaults missing PCA features to zero, and loads inherited model artifacts. |
| Dashboard | Streamlit includes inherited demo fallback, hardcoded transaction limits, and dataset-specific claims. |
| Agent | Fraud tools and case retrieval require review for sensitive record exposure and compatibility with the new schema. |
| Deployment | Docker and Kubernetes configuration are inherited; deployment has not been verified here. |

The pipeline runner currently prints training commands rather than executing them. Complete verification must include actual ingestion, dbt build/tests, fresh training, evaluation, API integration, and dashboard checks.

## Changes made in this adaptation session

- Added this repository audit and adaptation record.
- Added status notices to inherited README and model card so their results and license assertion are not presented as verified TransactionLens facts.
- Expanded Git exclusions for local datasets, credentials, model artifacts, results, and logs. Ignore rules do not remove files already tracked or erase history.

Updated the API branding and replaced the dashboard with a TransactionLens review layout, bounded batch input, explicit unavailable states, and provenance notes. Removed inherited screenshots, demo JSON/database, pretrained models/scaler, registry, and anomaly scores from the active checkout. Added DATASET.md and replaced historical README/model-card claims with current status. Dataset-dependent pipeline behavior has not yet been changed. These changes are preparation, not a completed personal implementation. Record future contributions by file and behavior, along with actual verification evidence.

## Pending implementation

After the full source dataset is supplied: implement the actual dataset contract across ingestion, dbt, training, API, and dashboard; redesign the dashboard as TransactionLens; train from scratch with leakage-safe evaluation; document measured results and limitations; run relevant tests and the full pipeline. Preserve required notices and existing Git history throughout.

## Verification in this session

Git whitespace checks passed and ignore rules were checked. Python syntax checks passed for the changed dashboard and API. Pytest could not run because pytest is absent from the bundled Python environment. Dashboard rendering and the full data/model pipeline remain unverified. No Git history was rewritten.

