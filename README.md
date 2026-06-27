# Nike Sales Management System

## 📌 Overview

The **Nike Sales Management System** is a Python-based application developed using **Streamlit**, **MySQL**, and **Pandas**. It allows users to upload Nike sales data from CSV files, store it in a MySQL database, manually add sales records, and view all stored records through an interactive web interface.

This project demonstrates CRUD operations, database connectivity, CSV data processing, and dashboard development using Streamlit.

---

## ✨ Features

* Upload sales data from CSV files
* Automatically create the MySQL table if it does not exist
* Store uploaded records in a MySQL database
* Add new sales records manually
* View all sales records in a tabular format
* Prevent duplicate records using the Order ID as the primary key
* Simple and user-friendly Streamlit interface

---

## 🛠️ Technologies Used

* Python 3.x
* Streamlit
* MySQL
* mysql-connector-python
* Pandas

---

## 📂 Project Structure

```
Nike-Sales-Management-System/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── sales_data.csv
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YourUsername/Nike-Sales-Management-System.git
```

### 2. Open the project

```bash
cd Nike-Sales-Management-System
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the MySQL database

```sql
CREATE DATABASE nike_sales;
```

### 5. Update the database credentials

Modify these values in `app.py`:

```python
host="localhost"
user="root"
password="your_password"
database="nike_sales"
```

### 6. Run the application

```bash
streamlit run app.py
```

---

## 📊 Functionalities

### Upload File

* Upload a CSV file containing Nike sales data.
* The application imports the data into MySQL.

### Add Record

* Enter sales details manually using the form.
* Save the record directly to the database.

### View Data

* Display all stored sales records in an interactive table.

---

## 📸 Future Improvements

* Edit existing records
* Delete records
* Search and filter functionality
* Sales dashboard with charts
* Authentication and user login
* Export data to Excel or CSV

---

## 👨‍💻 Author

Developed by **Your Name**

---

## 📄 License

This project is intended for educational purposes.
