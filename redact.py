import re

text = "User logged in from 192.168.0.1 with hostname server01"

# Example regex for IP
ip_pattern = r"\b\d{1,3}(\.\d{1,3}){3}\b"
redacted_text = re.sub(ip_pattern, "***IP***", text)

print(redacted_text)
