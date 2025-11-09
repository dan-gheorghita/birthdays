```python
# Dictionary to store birthdays where the key is the name and the value is the birthday
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# Infinite loop to continuously prompt the user for input
while True:
    # Prompt the user to enter a name, or leave blank to quit
    print('Enter a name: (blank to quit)')
    name = input()  # Get the user's input

    # If the user enters a blank line, break out of the loop
    if name == '':
        break

    # Check if the name is in the birthdays dictionary
    if name in birthdays:
        # If the name is in the dictionary, print the birthday
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        # If the name is not in the dictionary, print a message and ask for the birthday
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()  # Get the user's input for the birthday
        birthdays[name] = bday  # Add the birthday to the dictionary
        print('Birthday database updated.')
```