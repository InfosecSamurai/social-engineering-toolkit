# Social Engineering Toolkit (SET) - Penetration Testing Framework

🔥 **Overview**  
The Social Engineering Toolkit (SET) is an advanced penetration testing framework designed to simulate social engineering attacks for security awareness training and ethical hacking. It includes phishing, smishing, Wi-Fi attacks, and other social engineering techniques to assess an organization's susceptibility to such attacks.

🚨 **WARNING**: This tool is for legal penetration testing and educational purposes only. Unauthorized use is strictly prohibited and may be punishable under applicable laws.

📌 **Features**
- ✅ **Email Phishing**: Fake login pages and deceptive emails to collect credentials.
- ✅ **SMS Phishing (Smishing)**: Sending fraudulent messages to deceive victims into clicking malicious links.
- ✅ **Evil Twin Wi-Fi Attack**: Creating a fake Wi-Fi hotspot to capture login credentials.
- ✅ **USB Drop Attack**: Simulating the attack where malicious USBs trick users into executing payloads.
- ✅ **Pretexting & Information Gathering**: Collecting victim information for further exploitation.
- ✅ **Multi-threaded Logging**: Stores captured credentials, timestamps, and victim interactions.

🛠️ **Installation**
1. **Prerequisites**:
   - Ensure your system has:
     - Python 3.8+
     - Pip (Python package manager)
     - Aircrack-ng (for Wi-Fi attacks)
     - A wireless network adapter supporting monitor mode (for Evil Twin attacks)

2. **Install Dependencies**:
   Clone the repository and install required Python packages:
   ```bash
   git clone https://github.com/InfosecSamurai/social-engineering-toolkit.git
   cd social-engineering-toolkit
   pip install -r requirements.txt
   ```

3. **Configure Settings**:
   Update the `config/settings.conf` file with your email credentials, Twilio API keys, and Wi-Fi interface details.
   ```bash
   nano config/settings.conf
   ```

🚀 **Usage Guide**
1. **Email Phishing**:
   Start a phishing attack that sends fraudulent emails with fake login pages:
   ```bash
   python attacks/phishing/web_page.py
   ```

   **How It Works**:
   - Hosts a fake login page on a local or remote web server.
   - Captures entered credentials and saves them to `stolen_credentials.txt`.
   - Redirects victims to a legitimate page after submission.

2. **SMS Phishing (Smishing)**:
   Send fraudulent SMS messages to deceive victims:
   ```bash
   python utils/sms_utils.py
   ```

   **How It Works**:
   - Uses Twilio API to send fake messages.
   - Redirects victims to phishing websites.

3. **Evil Twin Wi-Fi Attack**:
   Create a fake Wi-Fi hotspot and capture credentials:
   ```bash
   python utils/wifi_utils.py
   ```

   **How It Works**:
   - Creates a Wi-Fi network with the same SSID as a real one.
   - Captures login attempts from unsuspecting users.

4. **Victim List Management**:
   Store target information in `config/victims_list.txt`.
   ```plaintext
   email:victim1@example.com
   email:victim2@example.com
   sms:+1234567890
   sms:+1987654321
   ```

5. **Stopping an Attack**:
   To stop any running attack, use:
   ```plaintext
   CTRL + C
   ```

⚠️ **Legal Disclaimer**: This tool is strictly for authorized penetration testing and security awareness training. 
- Do NOT use it for illegal activities.
- Unauthorized access to computer systems is a crime.
- Obtain written permission before testing any system.
- Use this tool only for ethical hacking and cybersecurity research.

🛠️ **Troubleshooting**
- **Issue: "ModuleNotFoundError"**
  - Run:
  ```bash
  pip install -r requirements.txt
  ```
- **Issue: "Permission Denied"**
  - Try running with sudo (on Linux/Mac):
  ```bash
  sudo python attacks/phishing/web_page.py
  ```
- **Issue: "No wireless interface found"**
  - Check your Wi-Fi adapter:
  ```bash
  airmon-ng
  ```
  - Enable monitor mode:
  ```bash
  airmon-ng start wlan0
  ```

📚 **References**
- 🔹 Kali Linux Social Engineering Toolkit
- 🔹 MITRE ATT&CK: Social Engineering
- 🔹 Phishing Awareness Training

📧 **Contact**
For ethical hacking research, feel free to reach out:
- 📌 Email: InfosecSamurai@onmail.com
- 📌 GitHub: github.com/InfosecSamurai

**Stay ethical. Hack responsibly.** 🛡️