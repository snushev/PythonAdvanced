import os

while True:
    command = input()
    if command == "End":
        break
    action = command.split('-')

    if action[0] == "Create":
        name = action[1]
        with open(name, 'w') as f:
            pass

    elif action[0] == "Add":
        name = action[1]
        text = action[2]
        with open(name, 'a') as f:
            f.write(text + "\n")

    elif action[0] == "Replace":
        name = action[1]
        old_text = action[2]
        new_text = action[3]
        try:
            with open(name, 'r') as f:
                content = f.read()

            content = content.replace(old_text, new_text)

            with open(name, 'w') as f:
                f.write(content)

        except FileNotFoundError:
            print("An error occurred")

    elif action[0] == "Delete":
        name = action[1]
        try:
            os.remove(name)
        except FileNotFoundError:
            print("An error occurred")
