# 🛡️ File Integrity Checker with Email Alerts

A robust, color-coded Python script for detecting new, modified, or deleted files in a specified directory. When changes occur, the script logs events, prints colored outputs to the console, and sends real-time email alerts — ideal for personal or small-scale monitoring.

---

## 👨‍💻 Developed By

- **Name**: D.J. Ganesh  
- **Intern ID**: CITSOD227  
- **Company**: CodTech IT Solutions  
- **Domain**: Cyber Security & Ethical Hacking  
- **Mentor**: Neela Santosh  
- **Internship Duration**: 6 Weeks

---

## 📌 About the Project

This script scans a specified directory and uses cryptographic hashing (**SHA-512**) to detect any changes in the files. It’s helpful for validating the integrity of critical data and monitoring unauthorized changes in sensitive systems.

---

## 🔍 Features


- ✅ Detects **New**, **Modified**, and **Deleted** files recursively
- ✅ Uses **SHA-512 hashing** for tamper detection
- ✅ Color-coded terminal output (`colorama`)
- ✅ Logs all events to `integrity_log.txt` via `logging`
- ✅ **Real-time email alerts** for file changes (via SMTP)
- ✅ Skips its own `baseline.txt` during scans

---


## ⚙️ Requirements


- Python 3.x  
- Install dependencies with:
  ```bash
  pip install colorama
  
🛠️ Setup


Clone the repo

bash
Copy
Edit
git clone https://github.com/yourusername/file-integrity-checker.git
cd file-integrity-checker
Configure email credentials
Edit the top of integrity_checker.py:

python
Copy
Edit
EMAIL_ADDRESS = "youremail@gmail.com"
EMAIL_PASSWORD = "your_generated_app_password"
EMAIL_TO = "receiver@example.com"

📌 Gmail Users: Create an App Password here:
https://myaccount.google.com/apppasswords

(Optional) Customize the monitored directory
Default is ./Files, but you can change it in the code.


🚀 Usage


Run the script:

bash
Copy
Edit
python integrity_checker.py
Menu options:

markdown
Copy
Edit
1. Generate baseline
2. Check file integrity
3. Exit
1: Creates baseline.txt storing file hashes

2: Checks directory for changes, logs results, sends email alerts

3: Exits the script


📁 Output Files


integrity_checker.py: Main script

baseline.txt: Stores initial file hashes

integrity_log.txt: Change logs

./Files/: Default monitored folder


📩 Email Alerts


Triggers: File added, modified, or deleted

Email Subject: File Integrity Alert: <Event>

Email Body: Affected file path


🔐 Security Tips


Do not commit your email credentials to GitHub

Use .env files or OS environment variables for safety

Use TLS with port 587 when using SMTP


🧠 Future Enhancements (Ideas)


Send daily summary instead of per-event emails

Export to HTML or CSV reports

Add GUI with Tkinter or web dashboard (Flask)

Let user choose hashing algorithm

Run automatically using scheduler (cron or schedule)



