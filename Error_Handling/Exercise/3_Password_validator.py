class PasswordTooShortError(Exception):
    pass

class PasswordTooCommonError(Exception):
    pass

class PasswordNoSpecialCharactersError(Exception):
    pass

class PasswordContainsSpacesError(Exception):
    pass

while True:
    password = input()

    if password == "Done":
        break

    elif len(password) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    elif (any(char.isalpha() for char in password)
          or any(char.isdigit() for char in password)
          or any(not char.isalnum() for char in password)):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    elif not any(char in password for char in ["@", "*", "&", "%"]):
       raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    elif " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    else:
        print("Password is valid")