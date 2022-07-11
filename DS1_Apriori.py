import pandas as pd
import streamlit as st
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import DS1_Assignment
# generate two pages
my_page = st.sidebar.radio('Projektnavigation', ['Input & Preprocessing', 'Generating Rules with Apriori'])
# page 1
if my_page == 'Input & Preprocessing':
    st.title("Association Rule Mining with Apriori")
    st.header("Input dataset and data preprocessing")
    st.markdown("Input Dataset of diabetes patients:")
    st.write(DS1_Assignment.data_input.head())
    st.write("Size of the input dataset ([rows/columns]):", DS1_Assignment.data_input.shape)
    st.markdown("Changed datasets with boolean types:")
    st.markdown("gender: checked box = male; unchecked box = female; rest of the columns: checked box means positive, "
                "unechecked box means negative")
    st.write(DS1_Assignment.data_processed.head())
    st.markdown("cut off age column; this set will get used to generate association rule mining rules:")
    st.write(DS1_Assignment.data_rules.head())
# page 2
else:
    st.title("Association Rule Mining with Apriori")
    st.header("Generating Rules with Apriori")

    support_slider = st.slider("Choose the minimum support value", min_value=0.1, max_value=1.0, value=0.25)
    confidence_slider = st.slider("Choose the minimum confidence value", min_value=0.1, max_value=1.0, value=0.75)

    freq_items = apriori(DS1_Assignment.data_rules, min_support=support_slider, use_colnames=True)
    res = association_rules(freq_items, metric="confidence", min_threshold=confidence_slider)
    #fix frozensets of antecedents and consequents columns
    res_antec = []
    for items in res["antecedents"].to_list():
        res_antec.append(set(items))
    res["antecedents"] = res_antec

    res_cons = []
    for items in res["consequents"].to_list():
        res_cons.append(set(items))
    res["consequents"] = res_cons

    res1 = res[["antecedents", "consequents", "support", "confidence", "lift", "conviction"]]
    # counter how many rules are generated with the given parameters
    counter = 0
    for i in range(0, len(res1['antecedents'])):
        counter = counter + 1
    st.write("Found rules [support: ", support_slider, " confidence: ", confidence_slider, "] : ", counter)
    st.table(res1)