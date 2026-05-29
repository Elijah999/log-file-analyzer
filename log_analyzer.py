# ============================================
# Log File Analyzer
# Detects suspicious failed login attempts
# Author: [His Name]
# ============================================

# This dictionary will store how many times each IP address failed to log in
failed_attempts = {}

# Open and read the log file line by line
with open("auth.log", "r") as log_file:
    for line in log_file:
        # We only care about lines that show a FAILED login
        if "Failed password" in line:
            # Pull out the IP address from the line
            # Example line: "…Failed password for root from 192.168.1.105 port 22"
            parts = line.split()
            ip_address = parts[10]  # The IP is always the 11th word in this format
            
            # Add 1 to the count for this IP address
            if ip_address in failed_attempts:
                failed_attempts[ip_address] += 1
            else:
                failed_attempts[ip_address] = 1

# ============================================
# Print the Report
# ============================================
print("=" * 50)
print(" FAILED LOGIN ATTEMPT REPORT")
print("=" * 50)
print()

suspicious_found = False
for ip, count in failed_attempts.items():
    if count > 3:
        print(f"[ALERT] SUSPICIOUS - IP: {ip} | Failed Attempts: {count}")
        suspicious_found = True
    else:
        print(f"[INFO]  NORMAL - IP: {ip} | Failed Attempts: {count}")

print()
print("=" * 50)
if suspicious_found:
    print("[WARNING] ACTION REQUIRED: Suspicious IPs detected above.")
else:
    print("[OK] No suspicious activity detected.")
print("=" * 50)
