import streamlit as st
import os

st.title("User Explanations Explorer")

# 2 tabs for MNIST and QuickDraw
tab_mnist, tab_quickdraw = st.tabs(["MNIST", "QuickDraw"])

# --- MNIST ---
with tab_mnist:
    col1, col2 = st.columns([1, 3])
    with col1:
        st.subheader("Controls")
        m_sample_idx = st.number_input("Sample Index", 0, 49, 0, key="mnist_idx")
        m_group_id = st.radio("Group", [1, 2], key="mnist_group")
    
    with col2:
        m_group_name = "Normal Edit" if m_group_id == 1 else "Min Edit"
        st.write(f"**Showing MNIST Sample {m_sample_idx} ({m_group_name})**")
        mnist_path = f"plots/mnist/mnist_group{m_group_id}_sample{m_sample_idx}.png"
        if os.path.exists(mnist_path):
            st.image(mnist_path, use_container_width=True)
        else:
            st.error("MNIST image not found.")

# --- QuickDraw ---
with tab_quickdraw:
    col1_qd, col2_qd = st.columns([1, 3])
    with col1:
            st.subheader("Controls")
            qd_sample_idx = st.slider("Sample ID", 0, 29, 0, key="qd_slider")
            st.info(f"Showing QuickDraw Sample {qd_sample_idx}")

    with col2:
        qd_path = f"plots/quickdraw/quickdraw_sample{qd_sample_idx}.png"
            
        if os.path.exists(qd_path):
            st.image(qd_path, use_container_width=True)
        else:
            st.error(f"File not found: {qd_path}")