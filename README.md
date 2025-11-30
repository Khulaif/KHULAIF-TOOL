=====================================================
          KHULAIF TOOL - Advanced Email OSINT
=====================================================

WHAT IS KHULAIF TOOL?
---------------------
KHULAIF TOOL is an advanced Email OSINT (Open Source Intelligence) tool
that helps you gather information about email addresses including:
- DNS Records (MX, A, TXT)
- Data Breach Information (via HaveIBeenPwned)
- Social Media Profiles
- Google Dork Search Links


INSTALLATION
------------
1. Make sure Python is installed on your system

2. Install required dependencies:
   Open Command Prompt or PowerShell in this folder and run:
   
   python -m pip install -r requirements.txt


CONFIGURATION (Optional)
------------------------
To use the HaveIBeenPwned API feature, you need an API key:

1. Get your free API key from: https://haveibeenpwned.com/API/Key
2. Open "config.json" file
3. Replace "your_api_key_here" with your actual API key
4. Save the file

Example config.json:
{
    "hibp_api_key": "abc123xyz456youractualkey"
}


HOW TO USE
----------
Basic command format:

python khulaif_tool.py -e <target_email>

Examples:

1. Basic scan:
   python khulaif_tool.py -e test@example.com

2. Scan your own email:
   python khulaif_tool.py -e yourname@gmail.com

3. View help:
   python khulaif_tool.py -h


WHAT THE TOOL DOES
------------------
When you run the tool with an email address, it will:

1. Display the KHULAIF TOOL banner
2. Validate the email format
3. Extract domain information
4. Query DNS records:
   - MX Records (Mail Exchange servers)
   - A Records (IP addresses)
   - TXT Records (Domain verification, SPF, etc.)
5. Check HaveIBeenPwned for data breaches (if API key configured)
6. Search for social media profiles (GitHub, Instagram, Twitter)
7. Generate Google Dork search links for deeper investigation


OUTPUT INFORMATION
------------------
The tool provides color-coded output:
- YELLOW: Processing/Information
- GREEN: Success/Found
- RED: Error/Not Found
- CYAN: Banner and Headers


TROUBLESHOOTING
---------------
Problem: "pip is not recognized"
Solution: Use "python -m pip install -r requirements.txt"

Problem: "Python is not recognized"
Solution: Make sure Python is installed and added to PATH

Problem: No breaches shown even though email is compromised
Solution: Add your HaveIBeenPwned API key to config.json

Problem: Unicode/Encoding errors
Solution: Make sure your terminal supports UTF-8 encoding


LEGAL NOTICE
------------
This tool is for educational and legitimate security research purposes only.
Only use this tool on email addresses you own or have explicit permission
to investigate. Unauthorized use may violate privacy laws and terms of service.


SUPPORT
-------
For questions or issues, please ensure:
1. Python is properly installed
2. All dependencies are installed
3. You have internet connection
4. The email format is valid


=====================================================
           Created by: KHULAIF
           Version: 1.0
=====================================================
