# TransactionLens model card

Status: untrained adaptation, October 1, 2026.

Inherited pretrained models and measured outputs have been removed from the active checkout. No fresh metrics have been measured. The original model implementations are a PyTorch autoencoder and XGBoost classifier, with SHAP contributions and registry management.

Training is pending the full source CSV. Before reporting results, fit imputation, scaling, and learned feature statistics on training data only; use a held-out split appropriate to the observation order; select thresholds on validation data; and evaluate both models on the same untouched test set. Report ROC-AUC, average precision, precision, recall, F1, class support, threshold, random seed, and split policy from actual outputs. Do not promote a model using training-set scores.

The public ULB/Worldline benchmark is historical and PCA-anonymized. Scores do not establish fraud, SHAP components lack original business meanings, and demographic fairness cannot be measured without relevant attributes. Production readiness, latency, and cross-population generalization have not been evaluated.

No software license is asserted for inherited code: the user confirmed modification permission, but license text was not found. See PROJECT_STATUS.md and DATASET.md for provenance and attribution.
