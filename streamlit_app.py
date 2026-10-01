"""TransactionLens analyst workspace; scores come only from the configured API."""
import os
import pandas as pd
import plotly.express as px
import requests
import streamlit as st

API_BASE = os.getenv("STREAMLIT_API_URL", "http://localhost:8000")


def api_get(path, base_url):
    try:
        response = requests.get(f"{base_url.rstrip('/')}{path}", timeout=10)
        if response.status_code == 404:
            return None, "Transaction not found."
        response.raise_for_status()
        return response.json(), None
    except (requests.RequestException, ValueError):
        return None, "Scoring service unavailable. Check the service and fresh model artifacts."


st.set_page_config(page_title="TransactionLens", page_icon="◈", layout="wide")
st.markdown("""
<style>
.stApp { background: #f5f7fb; color: #17243b; }
[data-testid="stSidebar"] { background: #eaf0f8; }
[data-testid="stMetric"] { background: white; border: 1px solid #dce4ef;
    border-radius: 14px; padding: 18px; }
h1, h2, h3 { letter-spacing: -0.025em; }
.stButton > button { border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("◈ TransactionLens")
    st.caption("Transaction review workspace")
    api_url = st.text_input("Scoring service", value=API_BASE)
    health, error = api_get("/health", api_url)
    ready = bool(health and health.get("ae_loaded") and health.get("xgb_loaded") and health.get("champion"))
    st.success("Models available") if ready else st.warning("Awaiting fresh training")
    st.divider()
    st.caption("Dataset: ULB / Worldline credit card transactions. Public benchmark; source values are preserved.")

st.title("Follow the risk. Inspect the evidence.")
st.caption("Review transactions and model explanations from your local scoring service.")
if not ready:
    st.info("No verified trained run is available here. Supply the full source CSV, complete training and evaluation, then start the API. No demo scores are substituted.")

review, batch, provenance = st.tabs(["Review a transaction", "Review a batch", "Data & methodology"])
with review:
    left, right = st.columns([1, 2], gap="large")
    with left:
        st.subheader("Select a transaction")
        transaction_id = st.number_input("Transaction ID", min_value=0, step=1, help="Identifier assigned during ingestion.")
        submitted = st.button("Assess risk", type="primary", disabled=not ready, use_container_width=True)
    with right:
        st.subheader("Risk assessment")
        if submitted:
            result, error = api_get(f"/transaction/{int(transaction_id)}", api_url)
            if error:
                st.error(error)
            elif result:
                c1, c2, c3 = st.columns(3)
                c1.metric("Model score", f"{result['risk_score']:.3f}")
                c2.metric("Review flag", "High risk" if result["is_high_risk"] else "Below threshold")
                c3.metric("Model", result.get("champion_model") or "Unavailable")
                st.caption("A model score is not proof of fraud. The inherited API's percentile field is omitted until its calculation is validated.")
                factors = pd.DataFrame(result.get("top_risk_factors", []))
                if not factors.empty:
                    figure = px.bar(factors, x="shap_value", y="feature", orientation="h", color="direction",
                                    color_discrete_map={"increases": "#da6657", "decreases": "#237d95"},
                                    labels={"shap_value": "Contribution to model output", "feature": "Feature"})
                    figure.update_layout(template="plotly_white", margin=dict(l=0, r=20, t=20, b=0))
                    st.plotly_chart(figure, use_container_width=True)
                st.caption("V1–V28 are anonymous PCA components; their original business meanings are unavailable.")
        else:
            st.caption("Choose an ID to inspect its score and directional feature contributions.")

with batch:
    st.subheader("Review a selection")
    identifiers = st.text_area("Transaction IDs, one per line", value="", placeholder="Enter IDs from your ingested dataset")
    st.caption("Up to 100 IDs per review. Summary values describe only this selection.")
    if st.button("Assess selection", disabled=not ready, type="primary"):
        lines = [line.strip() for line in identifiers.splitlines() if line.strip()]
        if not lines or len(lines) > 100 or any(not line.isascii() or not line.isdecimal() for line in lines):
            st.error("Enter between 1 and 100 nonnegative integer IDs.")
        else:
            results, failures = [], 0
            for identifier in dict.fromkeys(lines):
                record, error = api_get(f"/transaction/{int(identifier)}", api_url)
                if error or not record:
                    failures += 1
                else:
                    results.append({"transaction_id": record["transaction_id"], "risk_score": record["risk_score"],
                                    "review_flag": bool(record["is_high_risk"])})
            if results:
                frame = pd.DataFrame(results)
                c1, c2, c3 = st.columns(3)
                c1.metric("Scored", len(frame))
                c2.metric("Flagged", int(frame.review_flag.sum()))
                c3.metric("Mean model score", f"{frame.risk_score.mean():.3f}")
                st.plotly_chart(px.histogram(frame, x="risk_score", color_discrete_sequence=["#237d95"],
                                            template="plotly_white"), use_container_width=True)
                st.dataframe(frame, use_container_width=True, hide_index=True)
            if failures:
                st.warning(f"{failures} transaction(s) unavailable.")

with provenance:
    st.subheader("Data provenance")
    st.markdown("Source: [ULB / Worldline Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud). The full source CSV is currently missing from this checkout. TransactionLens continues to use this public benchmark; it is not a personally collected dataset.")
    st.markdown("Time measures seconds since the first observation, not a known local time. Amount is a transaction amount; Class is the supplied binary fraud label. V1–V28 are PCA components. The historical sample and anonymous features limit generalization and prevent demographic fairness evaluation.")
    st.subheader("Implementation record")
    st.markdown("Inherited: DuckDB ingestion, dbt models, autoencoder and XGBoost training, FastAPI scoring, case retrieval, and deployment manifests. Changed in this adaptation: TransactionLens branding, this review layout, removal of demo fallback and inherited artifacts, and provenance documentation. Contributor history is preserved.")
    st.subheader("Evaluation status")
    st.write("Fresh training and end-to-end evaluation are pending. No AUC, F1, latency, or fairness result is claimed for this adaptation.")
