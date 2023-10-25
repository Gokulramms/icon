import streamlit as st
import mysql.connector
import pandas as pd
import random
import string
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to connect to the database
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",  # Replace with your MySQL server host
            user="root",       # Replace with your MySQL username
            password="Gokul@sgr123",  # Replace with your MySQL password
            database="firstproject"  # Replace with your MySQL database name
        )
        c = conn.cursor()
        return conn, c
    except mysql.connector.Error as e:
        st.error(f"Error connecting to the database: {e}")
        st.stop()

# Function to create the "students_of_toh" table if it doesn't exist
def create_table_if_not_exists(c):
    c.execute("""
        CREATE TABLE IF NOT EXISTS students_of_toh (
            rollno VARCHAR(10) NOT NULL,
            name VARCHAR(45) NOT NULL,
            kit_no TEXT(10) NOT NULL,
            date DATE NOT NULL,
            mail TEXT(25) NOT NULL,
            year INT NOT NULL,
            PRIMARY KEY (rollno)
        )
    """)

# Function to add a student to the database
def add_student(rollno, name, kitno, date, mail, year):
    try:
        c.execute("INSERT INTO students_of_toh (rollno, name, kit_no, date, mail, year) VALUES (%s, %s, %s, %s, %s, %s)", (rollno, name, kitno, date, mail, year))
        conn.commit()
        return True
    except mysql.connector.Error as e:
        st.error(f"Error adding student to the database: {e}")
        return False

# Function to remove a student from the database
def remove_student(rollno):
    try:
        c.execute("DELETE FROM students_of_toh WHERE rollno=%s", (rollno,))
        conn.commit()
        if c.rowcount > 0:
            return True
        else:
            return False
    except mysql.connector.Error as e:
        st.error(f"Error removing student from the database: {e}")
        return False

# Home Page
def home_page():
    st.header("Tower Of Hanoi Management")
    options = ["ISSUING", "RETURNING", "STUDENT LIST"]
    choice = st.sidebar.selectbox("Select an option", options)

    if choice == "ISSUING":
        issuing_page()
    elif choice == "RETURNING":
        returning_page()
    elif choice == "STUDENT LIST":
        student_list_page()

# Issuing Page
def issuing_page():
    st.header("ISSUING")
    col0, col1, col2, col3 = st.columns(4)
    col4, col5 = st.columns(2)
    roll = col0.text_input("Roll No:")
    name_input = col1.text_input("Name:")
    age_input = col2.text_input("TOH NUMBER:")
    date_input = col3.date_input("Date")
    mail = col4.text_input("ENTER STUDENT EMAIL:")
    year = col5.text_input("Enter Your Year:")
    add_button = st.button("SUBMIT")

    if add_button and name_input and age_input and date_input:
        # Check if the name already exists in the database
        c.execute("SELECT COUNT(*) FROM students_of_toh WHERE name=%s", (name_input,))
        result = c.fetchone()
        if result[0] > 0:
            st.warning("Student with the given name already exists!")
        else:
            date_str = date_input.strftime("%Y-%m-%d")
            age_input = int(age_input)  # Convert to int
            if add_student(roll, name_input, age_input, date_str, mail, year):
                st.success("Student added successfully!")

                # Sending email to the student
                send = 'iconcreationai81@gmail.com'
                pas = 'tetkkfrshnidygvq'
                rec = mail
                message = MIMEMultipart()
                message['From'] = send
                message['To'] = rec
                message['Subject'] = 'TOWER OF HANOI MANAGEMENT'
                ans = f'''Hello {name_input}... That you are getting a tower of hanoi kit from the office. Your kit number is {age_input}
so keep the kit safe and use it in an efficient manner.

                Thank you...
                From:
                Tower Of Hanoi Management Team
                {date_input}'''

                message.attach(MIMEText(ans, 'plain'))
                session = smtplib.SMTP('smtp.gmail.com', 587)
                session.starttls()
                session.login(send, pas)
                text = message.as_string()
                session.sendmail(send, rec, text)
                session.quit()
                st.subheader('Mail sent to Student')

# Returning Page
def returning_page():
    st.header("RETURNING")
    roll_no_to_del = st.text_input("Enter the Roll No of the student:")
    remove_button = st.button("REMOVE")

    if remove_button and roll_no_to_del:
        if remove_student(roll_no_to_del):
            st.warning("Student removed successfully!")
        else:
            st.error("Student with the given name not found.")

# Student List Page
def student_list_page():
    st.header("Student List")
    c.execute("SELECT rollno, name, kit_no, date, mail, year FROM students_of_toh")
    persons = c.fetchall()
    if persons:
        df = pd.DataFrame(persons, columns=["RollNo", "Name", "KIT NO:", "Date", "Mail", "Year"])
        st.dataframe(df)
    else:
        st.info("No Students found.")

# Login Function
def login():
    st.title("Tower Of Hanoi Management Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Replace with your actual login credentials
        if username == "Kitestaff" and password == "kite@123":
            st.success("Login successful!")
            home_page()
        else:
            st.error("Invalid credentials. Please try again.")

# Main Function
if __name__ == "__main__":
    conn, c = connect_to_database()
    create_table_if_not_exists(c)
    login()
    conn.close()
