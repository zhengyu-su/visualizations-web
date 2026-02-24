import streamlit as st
import os

st.set_page_config(layout="wide")
st.title("User Explanations Explorer")

# paths prefix for different models
MODELS = {
    "Original Model": "plots",
    "New Torch Model": "plots_torch"
}

# 1. Dataset Tabs
tab_mnist, tab_quickdraw = st.tabs(["MNIST", "QuickDraw"])

# --- MNIST ---
with tab_mnist:
    # Tabs for different models
    m_model_tab1, m_model_tab2 = st.tabs(["Original Model", "New Torch Model"])
    
    # 1. MNIST - Original Model
    with m_model_tab1:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.subheader("Controls")
            idx = st.slider("Sample Index", 0, 49, 0, key="m_orig_slider")
            grp = st.radio("Group", [1, 2], key="mnist_group")
        with col2:
            m_group_name = "Normal Edit" if grp == 1 else "Min Edit"
            st.write(f"**Showing MNIST Sample {idx} ({m_group_name})**")
            mnist_path = f"plots/mnist_ssim/mnist_group{grp}_sample{idx}.png"
            if os.path.exists(mnist_path):
                st.image(mnist_path, use_container_width=True)
            else:
                st.error("MNIST image not found.")

    # 2. MNIST - New Torch Model
    with m_model_tab2:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.subheader("Controls")
            idx_t = st.slider("Sample Index", 0, 49, 0, key="m_torch_slider")
            grp_t = st.radio("Group", [1, 2], key="mnist_group_t")
        with col2:
            m_group_name = "Normal Edit" if grp_t == 1 else "Min Edit"
            st.write(f"**Torch Model Result Sample {idx_t} ({m_group_name})**")
            path_t = f"plots/torch/mnist/mnist_group{grp_t}_sample{idx_t}.png"
            if os.path.exists(path_t):
                st.image(path_t, use_container_width=True)
            else:
                st.info("MNIST image not found.")

# --- QuickDraw ---
with tab_quickdraw:
    
    col1_qd, col2_qd = st.columns([1, 3])
    with col1_qd:
        st.subheader("Controls")
        qd_sample_idx = st.slider("Sample ID", 0, 29, 0, key="qd_slider")

    with col2_qd:
        qd_path = f"plots/quickdraw_ssim/quickdraw_sample{qd_sample_idx}.png"
        st.write(f"**Showing QuickDraw Sample {qd_sample_idx}**")

            
        if os.path.exists(qd_path):
            st.image(qd_path, use_container_width=True)
        else:
            st.error(f"File not found: {qd_path}")
