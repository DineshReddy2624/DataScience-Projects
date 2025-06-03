import streamlit as st
from streamlit_autorefresh import st_autorefresh
import time
from datetime import datetime


# === STYLE ===
st.markdown("""
        <style>
            body, .main { background-color: #f4f4f8; color: #333; }
            .title { color: #007bff; text-align: center; margin-bottom: 2rem; }
            .assignment-title { color: #28a745; margin-top: 1.5rem; }
            .question { font-weight: 600; margin-top: 1rem; padding: 0.5rem; border-left: 5px solid #007bff; background-color: #333; border-radius: 5px; }
            .options label { display: block; margin-bottom: 0.5rem; }
            .correct { color: green; font-weight: bold; }
            .incorrect { color: red; font-weight: bold; }
            .timer-container {
                text-align: center;
                margin-bottom: 1rem;
            }
            .timer-title {
                font-size: 1rem;
                color: #6c757d;
                margin-bottom: 0.25rem;
            }
            .timer {
                font-size: 1.5rem;
                font-weight: bold;
                padding: 0.75rem;
                border-radius: 8px;
            }
            .timer.safe { background-color: #e6ffe6; color: #28a745; }
            .timer.warning { background-color: #fff3cd; color: #85640a; }
            .timer.danger { background-color: #f8d7da; color: #721c24; }
            .sidebar .sidebar-content { background-color: #f8f9fa; color: #333; }
            .sidebar-header { font-size: 1.2rem; font-weight: bold; padding: 1rem 0; border-bottom: 1px solid #ccc; margin-bottom: 1rem; }
            .sidebar-button { width: 100%; padding: 0.5rem 1rem; margin-bottom: 0.5rem; border: 1px solid #ccc; border-radius: 5px; background-color: #fff; color: #333; cursor: pointer; }
            .sidebar-button:hover { background-color: #e9ecef; }
            .results-title { color: #ffc107; text-align: center; margin-bottom: 1.5rem; }
            .results-score { font-size: 1.2rem; font-weight: bold; margin-bottom: 0.5rem; }
            .results-time { font-size: 1rem; color: #6c757d; margin-bottom: 1rem; }
            .results-assignment-score { margin-left: 1rem; }
            .restart-button { background-color: #007bff; color: white; padding: 0.75rem 1.5rem; border: none; border-radius: 5px; cursor: pointer; font-size: 1rem; }
            .restart-button:hover { background-color: #0056b3; }
            .tab-warning { background-color: #ffe0b2; color: #d68910; padding: 0.75rem; border-radius: 5px; margin-bottom: 1rem; }
            .tab-error { background-color: #ffdddd; color: #e53935; padding: 0.75rem; border-radius: 5px; margin-bottom: 1rem; }
            .rules-container {
                background-color: #f9f9f9;
                padding: 1rem;
                border: 1px solid #ddd;
                border-radius: 5px;
                margin-bottom: 1rem;
            }
            .rules-title {
                font-size: 1.1rem;
                font-weight: bold;
                margin-bottom: 0.5rem;
                color: #333;
            }
            .rules-list {
                list-style-type: disc;
                padding-left: 1.5rem;
                color: #555;
            }
        </style>
    """, unsafe_allow_html=True)

# === QUIZ DATA ===
assignments = {
    "Fundamentals of Data Analysis": [
        {"question": "Which of the following is NOT a core task in Data Analysis?",
         "options": ["Data Collection", "Model Deployment", "Data Cleaning", "Data Interpretation"],
         "answer": "Model Deployment"},
        {"question": "What does SQL primarily stand for in the context of data?",
         "options": ["Structured Query Language", "Simple Question Logic", "Systematic Query Language", "Standard Query Logic"],
         "answer": "Structured Query Language"},
        {"question": "Exploratory Data Analysis (EDA) is mainly used to:",
         "options": ["Build predictive models", "Visualize final results", "Understand the main characteristics of a dataset", "Automate data pipelines"],
         "answer": "Understand the main characteristics of a dataset"},
        {"question": "Which Python library is essential for working with structured data and DataFrames?",
         "options": ["NumPy", "Matplotlib", "Pandas", "Seaborn"],
         "answer": "Pandas"},
        {"question": "A histogram is most suitable for visualizing:",
         "options": ["Relationships between two continuous variables", "Distribution of a single categorical variable", "Distribution of a single continuous variable", "Trends over time"],
         "answer": "Distribution of a single continuous variable"}
    ],
    "SQL for Data Analysis": [
        {"question": "Which SQL clause is used to retrieve specific columns from a table?",
         "options": ["WHERE", "SELECT", "FROM", "GROUP BY"],
         "answer": "SELECT"},
        {"question": "To filter records based on a condition, which SQL keyword is used?",
         "options": ["HAVING", "ORDER BY", "WHERE", "AND"],
         "answer": "WHERE"},
        {"question": "Which SQL command is used to combine rows from two or more tables based on a related column?",
         "options": ["UNION", "INTERSECT", "JOIN", "MERGE"],
         "answer": "JOIN"},
        {"question": "The `GROUP BY` clause in SQL is used to:",
         "options": ["Sort the result set", "Filter the result set", "Aggregate functions on groups of rows", "Select distinct values"],
         "answer": "Aggregate functions on groups of rows"},
        {"question": "Which SQL keyword is used to arrange the result set in ascending or descending order?",
         "options": ["SORT BY", "ARRANGE BY", "ORDER BY", "LIMIT"],
         "answer": "ORDER BY"}
    ],
    "Python for Data Analysis": [
        {"question": "Which NumPy function is used to create arrays?",
         "options": ["create_array()", "make_array()", "np.array()", "array_from()"],
         "answer": "np.array()"},
        {"question": "How can you select a column named 'age' from a Pandas DataFrame named 'df'?",
         "options": ["df.age()", "df['age']", "df.get('age')", "df[['age']]"],
         "answer": "df['age']"},
        {"question": "Which Matplotlib function is commonly used to create a line plot?",
         "options": ["plt.bar()", "plt.scatter()", "plt.line()", "plt.plot()"],
         "answer": "plt.plot()"},
        {"question": "What is the purpose of the `groupby()` method in Pandas?",
         "options": ["To merge two DataFrames", "To filter rows based on a condition", "To group rows with the same values in a column", "To sort the DataFrame"],
         "answer": "To group rows with the same values in a column"},
        {"question": "Which Pandas function is used to handle missing values?",
         "options": ["remove_nulls()", "delete_na()", "fillna()", "handle_missing()"],
         "answer": "fillna()"}
    ],
    "Data Visualization": [
        {"question": "A pie chart is best used for showing:",
         "options": ["Trends over time", "Distribution of a continuous variable", "Proportions of different categories within a whole", "Correlation between two variables"],
         "answer": "Proportions of different categories within a whole"},
        {"question": "A scatter plot is primarily used to visualize:",
         "options": ["Frequency distribution", "Relationship between two numerical variables", "Hierarchical data", "Part-to-whole relationships"],
         "answer": "Relationship between two numerical variables"},
        {"question": "Which type of chart is suitable for comparing values across different categories?",
         "options": ["Line chart", "Scatter plot", "Bar chart", "Pie chart"],
         "answer": "Bar chart"},
        {"question": "A box plot (or box and whisker plot) is useful for displaying:",
         "options": ["Central tendency only", "Correlation and regression", "Distribution and outliers", "Time series data"],
         "answer": "Distribution and outliers"},
        {"question": "A heatmap is often used to visualize:",
         "options": ["Univariate distributions", "Changes over time", "Correlation matrices or intensity of phenomena", "Geographical data"],
         "answer": "Correlation matrices or intensity of phenomena"}
    ],
    "Statistics for Data Analysis": [
        {"question": "What is the median of the following dataset: [2, 5, 1, 8, 3]?",
         "options": ["1", "2", "3", "5"],
         "answer": "3"},
        {"question": "The standard deviation is a measure of:",
         "options": ["Central tendency", "Spread or dispersion of data", "Skewness of data", "Kurtosis of data"],
         "answer": "Spread or dispersion of data"},
        {"question": "A p-value in hypothesis testing represents:",
         "options": ["The probability of the null hypothesis being true", "The probability of the alternative hypothesis being true", "The probability of observing the data (or more extreme data) if the null hypothesis is true", "The significance level of the test"],
         "answer": "The probability of observing the data (or more extreme data) if the null hypothesis is true"},
        {"question": "What is the difference between a population and a sample?",
         "options": ["A population is a subset of a sample", "A sample is the entire group of interest, while a population is a subset", "A population is the entire group of interest, while a sample is a subset", "There is no difference between them"],
         "answer": "A population is the entire group of interest, while a sample is a subset"},
        {"question": "What type of distribution is often assumed for many statistical tests?",
         "options": ["Uniform distribution", "Exponential distribution", "Normal distribution", "Poisson distribution"],
         "answer": "Normal distribution"}
    ],
    "Data Cleaning and Preprocessing": [
        {"question": "Which of the following is a common technique for handling missing numerical data?",
         "options": ["Deleting the entire row", "Replacing with 0", "Replacing with the mean or median", "Ignoring the missing values"],
         "answer": "Replacing with the mean or median"},
        {"question": "What is the purpose of data normalization or scaling?",
         "options": ["To make the data more skewed", "To reduce the number of features", "To bring numerical features to a similar scale", "To handle categorical variables"],
         "answer": "To bring numerical features to a similar scale"},
        {"question": "Identifying and removing duplicate records is an important step in:",
         "options": ["Feature engineering", "Data integration", "Data cleaning", "Data visualization"],
         "answer": "Data cleaning"},
        {"question": "What is one-hot encoding used for?",
         "options": ["Scaling numerical data", "Handling missing values in categorical data", "Converting categorical variables into a numerical format", "Reducing the dimensionality of the data"],
         "answer": "Converting categorical variables into a numerical format"},
        {"question": "Outliers in a dataset can significantly affect:",
         "options": ["The number of data points", "The names of the columns", "Statistical measures like mean and standard deviation", "The data types of the variables"],
         "answer": "Statistical measures like mean and standard deviation"}
    ],
    "Machine Learning Fundamentals": [
        {"question": "Supervised learning algorithms learn from:",
         "options": ["Unlabeled data", "Labeled data", "Reinforcement signals", "Clustered data"],
         "answer": "Labeled data"},
        {"question": "Which of the following is a common supervised learning task?",
         "options": ["Clustering", "Dimensionality reduction", "Regression", "Association rule mining"],
         "answer": "Regression"},
        {"question": "What is the purpose of splitting a dataset into training and testing sets?",
         "options": ["To increase the amount of data", "To train the model on all the data", "To evaluate the model's performance on unseen data", "To make the training process faster"],
         "answer": "To evaluate the model's performance on unseen data"},
        {"question": "Which of the following is an example of an unsupervised learning algorithm?",
         "options": ["Linear Regression", "Decision Trees", "K-Means Clustering", "Support Vector Machines"],
         "answer": "K-Means Clustering"},
        {"question": "What does the term 'overfitting' refer to in machine learning?",
         "options": ["A model that performs poorly on the training data", "A model that generalizes well to unseen data", "A model that learns the training data too well, leading to poor performance on unseen data", "A model that takes too long to train"],
         "answer": "A model that learns the training data too well, leading to poor performance on unseen data"}
    ],
    "Big Data and Cloud Concepts": [
        {"question": "What is a key characteristic of Big Data often referred to as 'Volume'?",
         "options": ["The speed at which data is generated and processed", "The variety of data types and sources", "The sheer amount of data", "The accuracy and reliability of the data"],
         "answer": "The sheer amount of data"},
        {"question": "Hadoop is a framework primarily used for:",
         "options": ["Real-time data processing", "Distributed storage and processing of large datasets", "Relational database management", "Data visualization"],
         "answer": "Distributed storage and processing of large datasets"},
        {"question": "Which of the following is a common cloud computing service model?",
         "options": ["Desktop as a Service (DaaS)", "Software as a Product (SaaP)", "Infrastructure as a Code (IaaC)", "Platform as a Service (PaaS)"],
         "answer": "Platform as a Service (PaaS)"},
        {"question": "What is the purpose of data partitioning in distributed systems?",
         "options": ["To reduce data redundancy", "To improve query performance by dividing data across nodes", "To increase data security", "To compress the data"],
         "answer": "To improve query performance by dividing data across nodes"},
        {"question": "Spark is known for its capabilities in:",
         "options": ["Long-term data archiving", "Batch processing only", "Real-time and batch data processing", "Small data analysis"],
         "answer": "Real-time and batch data processing"}
    ],
    "Data Storytelling and Communication": [
        {"question": "A key element of effective data storytelling is:",
         "options": ["Presenting as much data as possible", "Using highly technical jargon", "Having a clear narrative and message", "Focusing solely on the numbers"],
         "answer": "Having a clear narrative and message"},
        {"question": "When presenting data to a non-technical audience, it's important to:",
         "options": ["Use complex charts and graphs", "Explain every statistical detail", "Focus on the key insights and their implications", "Avoid any visuals to keep it simple"],
         "answer": "Focus on the key insights and their implications"},
        {"question": "Which type of visualization is often used to show trends over time?",
         "options": ["Pie chart", "Bar chart", "Line chart", "Scatter plot"],
         "answer": "Line chart"},
        {"question": "The 'so what?' question in data storytelling helps to identify:",
         "options": ["The data sources used", "The statistical methods applied", "The significance and implications of the findings", "The size of the dataset"],
         "answer": "The significance and implications of the findings"},
        {"question": "Using anecdotes or real-world examples can enhance data storytelling by:",
         "options": ["Making the data less accurate", "Confusing the audience with irrelevant information", "Making the data more relatable and memorable", "Slowing down the presentation"],
         "answer": "Making the data more relatable and memorable"}
    ],
    "Data Ethics and Privacy": [
        {"question": "What is data anonymization primarily aimed at?",
         "options": ["Improving data quality", "Making data analysis faster", "Protecting the identity of individuals in the data", "Increasing the size of the dataset"],
         "answer": "Protecting the identity of individuals in the data"},
        {"question": "Bias in data can lead to:",
         "options": ["More accurate models", "Fairer outcomes", "Discriminatory or unfair outcomes", "Faster data processing"],
         "answer": "Discriminatory or unfair outcomes"},
        {"question": "The GDPR (General Data Protection Regulation) is a law primarily focused on:",
         "options": ["Promoting free flow of data across all countries", "Setting standards for data security in hardware", "Protecting the privacy and personal data of individuals in the EU", "Encouraging open access to all datasets"],
         "answer": "Protecting the privacy and personal data of individuals in the EU"},
        {"question": "What is 'informed consent' in the context of data collection?",
         "options": ["Collecting data without the user's knowledge", "Providing users with clear information about how their data will be used and obtaining their agreement", "Sharing user data with any third party without restriction", "Using data only for the purpose it was initially collected, regardless of user preferences"],
         "answer": "Providing users with clear information about how their data will be used and obtaining their agreement"},
        {"question": "Ethical considerations in data analysis include:",
         "options": ["Only focusing on achieving the desired outcome", "Ignoring potential negative impacts of the analysis", "Transparency, fairness, and accountability", "Using any available data regardless of its source or legality"],
         "answer": "Transparency, fairness, and accountability"}
    ]
}

# === SESSION STATE ===
if 'started' not in st.session_state:
    st.session_state.started = False
if 'accepted_terms' not in st.session_state:
    st.session_state.accepted_terms = False
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'scores' not in st.session_state:
    st.session_state.scores = {assignment: 0 for assignment in assignments}
if 'responses' not in st.session_state:
    st.session_state.responses = {}
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'leave_attempt' not in st.session_state:
    st.session_state.leave_attempt = 0
if 'quiz_ended_early' not in st.session_state:
    st.session_state.quiz_ended_early = False
if 'show_results' not in st.session_state:
    st.session_state.show_results = False
if 'question_states' not in st.session_state:
    st.session_state.question_states = {f"{assignment}_q{i}": None
                                        for assignment, questions in assignments.items()
                                        for i in range(len(questions))}
if 'time_up' not in st.session_state:
    st.session_state.time_up = False
assignment_names = list(assignments.keys())
total_quiz_time = 180 * 60  # Total time: 180 minutes
warning_time = 5 * 60    # Warning time: 5 minutes
half_time = total_quiz_time // 2  # Half of the total time
max_leave_attempts = 3

def format_time(seconds):
    mins, secs = divmod(seconds, 60)
    return f"{int(mins):02d}:{int(secs):02d}"

def display_timer(time_left):
    if time_left > warning_time:
        color_class = "safe"
    elif time_left > 0:
        color_class = "warning"
    else:
        color_class = "danger"
    st.markdown(f"<div class='timer {color_class}'>⏳ Time Left: {format_time(time_left)}</div>", unsafe_allow_html=True)

# === START PAGE ===
if not st.session_state.started and not st.session_state.show_results:
    st.markdown("<h1 class='title'>📊 Data Analyst Quiz Challenge</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class='rules-container'>
        <p class='rules-title'>Quiz Rules:</p>
        <ul class='rules-list'>
            <li>The quiz consists of multiple assignments covering various data analysis topics.</li>
            <li>You have <strong>180 minutes</strong> to complete the entire quiz.</li>
            <li>You can navigate between assignments using the sidebar.</li>
            <li>The 'Next Assignment' button will save your current answers and move to the next section.</li>
            <li>The 'Previous Assignment' button will take you back to the previous section.</li>
            <li>The 'Finish Quiz' button will be enabled after <strong>90 minutes</strong> or when you reach the last assignment.</li>
            <li>Repeatedly switching tabs (more than 3 times) will automatically end the quiz and record your progress.</li>
            <li>The quiz will automatically submit when the time runs out.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    terms_accepted = st.checkbox("I have read and understood the quiz rules and conditions.")
    st.session_state.accepted_terms = terms_accepted

    if terms_accepted:
        if st.button("🚀 Start the Challenge"):
            st.session_state.started = True
            st.session_state.start_time = time.time()
            st.rerun()
    else:
        st.warning("Please accept the terms and conditions to start the quiz.")
    st.stop()

# === TIMER LOGIC ===
st.markdown("<h1 class='title'>📊 Data Analyst Quiz Challenge</h1>", unsafe_allow_html=True)
if st.session_state.started and not st.session_state.show_results:
    elapsed_time = int(time.time() - st.session_state.start_time)
    time_left = max(0, total_quiz_time - elapsed_time)

    # Live timer auto-refresh
    if time_left > 0 and not st.session_state.quiz_ended_early:
        st_autorefresh(interval=1000, key="timer_refresh")

    # Tab leave detection (requires client-side JS support)
    st.components.v1.html("""
    <script>
        window.onblur = function() {
            document.dispatchEvent(new CustomEvent("blurDetected"));
        };
        window.addEventListener("blurDetected", function() {
            let params = new URLSearchParams(window.location.search);
            params.set('leave', '1');
            window.location.search = params.toString();
        });
    </script>
    """, height=0)

    # Fake leave counter
    leave_param = st.query_params.get("leave")
    if time_left > 0 and st.session_state.leave_attempt < max_leave_attempts and leave_param == "1":
        st.session_state.leave_attempt += 1
        st.warning(f"<div class='tab-warning'>⚠️ You switched tabs! {max_leave_attempts - st.session_state.leave_attempt} attempts remaining.</div>", unsafe_allow_html=True)
        st.query_params.clear()
        if st.session_state.leave_attempt >= max_leave_attempts:
            st.session_state.quiz_ended_early = True
            st.session_state.show_results = True
            st.error("<div class='tab-error'>🚫 Quiz ended early due to repeated tab switching.</div>", unsafe_allow_html=True)
            st.rerun()

    # Auto-submit when time runs out
    if time_left <= 0 and not st.session_state.quiz_ended_early:
        st.session_state.show_results = True
        st.session_state.time_up = True
        st.warning("<div class='tab-warning'>⏰ Time is up! Submitting your quiz automatically...</div>", unsafe_allow_html=True)
        st.rerun()

    # === TIMER UI ===
    st.markdown("<div class='timer-container'><p class='timer-title'>Quiz Time Remaining:</p>", unsafe_allow_html=True)
    display_timer(time_left)
    st.markdown("</div>", unsafe_allow_html=True)

    # === NAVIGATION SIDEBAR ===
    st.sidebar.markdown("<div class='sidebar-header'>📚 Assignments</div>", unsafe_allow_html=True)
    for idx, name in enumerate(assignment_names):
        if st.sidebar.button(f"{idx + 1}. {name}", key=f"nav_{idx}"):
            st.session_state.current_index = idx
            st.rerun()

    # === QUIZ PAGE ===
    if st.session_state.current_index < len(assignments) and not st.session_state.show_results:
        current_assignment = assignment_names[st.session_state.current_index]
        st.markdown(f"<h2 class='assignment-title'>📝 {current_assignment}</h2>", unsafe_allow_html=True)

        with st.form(key=f"quiz_form_{st.session_state.current_index}"):
            for i, q in enumerate(assignments[current_assignment]):
                qkey = f"{current_assignment}_q{i}"
                st.markdown(f"<div class='question'>Q{i+1}: {q['question']}</div>", unsafe_allow_html=True)
                selected_option = st.radio("", q["options"], index=0, key=qkey)
                st.session_state.responses[qkey] = selected_option

            is_last_assignment = st.session_state.current_index == len(assignments) - 1
            col1, col2, col3 = st.columns([1, 1, 1])  # Adjusted columns for early submit
            if not is_last_assignment:
                if col2.form_submit_button("➡️ Next Assignment"):
                    st.session_state.current_index += 1
                    st.rerun()
            else:
                 if time_left <= half_time or st.session_state.time_up: # Enable submit after half time
                    if col2.form_submit_button("✅ Finish Quiz"):
                        st.session_state.show_results = True
                        st.rerun()
                 else:
                    st.markdown(f"<div class='tab-warning'>Submit available after {format_time(half_time)}</div>", unsafe_allow_html=True) # Display time until submit is available

            if st.session_state.current_index > 0:
                if col1.form_submit_button("⬅️ Previous Assignment"):
                    st.session_state.current_index -= 1
                    st.rerun()

# === RESULTS PAGE ===
if st.session_state.show_results:
    total_time = int(time.time() - st.session_state.start_time) if st.session_state.start_time else 0
    total_questions = sum(len(v) for v in assignments.values())
    total_correct = 0

    st.markdown("<h1 class='results-title'>🏆 Quiz Results</h1>", unsafe_allow_html=True)
    if st.session_state.quiz_ended_early:
        st.warning("<div class='tab-warning'>⚠️ The quiz ended early. Your score reflects the completed questions.</div>", unsafe_allow_html=True)

    for assignment, questions in assignments.items():
        correct_in_assignment = 0
        for i, q in enumerate(questions):
            qkey = f"{assignment}_q{i}"
            if qkey in st.session_state.responses and st.session_state.responses[qkey] == q["answer"]:
                correct_in_assignment += 1
        st.session_state.scores[assignment] = correct_in_assignment
        total_correct += correct_in_assignment

    st.markdown(f"<p class='results-score'>🎯 You scored <strong>{total_correct}</strong> out of <strong>{total_questions}</strong> correct answers.</p>", unsafe_allow_html=True)
    st.markdown(f"<p class='results-time'>⏱️ Time Taken: {format_time(total_time)}</p>", unsafe_allow_html=True)

    st.markdown("<h3>Detailed Scores by Assignment:</h3>", unsafe_allow_html=True)
    for assignment in assignment_names:
        score = st.session_state.scores.get(assignment, 0)
        total_in_assignment = len(assignments[assignment])
        st.markdown(f"<p class='results-assignment-score'>- <strong>{assignment}</strong>: {score} / {total_in_assignment}</p>", unsafe_allow_html=True)

    if st.button("🔄 Restart the Challenge", key="restart_button", on_click=lambda: st.session_state.clear()):
        pass
