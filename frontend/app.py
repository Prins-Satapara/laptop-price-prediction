import streamlit as st
import requests
from textwrap import dedent

from api_client import predict_laptop_price, check_api_health, get_model_info
from styles import load_css

# PAGE CONFIGURATION

st.set_page_config(
    page_title="LaptopIQ | Price Predictor",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# CUSTOM CSS
load_css()


# HEADER

st.markdown(
    """
    <div class="hero">
        <div class="hero-title">LaptopIQ</div>
        <div class="hero-subtitle">
            AI-powered laptop price estimation based on hardware specifications
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# API status

api_online = check_api_health()

status_col, info_col = st.columns([1, 5])

with status_col:

    if api_online:
        st.markdown(
            '<div class="api-status api-status-online">● API ONLINE</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div class="api-status api-status-offline">● API OFFLINE</div>',
            unsafe_allow_html=True
        )

with info_col:
    st.caption("Powered by FastAPI + Gradient Boosting")

st.divider()



# BRAND & SYSTEM

st.markdown(
    """
    <div class="section-header">
        <div class="section-title">Brand & System</div>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    brand = st.selectbox(
        "Brand",
        [
            "acer",
            "apple",
            "asus",
            "dell",
            "hp",
            "lenovo",
            "msi",
            "samsung",
            "tecno",
            "infinix"
        ]
    )

with col2:
    rating = st.slider(
        "Rating",
        min_value=0,
        max_value=100,
        value=64
    )

with col3:
    os = st.selectbox(
        "Operating System",
        [
            "windows",
            "mac",
            "dos",
            "android",
            "chrome",
            "ubuntu",
            "other"
        ]
    )

with col4:
    year_of_warranty = st.selectbox(
        "Warranty",
        [
            None,
            1.0,
            2.0,
            3.0
        ],
        format_func=lambda x: (
            "No information" if x is None else f"{int(x)} year"
        )
    )


# PERFORMANCE

st.markdown(
    """
    <div class="section-header">
        <div class="section-title">Performance</div>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    processor_brand = st.selectbox(
        "Processor Brand",
        [
            "intel",
            "amd",
            "apple",
            "other"
        ]
    )

with col2:
    processor_tier = st.selectbox(
        "Processor Tier",
        [
            "core i3",
            "core i5",
            "core i7",
            "core i9",
            "core ultra 7",
            "ryzen 3",
            "ryzen 5",
            "ryzen 7",
            "ryzen 9",
            "m1",
            "m2",
            "m3",
            "celeron",
            "pentium",
            "other"
        ]
    )

with col3:
    num_cores = st.number_input(
        "CPU Cores",
        min_value=1,
        max_value=32,
        value=8
    )

with col4:
    num_threads = st.number_input(
        "CPU Threads",
        min_value=1,
        max_value=64,
        value=16
    )


# MEMORY & STORAGE

st.markdown(
    """
    <div class="section-header">
        <div class="section-title">Memory & Storage</div>
    </div>
    """,
    unsafe_allow_html=True
)

# Row 1
col1, col2, col3 = st.columns(3)

with col1:
    ram_memory = st.number_input(
        "RAM (GB)",
        min_value=1.0,
        max_value=128.0,
        value=16.0,
        step=1.0
    )

with col2:
    primary_storage_type = st.selectbox(
        "Primary Storage Type",
        ["SSD", "HDD"]
    )

with col3:
    primary_storage_capacity = st.number_input(
        "Primary Storage Capacity (GB)",
        min_value=0.0,
        max_value=8192.0,
        value=512.0,
        step=128.0
    )


# Row 2
col1, col2 = st.columns(2)

with col1:
    secondary_storage_type = st.selectbox(
        "Secondary Storage Type",
        [
            "No secondary storage",
            "SSD"
        ]
    )

with col2:
    secondary_storage_capacity = st.number_input(
        "Secondary Storage Capacity (GB)",
        min_value=0.0,
        max_value=8192.0,
        value=0.0,
        step=128.0
    )

# GRAPHICS

st.markdown(
    """
    <div class="section-header">
        <div class="section-title">Graphics</div>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    gpu_brand = st.selectbox(
        "GPU Brand",
        [
            "intel",
            "amd",
            "apple",
            "nvidia",
            "arm"
        ]
    )

with col2:
    if gpu_brand == "nvidia":
        gpu_type = st.selectbox(
            "GPU Type",
            ["dedicated"]
        )

    elif gpu_brand == "apple":
        gpu_type = st.selectbox(
            "GPU Type",
            ["apple"]
        )

    else:
        gpu_type = st.selectbox(
            "GPU Type",
            ["integrated", "dedicated"]
        )

with col3:
    is_touch_screen = st.toggle(
        "Touch Screen",
        value=False
    )

# DISPLAY

st.markdown(
    """
    <div class="section-header">
        <div class="section-title">Display</div>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    display_size = st.number_input(
        "Display Size (inches)",
        min_value=10.0,
        max_value=20.0,
        value=15.6,
        step=0.1
    )

with col2:
    resolution_width = st.number_input(
        "Resolution Width",
        min_value=640,
        max_value=7680,
        value=1920
    )

with col3:
    resolution_height = st.number_input(
        "Resolution Height",
        min_value=480,
        max_value=4320,
        value=1080
    )


# PREDICT

st.divider()

predict_button = st.button(
    "Estimate Laptop Price",
    type="primary",
    use_container_width=True
)


# PREDICTION
if predict_button:
    laptop_data = {
        "brand": brand,
        "Rating": rating,
        "processor_brand": processor_brand,
        "processor_tier": processor_tier,
        "num_cores": num_cores,
        "num_threads": num_threads,
        "ram_memory": ram_memory,
        "primary_storage_type": primary_storage_type,
        "primary_storage_capacity": primary_storage_capacity,
        "secondary_storage_type": secondary_storage_type,
        "secondary_storage_capacity": secondary_storage_capacity,
        "gpu_brand": gpu_brand,
        "gpu_type": gpu_type,
        "is_touch_screen": is_touch_screen,
        "display_size": display_size,
        "resolution_width": resolution_width,
        "resolution_height": resolution_height,
        "OS": os,
        "year_of_warranty": year_of_warranty
    }

    try:
        with st.spinner("Analyzing specifications..."):
            result = predict_laptop_price(laptop_data)

        predicted_price = result["predicted_price"]

        # Removed the leading spaces inside the f-string
        st.markdown(
            f"""
                <div class="prediction-card">
                    <div class="prediction-label">
                        Estimated Laptop Price
                    </div>
                    <div class="prediction-price">
                        ₹{predicted_price:,.0f}
                    </div>
                    <div class="prediction-model">
                        Gradient Boosting Regressor • INR
                    </div>
                </div>
            """,
            unsafe_allow_html=True
        )

    except Exception as e:
        st.error(
            "Unable to generate prediction. "
            "Please make sure the FastAPI server is running."
        )
        st.caption(str(e))
        

# =========================================================
# MODEL DETAILS
# =========================================================

st.divider()

if api_online:

    model_info = get_model_info()

    if model_info:

        st.markdown(
            dedent(
                """
                <div class="model-details-title">
                    Model Details
                </div>
                """
            ),
            unsafe_allow_html=True
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.caption("Model")
            st.write(model_info["model"])

        with col2:
            st.caption("R² Score")
            st.write(
                f"{model_info['metrics']['r2']:.4f}"
            )

        with col3:
            st.caption("MAE")
            st.write(
                f"₹{model_info['metrics']['mae']:,.0f}"
            )

        with col4:
            st.caption("RMSE")
            st.write(
                f"₹{model_info['metrics']['rmse']:,.0f}"
            )     

        
# FOOTER

st.markdown(
    """
    <div class="footer">
        LaptopIQ • Machine Learning Price Estimation
    </div>
    """,
    unsafe_allow_html=True
)