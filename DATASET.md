# Dataset record

## Source and permitted use

The user selected the same dataset used by the inherited project: ULB / Worldline Credit Card Fraud Detection, https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud. This is a public benchmark, not a personally collected dataset. The source page identifies its license category as Database: Open Database, Contents: Database Contents. Keep the source attribution and retain the exact download's terms and version information before redistribution. No downloaded license document is available in this checkout.

The full source file is missing. File hash, download date, actual row count, validation results, and split assignments remain unmeasured. The former demo database was removed rather than substituted for the full benchmark.

## Expected source schema

These expectations come from inherited code and source documentation; they must be checked against the supplied file.

| Field | Meaning | Validation to complete |
| --- | --- | --- |
| Time | Seconds since the first transaction | Numeric, finite, nonnegative; not a known local clock |
| V1–V28 | Anonymous PCA components | Numeric and finite; no invented business names |
| Amount | Transaction amount | Numeric, finite, nonnegative; confirm units from source |
| Class | Supplied fraud label | Integer 0 or 1, non-null |
| transaction_id | Locally generated row identifier | Stable within the imported file; unique, non-null |

Never change source amounts or labels merely to make this project appear original. Derived features belong in transformations, with their definitions recorded. Test fixtures may be synthetic but must be identified as such and excluded from reported evaluation.

## Limitations and handling

The benchmark is historical, spans a short observation window, and is severely imbalanced. PCA obscures original feature meanings and demographic attributes are absent. Elapsed time modulo a day does not establish local hour or nighttime. Sampling only demo frauds and selected legitimate records changes the class distribution and is unsuitable as a replacement training/evaluation set.

Keep raw records, local databases, trained artifacts, retrieval indexes, logs, and secrets outside Git. Do not log record contents or credentials, and use only approved aggregate displays for shared screenshots. Record dataset identity and training/evaluation provenance without publishing raw records.
