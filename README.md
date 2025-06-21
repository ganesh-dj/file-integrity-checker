# 🛡️ File Integrity Checker

A Python-based tool to detect file tampering, modifications, deletions, and additions using SHA-512 cryptographic hashing.

---

## 🔖 Developed By

- **Name:** D.J. Ganesh  
- **Intern ID:** CITSOD227  
- **Company:** CodTech IT Solutions  
- **Domain:** Cyber Security & Ethical Hacking  
- **Mentor:** Neela Santosh  
- **Internship Duration:** 6 Weeks  

---

## 📌 About the Project

This script scans a specified directory and uses cryptographic hashing (SHA-512) to detect any changes in the files. It’s helpful for validating the integrity of critical data and monitoring unauthorized changes.

It identifies:

- 🟡 New files
- 🔴 Modified files
- 🟣 Deleted files
- 🟢 Unchanged files

---

## ⚙️ Tech Stack

| Component     | Usage                          |
|---------------|--------------------------------|
| `Python 3.x`  | Programming Language            |
| `hashlib`     | Hashing (standard library)     |
| `colorama`    | Colored CLI output             |
| `os, json`    | File handling, data storage    |

---

## 🛠️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/File-Integrity-Checker.git
cd File-Integrity-Checker
Install Requirements
bash
Copy
Edit
pip install colorama
3. Prepare Files for Monitoring
Place the files you want to monitor into the /Files/ directory.

🧪 How to Use

Run the Python script:

bash
Copy
Edit
python file_integrity_checker.py
Choose from the menu options:

mathematica
Copy
Edit
1. Generate Baseline
2. Check File Integrity
3. Exit
Generate Baseline: Creates baseline.txt with current file hashes.

Check File Integrity: Compares current file states with baseline and logs differences.

Exit: Ends the program.

📁 Directory Layout

bash
Copy
Edit
File-Integrity-Checker/
├── Files/                    # Folder being monitored
│   └── Subfolder/            # Nested directories supported
├── file_integrity_checker.py
├── baseline.txt              # Stores file hashes
└── integrity_log.txt         # Logs changes after checks


🔐 Security Algorithm Used

SHA-512 (Secure Hash Algorithm)

Part of the SHA-2 family

Strong resistance to collisions

Ideal for integrity checking and forensic validation

📘 Use Cases

🔍 Detect tampering in confidential files

📦 Verify backup file consistency

🚀 Confirm post-deployment file integrity

🧪 Forensic or incident response scenarios

🌟 Roadmap & Enhancements


 Add Tkinter GUI for user-friendly interface

 Add support for SHA-256, MD5

 Send email alerts on file modifications

 Support remote file integrity validation

