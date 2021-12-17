# Test program

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import streamlit as st

st.markdown("""---""")
st.markdown("""Hi- This is test""")

# write the header
col1, col2, col3 = st.columns(3)
col1.write("### Spend")
col2.write("### Redemtion Rate")
col3.write("### Average Cost")
