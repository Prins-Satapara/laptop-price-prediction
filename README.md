# Laptop Price Prediction

Predicts laptop prices (₹) from hardware specs using regression models.

> **Status: in progress.** The ML pipeline (EDA → cleaning → features →
> training → tuning) is done. FastAPI, Streamlit, and Docker are not built yet.

## Pipeline

| Step | Notebook | Output |
|---|---|---|
| 1. EDA | `notebooks/01_eda.ipynb` | insights only |
| 2. Cleaning | `notebooks/02_data_cleaning.ipynb` | `data/processed/laptops_cleaned.csv` |
| 3. Feature engineering | `notebooks/03_feature_engineering.ipynb` | `data/processed/laptops_features.csv` |
| 4. Model training | `notebooks/04_model_training.ipynb` | `src/models/gb_baseline.pkl`, `preprocessor.pkl` |
| 5. Tuning | `notebooks/05_model_tuning.ipynb` | `src/models/laptop_price_pipeline.pkl` |

Run the notebooks in order (each reads the previous step's output). All paths
are relative, so run them from inside `notebooks/`.

## Setup

```bash
pip install -r requirements.txt
```

## Model

Gradient Boosting Regressor. Optuna tuning didn't beat the hand-picked
baseline, so the baseline is the final model. See `05_model_tuning.ipynb`
for the comparison.

## TODO

- [ ] FastAPI serving endpoint (`app/`)
- [ ] Streamlit UI (`streamlit/`)
- [ ] Dockerize
