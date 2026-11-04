STUDENT LIST WEB APP (Python + SQLite)

WHAT'S INCLUDED
- Flask web app styled to resemble the supplied screenshot
- SQLite database (students.db), created automatically
- Starter rows matching the screenshot
- Add and delete student functions
- Listens on every network interface (0.0.0.0), port 5000

WINDOWS SETUP
1. Extract this folder.
2. Open Command Prompt or PowerShell inside the extracted student_list_app folder.
3. (Recommended) Create and activate a virtual environment:
   py -m venv .venv
   .venv\Scripts\activate
4. Install dependencies:
   py -m pip install -r requirements.txt
5. Start:
   py app.py
6. On the host computer, open:
   http://127.0.0.1:5000

OPEN IT FROM OTHER DEVICES ON THE SAME NETWORK
1. On the host PC, run ipconfig.
2. Find the active network adapter's IPv4 Address, for example 192.168.1.25.
3. From another device on the same Wi-Fi/LAN, open:
   http://192.168.1.25:5000
   Replace the example IP with the host PC's actual IPv4 address.

WINDOWS FIREWALL
If other devices cannot connect, allow inbound TCP port 5000 on the host PC.
In Windows Defender Firewall with Advanced Security, create an inbound rule:
- Port
- TCP
- Specific local ports: 5000
- Allow the connection
- Apply to the appropriate private network profile

IMPORTANT
- Keep app.py running while other devices use the app.
- This is for a trusted local network, not direct public-internet exposure.
- Change app.secret_key before real deployment.
- The built-in Flask server is for development/classroom use, not a production deployment.
- SQLite is stored in students.db beside app.py. Back up that file to back up records.
