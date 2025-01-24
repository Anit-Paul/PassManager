# PassManager

## Overview
This Password Manager application helps you securely manage your passwords. It allows you to:
- Store website credentials (username and password).
- Generate secure passwords.
- Search for saved credentials by website name.

The application is built using Python and Tkinter for the graphical user interface (GUI).

---

## Features

### 1. Search for Credentials
- Quickly retrieve stored credentials by entering the website name.
- Displays the username and password for the queried website.

### 2. Generate Secure Passwords
- Automatically generate a strong, random password.
- Easily insert the generated password into the password entry field.

### 3. Store Credentials
- Save website name, username/email/phone number, and password.
- Data is securely stored in a JSON file.

---

## Requirements

### Python Modules
- tkinter
- json

### Additional Files
- `data.json`: Stores the saved credentials.
- `lock.png`: Logo image displayed in the GUI.
- `password.py`: Contains the `Password` class for generating passwords.

---

## Directory Structure
```
PassManager/
├── data.json                  # JSON file to store credentials
├── lock.png                   # Logo image for the application
├── main.py                    # Main application script
├── password.py                # Password generation logic
└── README.md                  # Documentation file
```

---

## How to Run
1. Ensure all required files are in the same directory:
   - `main.py`
   - `lock.png`
   - `password.py`
   - `data.json` (optional; will be created if not present).

2. Install Python if not already installed.

3. Run the application using the command:
   ```
   python main.py
   ```

---

## Usage Instructions

1. **Add Credentials:**
   - Fill in the "Website", "Email/Username/Number", and "Password" fields.
   - Use the "Generate Password" button for a secure password.
   - Click "Add" to save the credentials.

2. **Search for Credentials:**
   - Enter the website name in the "Website" field.
   - Click "Search" to retrieve the stored username and password.

3. **Generate Password:**
   - Click "Generate Password" to create a strong password.

---

## Error Handling
- **Data Not Found:** If the entered website name does not exist in the saved data, an error message will appear.
- **Missing Fields:** Ensure all fields are filled before saving credentials.

---

## Contribution
Feel free to fork this repository and submit pull requests to add new features or fix bugs.

---

## License
This project is licensed under the MIT License.

