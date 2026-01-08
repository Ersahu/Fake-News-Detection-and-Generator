# 📰 Fake News Detection and Generator

**Detects, analyzes, and generates fake news.**

This project is a Streamlit web application that allows users to:
- 🔍 **Detect** whether a news article is real or fake using a machine learning model.
- 🤖 **Generate** realistic-looking fake news using a text generation model.



## 🚀 Features

- **Fake News Detection**
  - Uses a trained Logistic Regression model.
  - Converts text using a pre-trained vectorizer.
  - Predicts whether the input news is *Real* or *Fake*.

- **Fake News Generator**
  - Uses **GPT-2** via Hugging Face Transformers.
  - Produces realistic-style fake news paragraphs.
  - Clean output without non-printable characters.

---

## 🛠 Tech Stack

- **Python**
- **Streamlit** for web interface  
- **Scikit-learn** for ML model  
- **Transformers (Hugging Face)** for text generation  
- **Joblib** for model loading  


## 📂 Project Structure

```
Fake-News-Detection-and-Generator/
│
├── app.py               # Main Streamlit application
├── lr_model.jb         # Trained Logistic Regression model
├── vectorizer.jb       # Text vectorizer
├── requirements.txt    # Required Python libraries
└── README.md           # Project documentation
```



## ⚙️ Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/your-username/Fake-News-Detection-and-Generator.git
cd Fake-News-Detection-and-Generator
```

2. **Create a virtual environment (optional but recommended)**
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Your app will open in the browser at:
```
http://localhost:8501
```


## 🧪 How It Works

### 🔍 Detection Mode
1. Enter a news article in the text box.
2. Click **“Check News”**.
3. The model classifies it as:
   - ✔ **Real**
   - ❌ **Fake**

### 🤖 Generator Mode
1. Click **“Generate Fake News”**.
2. A fake news paragraph is generated using GPT-2.


## ⚠️ Disclaimer

This project is created **for educational purposes only**.  
The fake news generator is meant to demonstrate AI capabilities and should **not be used to spread misinformation**.


## 📌 Future Improvements

- Add dataset upload for custom training  
- Improve UI design  
- Use more advanced NLP models (BERT, RoBERTa)  
- Add confidence scores for predictions  



## 🤝 Contributions
We welcome pull requests! For major changes, please open an issue to discuss what you'd like to improve or add.

## 📧 Contact
**Developer**: Vaibhav

**Email**: sahuvaibhav064@gmail.com

**LinkedIn**: https://www.linkedin.com/in/vaibhav-chaudhary-615712272/

## 📜 License
MIT License © 2025 Vaibhav
