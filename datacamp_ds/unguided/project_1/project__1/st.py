import streamlit as st
import numpy as np
import pandas as pd
from data import BuildModel
from data import CustomerAnalytics


# -----------------------------------------------------------------------------
# HEADER
st.title('Customer Analytics App', anchor='center')
# --------------------------------------------------------------------------
# BODY


# ------------------------------------------------------------------------------
# SLIDER
st.sidebar.title('**User Input Features**')

# FORM attached to slider
with st.sidebar.form('User Input Features'):
    # Select Gender
    gender = st.selectbox(
        'Gender', ['Other', 'Male', 'Female'], key='Gender')
    # Select Relevant Experience
    rel_exp = st.selectbox(
        'Relevant Experience', ['Has relevant experience', 'No relevant experience'], key='relevant_experience')
    # Select Enrolled Uni
    enrolled_uni = st.selectbox(
        'Enrolled University', ['Full time course',
                                'Part time course', 'no_enrollment'], key='enrolled_university')
    # Select Education Level
    educa_level = st.selectbox(
        'Education Level', ['Primary School', 'High School', 'Graduate', 'Masters', 'Phd'], key='education_level')
    # Select Major Discipline
    mj_disc = st.selectbox('Major Discipline', [
                           'Arts', 'Business Degree', 'Humanities', 'No Major', 'Other', 'STEM'], key='major_discipline')
    # Select Experience
    yr_exp = st.selectbox('Experience', [
                          '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '>20'], key='experience')
    # Select Company Size
    cmp_size = st.selectbox('Company Size', [
                            '<10', '10-49', '50-99', '100-499', '500-999', '1000-4999', '5000-9999', '10000+'], key='company_size')
    # Select Company Type
    comp_type = st.selectbox('Company Type', [
        'Early Stage Startup', 'Funded Startup', 'NGO', 'Other', 'Public Sector', 'Pvt Ltd'], key='company_type')
    # Select Length of last job
    lst_new_jb = st.selectbox('How long since last job?', [
                              'never', '1', '2', '3', '4', '>4'], help='Number of years between current and last job', key='last_new_job')
    # Select Number of training hours
    train_hrs = st.number_input(
        'Enter Number of Hours Worked', 1, 100000, key='training_hours')
    # ADD a submit button
    submiited = st.form_submit_button('Submit')

# Create dataframe from user inputs
df = pd.DataFrame(st.session_state.to_dict(), index=[0])

if submiited:
    st.write(df.drop(columns='FormSubmitter:User Input Features-Submit'))
