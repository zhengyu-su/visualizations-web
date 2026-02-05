import streamlit as st
import os

st.title("MNIST User Explanations Explorer")

# Create sidebar for user inputs
sample_idx = st.sidebar.slider("Select sample index", 0, 49, 0)
group_id = st.sidebar.radio("Select group", [1, 2])

group_name = "Normal Edit" if group_id == 1 else "Min Edit"
st.header(f"Sample {sample_idx} - Group {group_name}")

# Show the corresponding image
img_path = f"plots/mnist/mnist_group{group_id}_sample{sample_idx}.png"
if os.path.exists(img_path):
    st.image(img_path, use_column_width=True)
else:
    st.error("No image found for the selected sample.")

# st.subheader("Something Else")