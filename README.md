Here’s a detailed **README** guide that you can use for your **GitHub repository**. This guide is written in a clear, structured, and beginner-friendly way to help anyone set up and use your program. 🚀  

---

# **Keystroke-Based Application Launcher**  

 **This program monitors keystrokes and executes a specific action (like opening a website or app) when a predefined keyword is typed outside text editors.**  

🔹 **Use Case:** Instead of manually opening a specific website (e.g., Kaggle) or application, simply type a keyword anywhere, and the program will launch it automatically.  

---

## 📌 **Features**
✅ Runs in the background, silently monitoring keystrokes.  
✅ Detects a specific keyword typed outside of writing applications.  
✅ Executes a custom command (e.g., opening a website, launching an app).  
✅ Starts automatically when Windows boots up.  

---

## 🖥️ **How It Works**
1. The script listens to **all keystrokes**.  
2. If the predefined keyword (e.g., `"kaggle"`) is typed **outside** of a text editor (e.g., Notepad, Word, VS Code), the program executes an action.  
3. By default, the action is **opening a Chrome profile with a specific URL** (but you can modify it to run any command).  

---

## 🚀 **Installation Guide**

### 🔹 **Step 1: Clone the Repository**
Download the code from GitHub:  
```bash
git clone https://github.com/yourusername/keystroke-launcher.git
cd keystroke-launcher
```

---

### 🔹 **Step 2: Install Dependencies**
The script requires some Python libraries. Install them using:  
```bash
pip install pyinstaller pynput pygetwindow pywin32
```

#### **Required Libraries:**
- `pyinstaller` → To convert Python scripts into `.exe`.  
- `pynput` → To listen to keystrokes.  
- `pygetwindow` & `pywin32` → To check which application is currently active.  

---

### 🔹 **Step 3: Configure Your Command**
Modify **`main.py`** to execute the desired action when the keyword is detected.

#### **Default: Opens a Specific Website in Chrome**
```python
import subprocess

def execute_kaggle():
    subprocess.Popen(
        ["start", "chrome", "--Profile-Directory=`Your Profile Number'", "your_link"],
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

if __name__ == "__main__":
    execute_kaggle()
```
👉 **Change `your_link`** to the desired website URL (e.g., Kaggle, GitHub, or any other).  
👉 If using **multiple Chrome profiles**, replace `Your Profile Number` with the correct profile.  

#### **Modify to Open an Application Instead**
If you want to launch a local application instead (e.g., Notepad), replace `execute_kaggle()` with:
```python
subprocess.Popen(["notepad.exe"])
```

---

## 🔄 **Running the Program**
Once configured, run the program using:  
```bash
python keystroke_record_check.py
```
This will start listening for the keyword. If typed outside text editors, the program executes the command.  

---

## 🔹 **Step 4: Convert Python Script to Executable (`.exe`)**
To run the program without Python installed, convert it into a standalone Windows executable:

```bash
pyinstaller --onefile --noconsole --icon=your_icon.ico keystroke_record_check.py
```

### Explanation:
- `--onefile` → Bundles everything into a single `.exe` file.  
- `--noconsole` → Runs the program in the background (no visible terminal).  
- `--icon=your_icon.ico` → (Optional) Custom icon for the executable.  

 **The `.exe` file will be generated inside the `dist/` folder.**

---

## 🖥️ **Step 5: Run the Program on Startup**
To ensure the program launches every time the system starts, follow one of these methods:

### **Method 1: Add to Windows Startup Folder**
1. Press `Win + R`, type:
   ```
   shell:startup
   ```
   and hit **Enter** to open the Startup folder.
2. Copy the **`keystroke_record_check.exe`** from `dist/` and paste it into this folder.  
3. The program will now **automatically start every time you log in**.  

---

### **Method 2: Add via Windows Registry (Alternative)**
1. Press `Win + R`, type `regedit`, and hit **Enter**.  
2. Navigate to:
   ```
   HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
   ```
3. Right-click → **New → String Value**.  
4. Name it something like `AutoScript`.  
5. Double-click it and set its value to:
   ```
   "C:\path\to\your\keystroke_record_check.exe"
   ```
6. Click **OK**, and restart your computer.  

---

## **Step 6: Testing & Debugging**
1. Restart your PC to check if the script starts on login.  
2. Type the **keyword** (e.g., `"kaggle"`) in any **non-writing** app (e.g., desktop, file explorer).  
3. If the expected action happens (e.g., opening Chrome), the setup is working!  

---

## **How to Stop or Uninstall the Program**
- **Stop the script manually**: Open Task Manager (`Ctrl + Shift + Esc`), find `keystroke_record_check.exe`, and **end the process**.  
- **Remove from Startup**:
  - If added to **Startup folder**, delete it from `shell:startup`.  
  - If added to **Registry**, delete the `AutoScript` entry from `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`.  

---

## **Conclusion**
You now have a Python-based keystroke detection program that:
✅ Runs silently in the background.  
✅ Detects specific keystrokes outside writing apps.  
✅ Launches a predefined action (e.g., open a website or app).  
✅ Automatically starts when Windows boots up.  

This method can be used for **any script** that needs to trigger commands based on keystrokes. 🎉  

💡 **Want to extend this project?** Modify `execute_kaggle()` to perform custom tasks like opening documents, sending notifications, or running scripts!  

🔗 **Contribute & Feedback**: Feel free to suggest improvements, report issues, or fork this project.  

---

🚀 **Happy coding!** 😊
