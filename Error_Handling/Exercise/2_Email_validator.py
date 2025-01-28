class NameTooShortError(Exception):
     pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

domain = (".com", ".bg", ".org", ".net")
while True:
    email = input()
    if email == "END":
        break

    elif "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    elif email.index("@") < 4:
        raise NameTooShortError("Name must be more than 4 characters")

    elif not email.endswith(domain):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    
    else:
        print("Email is valid")
