SECURE TASK MANAGER - INSTALLATION INSTRUCTIONS
===============================================

PREREQUISITES:
- Python 3.10 or higher
- Internet connection (to install dependencies)

INSTALLATION STEPS:
1. Unzip the project folder.
2. Open a terminal/command prompt inside the folder.
3. Create a virtual environment:
   python -m venv venv
4. Activate the virtual environment:
   - Windows: venv\Scripts\activate
   - Linux/Mac: source venv/bin/activate
5. Install dependencies:
   pip install -r requirements.txt

CONFIGURATION:
1. The project uses a .env file for security configuration.
2. Ensure the .env file exists in the root directory with the following content:
   SECRET_KEY=your-secret-key-here
   DEBUG=True

RUNNING THE APPLICATION:
1. Initialize the database:
   python manage.py migrate
2. Create an Admin user (optional, for accessing Audit Logs):
   python manage.py createsuperuser
3. Start the server:
   python manage.py runserver
4. Access the app at: http://127.0.0.1:8000

### **HOW TO RUN THE SECURE TASK APP (BEGINNER GUIDE)**

**BEFORE YOU START:**

* Make sure you have **Python** installed on your computer.
* *Check:* Open Command Prompt (type `cmd` in Windows search) and type `python --version`. If you see numbers (like `3.10` or `3.12`), you are good.



---

### **STEP 1: UNZIP THE FOLDER**

1. Download the zip file I sent you.
2. Right-click the zip file and choose **Extract All...**
3. Click **Extract**.
4. Open the new folder so you can see files like `manage.py` and `requirements.txt`.

---

### **STEP 2: OPEN THE COMMAND CENTER**

1. Click inside the address bar at the top of the folder window (where it says `C:\Users\YourName...`).
2. Delete the text there, type `cmd`, and press **Enter**.
* *A black box should pop up. This is where we will type the commands.*



---

### **STEP 3: CREATE THE ENVIRONMENT**

We need a clean space to install the tools. Copy and paste these commands into the black box one by one.

**Command 1:** (Creates the environment)

```cmd
python -m venv venv

```

*(Wait a few seconds until the cursor appears again).*

**Command 2:** (Turns it on)

```cmd
venv\Scripts\activate

```

*(You should see `(venv)` appear at the start of the line).*

**Command 3:** (Installs the tools)

```cmd
pip install -r requirements.txt

```

*(You will see a lot of text scrolling. Wait until it stops).*

---

### **STEP 4: CREATE THE SECRET KEY**

The app needs a password to run securely.

1. Go back to your folder window (keep the black box open).
2. Right-click in the empty space -> **New** -> **Text Document**.
3. Name the file exactly: `.env`
* *(If it asks "Are you sure you want to change the extension?", say **YES**).*
* *(If it stays as `.env.txt`, that is okay too, but try to make it just `.env`).*


4. Open that file with Notepad and paste this exactly:
```text
SECRET_KEY=django-insecure-test-key-12345
DEBUG=True

```


5. **Save** and close it.

---

### **STEP 5: RUN THE APP!**

Go back to the black box. Since I included the database, you don't need to do any setup. Just run it!

**Command 4:**

```cmd
python manage.py runserver

```

If it says `Starting development server at http://127.0.0.1:8000/`, **IT WORKED!** 🚀

---

### **STEP 6: LOG IN**

1. Open your web browser (Chrome, Edge, etc.).
2. Type this address: `http://127.0.0.1:8000`
3. Log in with these details:
* **Username:** `admin`
* **Password:** `password123`



**You are done!**