New Tool Alert: KHULAIF TOOL - Advanced Email OSINT
I'm excited to share a powerful new resource for security researchers, penetration testers, and anyone interested in Open Source Intelligence (OSINT)!

Introducing KHULAIF TOOL - an advanced Python utility designed to gather comprehensive information from a target email address.

🔍 What Does it Do?
This tool automates several critical OSINT checks, providing a consolidated view for deeper investigation:

DNS Record Lookup: Extracts vital domain information, including MX (Mail Exchange), A (IP Address), and TXT records (SPF, domain verification).

Data Breach Check: Integrates with the HaveIBeenPwned API to instantly check if the target email has been compromised in known data breaches.

Social Media Discovery: Searches for associated profiles on platforms like GitHub, Instagram, and Twitter.

Google Dork Generation: Creates specialized search links for advanced, deeper investigation using Google Dorking techniques.

💡 Why is this useful?
Whether you're performing a vulnerability assessment, conducting a due diligence check, or simply hardening your own digital footprint, KHULAIF TOOL provides a quick and efficient way to gather the initial intelligence needed.

💻 How to Get Started:
Make sure you have Python installed.

Clone the repository (or download the tool).

Install dependencies: python -m pip install -r requirements.txt

Run a basic scan: python khulaif_tool.py -e yourtarget@example.com

P.S. Don't forget to configure your HaveIBeenPwned API key in config.json for the breach detection feature!

⚠️ A quick reminder (Legal Notice): This tool is for educational and legitimate security research purposes only. Only use it on email addresses you own or have explicit permission to investigate.
