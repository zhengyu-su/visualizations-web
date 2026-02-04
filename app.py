import streamlit as st
import os

st.title("MNIST User Explanations Explorer")

# Create sidebar for user inputs
sample_idx = st.sidebar.slider("Select sample index (Sample Index)", 0, 49, 0)
group_id = st.sidebar.radio("Select group (Group)", [1, 2])

st.header(f"Sample {sample_idx} - Group {group_id}")

# Show the corresponding image
img_path = f"plot_cache/sample_{sample_idx}.png"
if os.path.exists(img_path):
    st.image(img_path, use_column_width=True)
else:
    st.error("No image found for the selected sample.")

# Print softmax scores
st.subheader("Softmax Scores")