import glob
import os
import re

import pandas as pd
import streamlit as st

md_files = sorted(
    [str(x.strip(".md")) for x in glob.glob1(f"content/", "*.md")]
)

content_list = [f"{x}" for x in md_files]

selected_content = st.selectbox(
    ("Select Policy details👇, these are md files extracted through google's bard"), content_list, key="day"#, on_change=update_params
)

# Display content
for x in content_list:
    if selected_content == x:
        with open(f"content/{x}.md", "r") as f:
            st.markdown(f.read())