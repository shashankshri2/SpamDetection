import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.naive_bayes import MultinomialNB
import streamlit as st

data = pd.read_csv("C:\\Users\\shash\\Downloads\\Spam\\spam.csv")

data.drop_duplicates(inplace=True)
data['Category']=data['Category'].replace(['ham','spam'],['Not Spam','Spam'])
print(data.head())

msg =data['Message']
cat =data['Category']

(msg_train,msg_test,cat_train,cat_test)= train_test_split(msg,cat, test_size=0.2)

cv=CountVectorizer(stop_words='english')
features=cv.fit_transform(msg_train)

#creating model

model=MultinomialNB()
model.fit(features, cat_train)

#Test the model
features_test=cv.transform(msg_test)
#print(model.score(features_test, cat_test))




#predict the data

def predict(message):
    input_message=cv.transform([message]).toarray()
    result=model.predict(input_message)
    return result

st.header('Spam Detection')


input_msg=st.text_input("Enter Message Here")

if st.button("Validate"):
    output=predict(input_msg)
    st.markdown(output)