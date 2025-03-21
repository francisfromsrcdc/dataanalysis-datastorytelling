import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def load_data():
    data = pd.read_csv(
       "/data/Students_Grading_Dataset.csv",
        encoding='ISO-8859-1'
    )
    return data

#data = load_data()
#with st.expander("View Data"):
    #st.dataframe(data)
    #st.caption("*CAPTION HERE")

def introduction():
    st.title("Comparing Students' Performance in School")

    st.subheader("Research Objectives")

    st.subheader("Methodology")
    st.markdown(
        """
        This study involves conducting a series of experiments on a dataset sourced from Kaggle. The objective here is to analyze and compare various aspects of student performance, drawing insights from the visualized results.
        """
    )

    st.subheader("Scope and Limitations")
    st.markdown(
        """
        The dataset utilized in this analysis is derived from real-world data; however, it is important to note that certain elements have been modified for privacy reasons. Specifically, names and email addresses have been altered, and additional columns and rows have been introduced, which may or may not influence the results. The raw dataset is provided below:
        """
    )

    data = load_data()
    with st.expander("View Data"):
        st.dataframe(data)
        st.caption("*Source: Kaggle*")
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
def visualization():
    data = load_data()

    st.title("Data Visualization")
    limited_data = data.head(100)
    st.dataframe(limited_data)
    st.markdown("This is a smaller version of the dataset, narrowed down to 100 students.")

    # LINE CHART START
    st.subheader("Student Ages")
    fig = px.line(limited_data, x=limited_data.index, y='Age', title='Student Age Chart', markers=True)
    fig.update_layout(xaxis_title='Student Number')
    st.plotly_chart(fig)
    st.markdown("The plot illustrates the age distribution of the students from the smaller sample that we have above. From this data, we can conclude that there are no students younger than 18 or older than 24. Now, to make this more meaningful, let's separate the students by their gender and get the average value of both sides of the spectrum.")

    # BAR CHART 1 START
    age_gender_data = limited_data.groupby('Gender')['Age'].mean().reset_index()

    fig = px.bar(age_gender_data, x='Gender', y='Age', title='Age and Gender Chart', 
             labels={'Age': 'Average Age', 'Gender': 'Gender'},
             color='Gender', 
             color_discrete_sequence=['red', 'blue'])

    st.subheader("Student Average Ages by Gender")
    st.plotly_chart(fig)
    st.markdown("The chart above now clearly shows the average age out of this watered down dataset. On average, female students age ~21.48 years old, meanwhile male students age ~20.7 years old. Okay, let's try and gather more information; we don't know what departments the students are tied to so let's sort them based on that.")

    # PIE CHART 1 START
    department_counts = limited_data['Department'].value_counts().reset_index()
    department_counts.columns = ['Department', 'Count']

    fig = px.pie(department_counts, values='Count', names='Department', title='Department Distribution Chart')

    st.subheader('Student Department Distribution')
    st.plotly_chart(fig)
    st.markdown("From this chart, we can now see a rough percentage of how many students are studying in each respective department. It is worth noting that this is not from the original dataset, and instead only relies on the watered down sample of 100 students. Moving on, what if we wanted to see the grade rating of each student in the form of a pie chart like this one?")

    # PIE CHART 2 START
    grade_counts = limited_data['Grade'].value_counts().reset_index()
    grade_counts.columns = ['Grade', 'Count']

    fig = px.pie(grade_counts, values='Count', names='Grade', title='Letter Grade Distribution Chart')

    st.subheader('Student Letter Grade Distribution')
    st.plotly_chart(fig)
    st.markdown("And now we can get an idea of how each student is performing at school. The majority of the students are getting high grades, so that can be assumed to be the case for the original dataset, however it may not be the case due to potential variance and randomness when picking the 100 students earlier. Now, let's sort everyone based on their income level.")

    fig = px.bar(age_gender_data, x='Gender', y='Age', title='Age and Gender Chart', 
             labels={'Age': 'Average Age', 'Gender': 'Gender'},
             color='Gender', 
             color_discrete_sequence=['red', 'blue'])
    
    # BAR CHART 2 START
    income_counts = limited_data['Family_Income_Level'].value_counts().reset_index()
    income_counts.columns = ['Family_Income_Level', 'Count']

    fig = px.bar(income_counts, 
              x='Family_Income_Level', 
              y='Count', 
              title='Family Income Level Distribution',
              color='Family_Income_Level',
              color_discrete_sequence=['#1f77b4', '#ff7f0e', '#2ca02c'])
    fig.update_layout(xaxis_title='Income Level Among Students')
    fig.update_layout(yaxis_title='Student Count')

    st.subheader('Family Income Levels')
    st.plotly_chart(fig)
    st.markdown("Once more, we can now see the income levels of each of the families of the students involved in the dataset. The majority of them don't earn as much as the others so they fall into the 'low' category. Next, let's look at the average sleep time per night.")

    # BAR CHART 3 START
    average_sleep = limited_data['Sleep_Hours_per_Night'].mean()
    average_data = pd.DataFrame({
    'Average Sleep Hours': [average_sleep]
    })

    average_sleep = limited_data['Sleep_Hours_per_Night'].mean()
    average_data = pd.DataFrame({
    'Category': ['Average Sleep Hours'],
    'Average': [average_sleep]
    })

    fig = px.bar(average_data, 
             x='Category', 
             y='Average', 
             title='Average Sleep Hours',
             labels={'Average': 'Average Sleep Hours'},
             text='Average')

    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig.update_layout(
    yaxis_title='Hours',
    xaxis_title=' ',
    bargap=0.7 
    )

    st.subheader('Average Sleep Hours per Night')
    st.plotly_chart(fig)
    st.markdown("From this, we can see that the students accumulate on average 6.5 hours of sleep per night. Lastly, let's see how long each student spent studying for the week.")

    # BAR CHART 4 START
    average_sleep = limited_data['Study_Hours_per_Week'].mean()
    average_data = pd.DataFrame({
    'Average Sleep Hours': [average_sleep]
    })

    average_sleep = limited_data['Study_Hours_per_Week'].mean()

    average_data = pd.DataFrame({
    'Category': ['Study Hours'],
    'Average': [average_sleep]
    })

    fig = px.bar(average_data, 
             x='Category', 
             y='Average', 
             title='Study Hours',
             labels={'Average': 'Study Hours'},
             text='Average')

    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig.update_layout(
    yaxis_title='Hours',
    xaxis_title=' ',
    bargap=0.7 
    )

    st.subheader('Study Hours per Week')
    st.plotly_chart(fig)
    st.markdown("On average, it appears that students have enough time for 17.25 hours of studying per week (7 days). The lowest that was found was 5.1, and the highest was 29.7.")
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
def conclusion():
    st.title("Summary and Conclusion")

    st.subheader("How are the students' performance overall?")
    st.markdown(
        """
        By quickly analyzing the dataset given to us via finding the means and visualizing the data, we can conclude that:
        1. Age and gender don't affect grades
        2. Family income levels don't affect grades
        3. Sleep time and study hours affect grades
        """
    )

    st.subheader("Any further insights?")
    st.markdown(
        """
        K-modes clustering was used for this analysis as we compared students that shared similar attributes to one another.
        Student performance varies wildly, and it is worth noting that the attributes which were compared to one another in this test do not fully
        correlate to the performance of a student. There are more factors at play, some of which cannot be known because once again,
         this is a modified dataset.
        """
    )


# Define the main menu
list_of_pages = [
    "Introduction",
    "Data Visualization",
    "Conclusion",
]

st.sidebar.title(':scroll: Main Menu')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Introduction":
    introduction()

elif selection == "Data Visualization":
    visualization()

elif selection == "Conclusion":
    conclusion()
