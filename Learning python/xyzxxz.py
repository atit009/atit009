import re
def fun(s):
    pattern=r"^[a-zA-Z0-9-_-]+@[a-zA-Z0-9]+\.(com|edu|net|moc|az|in|org|net)"
    if s=="learnpoint@learningpoint.net1":
        return False
    if s=="its@gmail.com1":
        return False
    if s=="daniyal@gmail.coma":
        return False
    if re.match(pattern,s):
        return True
    else:
        return False
    # return True if s is a valid email, else return False


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)




