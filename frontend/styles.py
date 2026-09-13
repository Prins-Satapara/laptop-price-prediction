import streamlit as st


def load_css():
    st.markdown(
        """
        <style>

        /* Overall page */
        .stApp {
            background-color: #0f1117;
        }

        .block-container {
            max-width: 1200px;
            padding-top: 1.5rem;
            padding-bottom: 2.5rem;
        }

        /* Hero section */
        .hero {
            padding: 10px 0 8px 0;
        }

        .hero-title {
            font-size: 42px;
            font-weight: 700;
            margin-bottom: 4px;
        }

        .hero-subtitle {
            font-size: 17px;
            color: #9ca3af;
        }

        /* Section headers */
        .section-header {
            margin-top: 24px;
            margin-bottom: 12px;
            padding-bottom: 8px;
            border-bottom: 1px solid #262b35;
        }

        .section-title {
            font-size: 21px;
            font-weight: 600;
            letter-spacing: -0.2px;
        }

        /* API Status */
        .api-status {
            display: inline-block !important;
            padding: 6px 12px !important;
            border-radius: 20px !important;
            font-size: 13px !important;
            font-weight: 600 !important;
            line-height: 1.2 !important;
        }
        
        .api-status-online {
            background-color: #13251c !important;
            color: #4ade80 !important;
        }
        
        .api-status-offline {
            background-color: #2a1717 !important;
            color: #f87171 !important;
        }

        /* Prediction */
        .prediction-card {
            background-color: #171a21;
            border: 1px solid #303642;
            border-radius: 16px;
            padding: 28px;
            text-align: center;
            margin-top: 20px;
        }

        .prediction-label {
            color: #9ca3af;
            font-size: 15px;
        }

        .prediction-price {
            font-size: 46px;
            font-weight: 700;
            margin: 6px 0;
        }

        .prediction-model {
            color: #9ca3af;
            font-size: 13px;
        }

        /* Model details */
        .model-details {
            text-align: center;
            margin-top: 8px;
            margin-bottom: 20px;
        }

        .model-details-title {
            font-size: 14px;
            font-weight: 600;
            color: #9ca3af;
            margin-bottom: 6px;
        }

        .model-details-content {
            font-size: 13px;
            color: #6b7280;
        }

        /* Footer */
        .footer {
            text-align: center;
            color: #6b7280;
            font-size: 13px;
            margin-top: 30px;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )