# PhishGuard 🚨🛡️

**PhishGuard** is a Python Flask web application that helps users detect phishing websites in real-time. It features a sleek UI, interactive results, history tracking, stats, and a clear history option.

---

## **Live Demo**

Try it online: [https://phishguard.onrender.com](https://phishguard.onrender.com)

---

## **Features**

- Check if a website is **Safe** or **Phishing** based on keywords.
- **History tracking** with URL, result, and timestamp.
- **Stats panel** showing Safe vs Phishing counts.
- **Clear history** button to reset data.
- **Copy URL** button for quick copying.
- Attractive UI with animations and color-coded results.

---

## **Installation (Local)**

1. Clone this repository:
```bash
git clone https://github.com/manvithakotte80/PhishGuard.git
2.Go into the project folder:
cd PhishGuard
3.(Optional) Create a virtual environment:
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
4.Install dependencies:
pip install -r requirements.txt
5.Run the app:
python app.py
6.Open your browser and go to:
http://127.0.0.1:5000
Folder Structure:
PhishGuard/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── templates/              # HTML files
│   └── index.html
├── static/                 # CSS and static files
│   └── style.css
└── README.md               # Project description
How It Works:
1.Enter a website URL in the input field.
2.Click Check → the app detects if the URL is Safe or Phishing.
3.Each check is saved in the History table with timestamp.
4.Use Copy button to copy URLs, Clear History to reset.
Technologies Used:
1.Python 3
2.Flask – Web framework
3.HTML / CSS – Frontend
4.Optional: Render for live hosting
License:
This project is open source under the MIT License.
Author
Manvitha Kotte
