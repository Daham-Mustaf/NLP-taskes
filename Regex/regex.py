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







