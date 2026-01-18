# Superstore-Data-Pipeline
This project demonstrates a data pipeline built for the interview assessment. It transforms raw retail data into an interactive executive dashboard using a modern data stack.


### 🔗 [View Live Interactive Dashboard](https://superstore-data-pipeline-jrn8sxurtzyjmr4yh6umkp.streamlit.app/)

Important: Use the link above to interact with the real-time data visualizations.

Architecture & Tools

-Data Warehouse: Snowflake (Storage and Compute)

-Transformation: dbt Cloud (Medallion Architecture: Staging and Mart layers)

-Visualization: Streamlit (Interactive Python-based dashboard)

-Version Control: GitHub (Branching, Pull Requests, and Documentation)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Key Features

1. Data Transformation (dbt)
I implemented a Medallion Architecture to ensure data quality and scalability:

-Staging Layer (stg_superstore): Handled complex data cleaning, we are transforming Profit_Margin and Target_Profit_Margin from text strings with percentage signs into numeric floats for analysis.

-Mart Layer (mart_regional_performance): Aggregated business-ready metrics including Total Sales, Total Profit, and Average Margin by Region and Category.



2. Data Governance & Testing
-Documentation: Full model and column-level descriptions are provided in the schema.yml file.

-Implemented not_null and uniqueness tests to ensure the integrity of the profit margin calculations before they reached the dashboard.



3. Interactive Analytics (Streamlit)
The final deliverable is a live dashboard that pulls data directly from the Snowflake Mart layer. It includes:

-Interactive Filtering: Users can filter performance by one or multiple regions via the sidebar.

-Executive KPIs: Real-time calculation of Total Sales, Total Profit, and Profit Margins.

-Visual Insights: Automated bar and scatter charts for rapid regional performance comparisons.


