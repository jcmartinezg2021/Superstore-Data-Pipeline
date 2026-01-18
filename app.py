import streamlit as st
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col

# 1. Setup Connection/Streamlit Secrets
def create_session():
    # Streamlit pull from  "Secrets" settings
    return Session.builder.configs(st.secrets["snowflake"]).create()

st.set_page_config(page_title="Superstore Performance", layout="wide")
st.title("Superstore Executive Performance")

session = create_session()

# 2. Sidebar Filter
st.sidebar.header("Filter Options")
source_table = "SNOWFLAKE_LEARNING_DB.DBT_STAGING.MART_REGIONAL_PERFORMANCE"

#unique regions for filter
region_list = session.table(source_table).select("REGION").distinct().to_pandas()
selected_region = st.sidebar.multiselect("Select Region(s)", options=region_list["REGION"].tolist(), default=region_list["REGION"].tolist())

# 3. Filtered Data retrieval
raw_df = session.table(source_table).filter(col("REGION").in_(selected_region)).to_pandas()

# 4. KPIs/Charts
col1, col2, col3 = st.columns(3)
with col1: st.metric("Total Sales", f"${raw_df['TOTAL_SALES'].sum():,.0f}")
with col2: st.metric("Total Profit", f"${raw_df['TOTAL_PROFIT'].sum():,.0f}")
with col3: st.metric("Avg Margin", f"{(raw_df['AVG_PROFIT_MARGIN'].mean() if not raw_df.empty else 0):.1%}")

st.divider()
vis_col1, vis_col2 = st.columns(2)
with vis_col1:
    st.subheader("Profit by Region")
    st.bar_chart(data=raw_df, x="REGION", y="TOTAL_PROFIT", color="CATEGORY")
with vis_col2:
    st.subheader("Sales vs. Profit Margin")
    st.scatter_chart(data=raw_df, x="TOTAL_SALES", y="AVG_PROFIT_MARGIN", color="CATEGORY")

st.dataframe(raw_df, use_container_width=True)