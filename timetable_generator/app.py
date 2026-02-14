import streamlit as st
import pandas as pd

FILE_PATH = "EXAM 2"

def generate_timetable(course_input):
    df = pd.read_excel(FILE_PATH, sheet_name="Sheet1", header=None)

    df[0] = df[0].ffill()
    df[1] = df[1].ffill()

    courses = course_input.strip().upper().split()
    search_terms = []

    for course in courses:
        if len(course) >= 5:
            search_terms.append(course[:2] + " " + course[2:])
        else:
            search_terms.append(course)

    filtered = df[df.apply(
        lambda row: row.astype(str).str.contains('|'.join(search_terms), case=False).any(),
        axis=1
    )]

    result = filtered[[0, 1, 2, 3, 5]].copy()
    result.columns = ["Date", "Time", "Course Code", "Course Name", "Rooms"]

    return result


st.title("IITGN Exam Timetable Generator")

course_input = st.text_input(
    "Enter course codes separated by space (e.g., MA104 ES116)"
)

if st.button("Generate Timetable"):
    if course_input:
        result = generate_timetable(course_input)

        if result.empty:
            st.error("No matching courses found.")
        else:
            st.success("Timetable Generated")
            st.dataframe(result)
    else:
        st.warning("Please enter at least one course.")
