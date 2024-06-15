** SIEM Log Parsing and Alert Generation (Python Example):

import re

def parse_log_line(line):
    # Extract relevant log data using regular expressions or parsing libraries
    timestamp = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", line).group()
    event_type = re.search(r"\[(.*?)\]", line).group(1)
    # ... Extract other relevant fields

    return {
        "timestamp": timestamp,
        "event_type": event_type,
        # ... Other extracted fields
    }

def analyze_logs(log_file):
    alerts = []
    with open(log_file, "r") as f:
        for line in f:
            parsed_log = parse_log_line(line)
            if is_suspicious_activity(parsed_log):  # Replace with your logic for identifying suspicious events
                alerts.append(parsed_log)

    return alerts

# Send alerts to security team or trigger further investigation logic

** 3. SIEM Log Parsing and Alert Generation:
This code demonstrates parsing log lines and generating alerts.
The parse_log_line function extracts relevant data from a log line using regular expressions (example shown) and returns a dictionary containing the extracted information.
The analyze_logs function iterates through log lines:
It parses each line using parse_log_line.
It checks if the parsed data indicates suspicious activity using the is_suspicious_activity function (implementation not shown).
If suspicious activity is detected, the parsed log data is appended to the alerts list.
The function ultimately returns a list of alerts containing information from suspicious log lines.




## Remember: The actual output of these functions will depend on how they are integrated into a larger system.  For example, the MFA function would likely be used within a login process, and the user would see prompts for username, password, and OTP. The access control function would be used within a web application to determine what resources a user can access. The SIEM code would likely be used in a security operations center (SOC) to monitor logs and generate alerts for investigation.
