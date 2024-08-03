# You will be given some emails until you receive the command "End". Create the following
# custom exceptions to validate the emails:
# •	NameTooShortError - raise it when the name in the email is less than or equal to 4
# ("peter" will be the name in the email "peter@gmail.com")
# •	MustContainAtSymbolError - raise it when there is no "@" in the email
# •	InvalidDomainError - raise it when the domain of the email is invalid (valid domains
# are: .com, .bg, .net, .org)
# When an error is encountered, raise it with an appropriate message:
# •	NameTooShortError - "Name must be more than 4 characters"
# •	MustContainAtSymbolError - "Email must contain @"
# •	InvalidDomainError - "Domain must be one of the following: .com, .bg, .org, .net"
# Hint: use the following syntax to add a message to the Exception:
# MyException("Exception Message")
# If the current email is valid, print "Email is valid" and read the next one

class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass


line = input()

while line != 'End':

    if '@' not in line:
        raise MustContainAtSymbolError("Email must contain @")

    if len(line.split('@')[0]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if line.split('.')[-1] not in ['com', 'bg', 'net', 'org']:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, "
                                 ".org, .net")

    print('Email is valid')

    line = input()
