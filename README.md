Log File Analyzer 

## What This Project Does This Python script analyzes Linux authentication log files to detect suspicious failed login activity. It reads through system logs, counts failed login attempts per IP address, and flags any IP with more than 3 failures as potentially malicious. 

## Why This Matters in Cybersecurity Brute force attacks — where hackers repeatedly guess passwords — are one of the most common attack vectors on networked systems. Security analysts use SIEM tools to detect exactly this pattern at scale. This project replicates that core detection logic in Python. 

## What It Does – Parses Linux auth.log format files – Counts failed SSH login attempts per IP address – Flags IPs exceeding 3 failed attempts as suspicious – Generates a clean summary report 

## Technologies Used – Python 3 – File I/O and string parsing – Dictionary data structures ## How to Run It 1. Clone this repository 2. Place your auth.log file in the same directory 3. Run: python log_analyzer.py 

## Sample Output <img width="416" height="146" alt="image" src="https://github.com/user-attachments/assets/0f85c9b8-18e0-465a-8b43-0e704041007f" />

## What I Learned Working on this project helped me understand how SIEM tools like Splunk and Wazuh detect brute force activity at scale. The same logic this script uses — parsing logs, counting events per source, flagging thresholds — is the foundation of real-world threat detection.

# log-file-analyzer
