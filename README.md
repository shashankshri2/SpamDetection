# SpamDetection


Spam Detection App 🚀
A simple spam detection web application built using Python, Streamlit, and Scikit-learn. This app classifies messages as Spam or Not Spam using a Naïve Bayes Machine Learning Model trained on a dataset of SMS messages.

🔥 Features
✅ Detects spam messages using Multinomial Naïve Bayes
✅ Preprocesses text data using CountVectorizer
✅ Removes duplicate messages for better accuracy
✅ Simple Streamlit UI for real-time message classification

📂 Project Structure
bash
Copy
Edit
├── spam.csv                  # Dataset file
├── app.py                     # Main Streamlit application
├── README.md                  # Project documentation
├── requirements.txt            # Required Python libraries
🛠️ Installation & Usage
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/shashankshri2/spam-detection-app.git
cd spam-detection-app
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the Streamlit App
bash
Copy
Edit
streamlit run app.py
📊 Model & Dataset
Dataset: Uses an SMS spam dataset (spam.csv)

Model: Multinomial Naïve Bayes trained on text features

Feature Extraction: CountVectorizer (removes stopwords and tokenizes text)

🖥️ Deployment
To deploy on GitHub Pages or Streamlit Cloud, follow:

Push Code to GitHub:

bash
Copy
Edit
git add .
git commit -m "Deploy Streamlit App"
git push origin main
Deploy on Streamlit Cloud:

Go to Streamlit Cloud

Select your GitHub repo

Configure app.py as the entry point
