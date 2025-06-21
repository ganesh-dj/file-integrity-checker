import hashlib
import os
import logging
from colorama import Fore, Style, init
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Initialize colorama
init(autoreset=True)

# Configure logging
logging.basicConfig(filename='integrity_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
EMAIL_ADDRESS = "youremail@gmail.com"         # <--- YOUR EMAIL
EMAIL_PASSWORD = "yourapppassword"            # <--- YOUR APP PASSWORD
EMAIL_TO = "receiveremail@example.com"        # <--- RECEIVER EMAIL

def send_email_alert(subject, message):
    """Send an email alert with a subject and message."""
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_TO
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        print(Fore.CYAN + " Email alert sent.")
        logging.info("Email alert sent.")
    except Exception as e:
        print(Fore.RED + f" Failed to send email: {e}")
        logging.error(f"Failed to send email: {e}")

def calculate_file_hash(filepath):
    """Calculate the SHA-512 hash of a file."""
    hash_sha512 = hashlib.sha512()
    try:
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha512.update(chunk)
        return hash_sha512.hexdigest()
    except Exception as e:
        logging.error(f"Error reading file {filepath}: {e}")
        return None

def scan_files_recursively(directory):
    """Recursively scan files in the directory."""
    file_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            if os.path.basename(full_path) == 'baseline.txt':
                continue
            file_list.append(full_path)
    return file_list

def generate_baseline(directory):
    """Generate baseline hashes for files in the specified directory."""
    baseline_file = 'baseline.txt'
    with open(baseline_file, 'w') as bf:
        for filepath in scan_files_recursively(directory):
            if os.path.isfile(filepath):
                file_hash = calculate_file_hash(filepath)
                if file_hash:
                    relative_path = os.path.relpath(filepath, directory)
                    bf.write(f"{relative_path}|{file_hash}\n")
    print(Fore.GREEN + f" Baseline created in {baseline_file}")
    logging.info("Baseline created successfully.")

def check_integrity(directory):
    """Compare current file hashes with the baseline to detect changes."""
    baseline_file = 'baseline.txt'
    if not os.path.exists(baseline_file):
        print(Fore.RED + " Baseline not found. Please generate it first.")
        logging.error("Baseline file not found.")
        return

    # Load baseline
    baseline_hashes = {}
    with open(baseline_file, 'r') as bf:
        for line in bf:
            filename, filehash = line.strip().split('|')
            baseline_hashes[filename] = filehash

    found_files = set()

    for filepath in scan_files_recursively(directory):
        if os.path.isfile(filepath):
            relative_path = os.path.relpath(filepath, directory)
            current_hash = calculate_file_hash(filepath)
            if not current_hash:
                continue
            baseline_hash = baseline_hashes.get(relative_path)
            found_files.add(relative_path)

            if not baseline_hash:
                print(Fore.YELLOW + f"[NEW FILE] {relative_path}")
                logging.warning(f"New file detected: {relative_path}")
                send_email_alert("File Integrity Alert: New File Detected",
                                 f"A new file was added:\n{relative_path}")
            elif current_hash != baseline_hash:
                print(Fore.RED + f"[MODIFIED] {relative_path}")
                logging.warning(f"File modified: {relative_path}")
                send_email_alert("File Integrity Alert: File Modified",
                                 f"The file was modified:\n{relative_path}")
            else:
                print(Fore.GREEN + f"[OK] {relative_path}")
                logging.info(f"File unchanged: {relative_path}")

    # Check for deleted files
    for filename in baseline_hashes:
        if filename not in found_files:
            print(Fore.MAGENTA + f"[DELETED] {filename}")
            logging.warning(f"File missing: {filename}")
            send_email_alert("File Integrity Alert: File Deleted",
                             f"The file is missing or deleted:\n{filename}")

def main():
    directory = './Files'  # Directory to monitor
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created. Add files and rerun the script.")

    while True:
        print("\n Choose an option:")
        print("1. Generate baseline")
        print("2. Check file integrity")
        print("3. Exit")
        choice = input("Enter 1, 2 or 3: ")

        if choice == '1':
            generate_baseline(directory)
        elif choice == '2':
            check_integrity(directory)
        elif choice == '3':
            print(" Exiting program. Goodbye!")
            break
        else:
            print(" Invalid choice. Try again.")

if __name__ == '__main__':
    main()
