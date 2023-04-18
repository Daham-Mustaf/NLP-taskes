import re 


def extract_order_num(urls):
    order_num=[]
    for url in urls:
        match = re.findall( r"(\d{10})|(\(\d{3}\)-\d{3}-\d{4})", url)
        if match:
            # order_num.append(match)
            order_num.extend([num for num in match[0] if num])
    return order_num

# Task: Given a list of URLs, extract the domain name from each URL.

urls = ['https://www.google.com/search?q=python',
        'https://en.wikipedia.org/wiki/Regular_expression',
        'https://www.amazon.com/gp/product/B09B6GLRHS']

# ['google.com', 'wikipedia.org', 'amazon.com']

def extract_domain_name(urls):
    domain_names = []
    for url in urls:
        match = re.search(r'(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?([^:\/\n]+)', url)
        if match:
            domain_names.append(match.group(1))
    return domain_names

def extract_patterns(pattern, string_list):
    matches = []
    for string in string_list:
        match = re.findall(pattern, string)
        if match:
            matches.extend(match)
    return matches

print(extract_domain_name(urls))

chats = [
    'codebasics: you ask lot of questions 😠  1235678912, abc@xyz.com',
    'codebasics: here it is: (123)-567-8912, abc@xyz.com',
    'codebasics: yes, phone: 1235678912 email: abc@xyz.com'
]



oreder = extract_order_num(chats)
list =oreder.extend([num for num in oreder[0] if num])
print(oreder)


# extract all email addresses from a list of strings
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
string_list = ['Contact me at john.doe@example.com', 'Email me at jane.smith@example.com']
email_matches = extract_patterns(email_pattern, string_list)
print(email_matches)

# Task: Given a list of phone numbers in different formats, extract and normalize them to a standard format.
text = "Please call me at (123) 456-7890 or 123-456-7891 if you have any questions."

matches = re.findall(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}", text)

print(matches)


# Task: Given a list of email addresses, extract the username and domain name from each email address.
emails = ['john.doe@example.com', 'jane.doe@example.org', 'jim.smith@gmail.com']

parsed_emails = []
for email in emails:
    match = re.match(r'^([\w.-]+)@([\w.-]+)$', email)
    if match:
        username = match.group(1)
        domain = match.group(2)
        parsed_emails.append((username, domain))
        
print(parsed_emails)



def extract_dates(text):
    pattern = r"\b([0123]?\d)[\./-]([01]?\d)[\./-]([12]\d{3})\b"
    matches = re.findall(pattern, text)
    return [f"{match[0]}.{match[1]}.{match[2]}" for match in matches]

text = "Some possible dates are 12/31/2022, 1-15-2023, and 02.28.2023"
dates = extract_dates(text)
print(dates) # Output: ['12.31.2022', '1.15.2023', '02.28.2023']






