import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"^[A-Z][A-z-']+\s?[A-z'-]+$"
name_regex = re.compile(name)

phone_number = r"\(?[0-9]{3}\)?(\s|-)?[0-9]{3}-?[0-9]{4}"
phone_regex = re.compile(phone_number)

email_address = r"^[A-z]\w+\.?\w+@[A-z]+\.[a-z]{2,3}"
email_regex = re.compile(email_address)
