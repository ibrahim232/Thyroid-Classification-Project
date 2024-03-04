
# Import required libraries
import streamlit as st
import joblib
import pandas as pd
import plotly.express as px

# Correct the imports (removed duplicate and unnecessary imports)
from imblearn.over_sampling import ADASYN
from imblearn.under_sampling import TomekLinks
from sklearn.impute import KNNImputer, SimpleImputer
from sklearn.preprocessing import OneHotEncoder, RobustScaler

# Page selection sidebar
select_page = st.sidebar.radio('Select page', ['Analysis', 'Model Classification', 'About'])

if select_page == 'Analysis':
    cleaned_data = pd.read_csv('clean_data.csv')
    st.image('https://th.bing.com/th/id/OIP.nCkh1m-FQ0zwXAv0-9HY6QHaFi?rs=1&pid=ImgDetMain')
    st.write('### Head of Dataframe')
    st.dataframe(cleaned_data.head(10))

    # Create tabs for analysis
    tab1, tab2, tab3 = st.tabs(['Univariate Analysis', 'Bivariate Analysis', 'Multivariate Analysis'])

    # Univariate Analysis
    tab1.write('### Univariate Analysis with Histogram for each Feature')
    for col in cleaned_data.columns:
        tab1.plotly_chart(px.histogram(cleaned_data, x=col))

    # Bivariate Analysis
    tab2.write('### Numerical Features vs Target Variable')
    select_plot = tab2.selectbox('Select Plot Type', ['Boxplot', 'Violinplot', 'Stripplot'])
    select_feature = tab2.selectbox('Select Feature', cleaned_data.columns.drop('Class'))

    if select_plot == 'Boxplot':
        tab2.plotly_chart(px.box(cleaned_data, x='Class', y=select_feature))
    elif select_plot == 'Violinplot':
        tab2.plotly_chart(px.violin(cleaned_data, x='Class', y=select_feature))
    else:
        tab2.plotly_chart(px.strip(cleaned_data, x='Class', y=select_feature))

    # Multivariate Analysis
    tab3.write('### Heatmap for Numerical Features')
    num_cols = cleaned_data.select_dtypes(exclude='O').columns.tolist()
    num_cols_df = cleaned_data[num_cols]
    tab3.plotly_chart(px.imshow(num_cols_df.corr(), x=num_cols, y=num_cols))

elif select_page == 'Model Classification':
    st.title('Model Classification')
    st.image('Thyroid.jpg')

    # Load the model
    pipeline = joblib.load('thyroid_model.pkl')

    # Input fields
    age = st.sidebar.slider('Enter your Age', 1, 113)
    TSH = st.sidebar.slider('TSH level', 0.005, 6.0)
    T3 = st.sidebar.slider('T3 level', 0.4, 3.6)
    TT4 = st.sidebar.slider('TT4 level', 34, 178)
    T4U = st.sidebar.slider('T4U level', 0.58, 1.38)
    FTI = st.sidebar.slider('FTI level', 46.5, 170.5)
    sex = st.selectbox('Please select your sex', ['F', 'M'])
    on_thyroxine = st.selectbox('Are you on thyroxine?', ['f', 't'])
    query_on_thyroxine = st.selectbox('Do you have a query on thyroxine treatment?', ['f', 't'])
    on_antithyroid_medication = st.selectbox('Are you on antithyroid medication?', ['f', 't'])
    sick = st.selectbox('Are you currently sick?', ['f', 't'])
    pregnant = st.selectbox('Are you pregnant?', ['f', 't'])
    thyroid_surgery = st.selectbox('Have you had thyroid surgery?', ['f', 't'])
    I131_treatment = st.selectbox('Have you had radioactive iodine treatment?', ['f', 't'])
    query_hypothyroid = st.selectbox('Do you have a query about hypothyroidism?', ['f', 't'])
    query_hyperthyroid = st.selectbox('Do you have a query about hyperthyroidism?', ['f', 't'])
    lithium = st.selectbox('Are you taking lithium?', ['f', 't'])
    goitre = st.selectbox('Do you have a goitre?', ['f', 't'])
    tumor = st.selectbox('Do you have a tumor?', ['f', 't'])
    psych = st.selectbox('Do you have a psychiatric history?', ['f', 't'])
    referral_source = st.selectbox('Please provide your referral source', ['SVHD', 'STMW', 'SVHC', 'SVI', 'other'])

    if st.button('Predict'):
        # Prepare the data for prediction
        data = {
            'age': age, 'TSH': TSH, 'T3': T3, 'TT4': TT4, 'T4U': T4U, 'FTI': FTI,
            'sex': sex, 'on_thyroxine': on_thyroxine, 'query_on_thyroxine': query_on_thyroxine,
            'on_antithyroid_medication': on_antithyroid_medication, 'sick': sick, 'pregnant': pregnant,
            'thyroid_surgery': thyroid_surgery, 'I131_treatment': I131_treatment,
            'query_hypothyroid': query_hypothyroid, 'query_hyperthyroid': query_hyperthyroid,
            'lithium': lithium, 'goitre': goitre, 'tumor': tumor, 'psych': psych,
            'referral_source': referral_source
        }
        df = pd.DataFrame([data])

        # Make prediction
        result = pipeline.predict(df)[0]
        if result == 0:
            st.success("The patient is euthyroid.")
        elif result == 1:
            st.warning('The patient has compensated hypothyroid.')
        else:
            st.error('The patient has primary hypothyroid.')
            
elif select_page == 'About':
    st.title('About Thyroid Disease Classification')
    st.markdown("""
        ## Background of Thyroid Disease and Prevalence

        Thyroid disease is a common endocrine disorder affecting millions of people worldwide. It encompasses a spectrum of conditions affecting the thyroid gland's structure or function. According to the World Health Organization (WHO), thyroid disorders are estimated to affect about 200 million people globally, with prevalence increasing over the years.

        Thyroid disease can manifest in various forms, including hypothyroidism, hyperthyroidism, and euthyroidism. Euthyroidism refers to normal thyroid function, while hypothyroidism and hyperthyroidism represent underactive and overactive thyroid function, respectively.

        ### Classes of Thyroid Disease in the dataset
        
        1. **Euthyroid**: Individuals with normal thyroid function.
        2. **Compensated Hypothyroid**: Patients with subclinical or compensated hypothyroidism, where thyroid hormone levels are within the normal range, but other indicators suggest thyroid dysfunction.
        3. **Primary Hypothyroid**: Patients with overt hypothyroidism, characterized by low thyroid hormone levels and elevated thyroid-stimulating hormone (TSH) levels.

        ### Problem Statement
        The goal is to develop a classification model to predict the type of thyroid disease a person has based on relevant features such as demographic information and thyroid hormone levels.
    """)

    
# At the bottom of every page, add your name and social media links
st.image("Ibrahim.jpg", width=200)
st.markdown("Done by Ibrahim Abdelnasar Yakout.")
st.markdown("[LinkedIn](https://www.linkedin.com/in/ibrahim-abdelnasar/) | [Facebook](https://www.facebook.com/profile.php?id=100005030929252&mibextid=sCpJLy)")
