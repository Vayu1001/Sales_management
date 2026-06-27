import mysql.connector
import streamlit as st
import pandas as pd
import io

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Your password",
    database="nike_sales"
)

cursor = conn.cursor()
print("Connected successfully")

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales_data (
    Order_ID VARCHAR(50) PRIMARY KEY,
    Gender_Category VARCHAR(20),
    Product_Line VARCHAR(100),
    Product_Name VARCHAR(255),
    Size VARCHAR(20),
    Units_Sold INT,
    MRP DECIMAL(10,2),
    Discount_Applied DECIMAL(10,2),
    Order_Date DATE,
    Revenue DECIMAL(12,2),
    Sales_Channel VARCHAR(100),
    Region VARCHAR(100),
    Profit DECIMAL(12,2)
)
""")
conn.commit()
st.title("Nike Sales Management System")

menu = st.sidebar.selectbox(
    "Choose Option",
    ["Upload File", "Add Record", "View Data"]
)

if menu == "Upload File":

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["xls", "xlsx", "csv"]   
    )

    if uploaded_file:
        df = pd.read_csv(io.BytesIO(uploaded_file.read()))

        df["Order_Date"] = pd.to_datetime(
            df["Order_Date"]
        ).dt.date

        st.dataframe(df.head())

        if st.button("Upload to MySQL"):

            for _, row in df.iterrows():

                cursor.execute("""
                INSERT IGNORE INTO sales_data
                (Order_ID, Gender_Category, Product_Line, Product_Name,
                Size, Units_Sold, MRP, Discount_Applied, Order_Date,
                Revenue, Sales_Channel, Region, Profit)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """,
                (
                    row["Order_ID"],
                    row["Gender_Category"],
                    row["Product_Line"],
                    row["Product_Name"],
                    row["Size"],
                    row["Units_Sold"],
                    row["MRP"],
                    row["Discount_Applied"],
                    row["Order_Date"],
                    row["Revenue"],
                    row["Sales_Channel"],
                    row["Region"],
                    row["Profit"]
                ))

            conn.commit()

            st.success("CSV data uploaded successfully!")

if menu == "Add Record":

    st.subheader("Add New Sale")

    with st.form("add_form"):

        order_id = st.text_input("Order ID")
        gender = st.text_input("Gender Category")
        product_line = st.text_input("Product Line")
        product_name = st.text_input("Product Name")
        size = st.text_input("Size")

        units_sold = st.number_input(
            "Units Sold",
            min_value=0
        )

        mrp = st.number_input(
            "MRP",
            min_value=0.0
        )

        discount = st.number_input(
            "Discount Applied",
            min_value=0.0
        )

        order_date = st.date_input("Order Date")

        revenue = st.number_input(
            "Revenue",
            min_value=0.0
        )

        sales_channel = st.text_input(
            "Sales Channel"
        )

        region = st.text_input("Region")

        profit = st.number_input(
            "Profit",
            min_value=0.0
        )

        submit = st.form_submit_button(
            "Add Record"
        )

        if submit:

            cursor.execute("""
            INSERT INTO sales_data
            (Order_ID, Gender_Category,
             Product_Line, Product_Name,
             Size, Units_Sold, MRP,
             Discount_Applied, Order_Date,
             Revenue, Sales_Channel,
             Region, Profit)

            VALUES
            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,

            (
                order_id,
                gender,
                product_line,
                product_name,
                size,
                units_sold,
                mrp,
                discount,
                order_date,
                revenue,
                sales_channel,
                region,
                profit
            ))

            conn.commit()

            st.success("Record added successfully!")

if menu == "View Data":

    cursor.execute("SELECT * FROM sales_data")

    data = cursor.fetchall()

    columns = [
        "Order_ID",
        "Gender_Category",
        "Product_Line",
        "Product_Name",
        "Size",
        "Units_Sold",
        "MRP",
        "Discount_Applied",
        "Order_Date",
        "Revenue",
        "Sales_Channel",
        "Region",
        "Profit"
    ]

    df = pd.DataFrame(data, columns=columns)

    st.dataframe(df)