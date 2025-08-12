import re

class EmailAddressParser:
    def __init__(self, emails):
        self.emails = emails

    def parse(self):
        # Regex for valid emails
        pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
        matches = re.findall(pattern, self.emails)
        # Remove duplicates and sort
        return sorted(set(matches))
