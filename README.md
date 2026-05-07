# 🔐 PassAnalyzer – Password Strength Analyzer

A simple yet powerful web-based tool that evaluates the strength of passwords and helps users understand how secure their passwords are against modern attack techniques.

Live App:  
👉 [PassAnalyzer Hugging Face Space](https://huggingface.co/spaces/harshi1305/passanalyzer?utm_source=chatgpt.com)  

---

## 📸 Dashboard Preview

<p align="center">
  <img src="assets/dashboard.png" width="750"/>
</p>

---

## 🚀 Overview

**PassAnalyzer** is a password strength evaluation tool that analyzes user-entered passwords and provides a clear security rating based on multiple factors such as:

- Length of password  
- Uppercase and lowercase characters  
- Numbers  
- Special characters  
- Common patterns and weak structures  

It gives instant feedback so users can improve password security in real time.

---

## 🧠 Why this matters

Weak passwords are one of the most common causes of data breaches. Many users still rely on predictable passwords like:

- `123456`
- `password`
- `qwerty`

This tool helps users:

- Understand password weaknesses  
- Learn security best practices  
- Build stronger authentication habits  

---

## ⚙️ Features

- 🔍 Real-time password analysis  
- 📊 Strength scoring system (Weak / Medium / Strong)  
- 💡 Suggestions to improve security  
- 🧩 Detection of weak patterns  
- ⚡ Lightweight and fast UI  

---

## 🖥️ Tech Stack

- Python  
- Streamlit  
- Password evaluation logic  
- Hugging Face Spaces deployment  

---

## 📸 How it works

1. User enters a password  
2. System evaluates complexity rules  
3. Strength score is generated  
4. Suggestions are displayed instantly  

---

## 📦 Installation (Local Setup)

```bash
git clone https://github.com/your-username/passanalyzer.git
cd passanalyzer
pip install -r requirements.txt
streamlit run app.py
