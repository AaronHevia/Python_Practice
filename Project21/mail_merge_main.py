# Creates a letter using starting_letter.txt for each name in invited_names.txt
NAME_HOLDER = '[name]'

with open('./Input/Names/invited_names.txt', 'r') as name_data:
    names = name_data.readlines()
for name in range(len(names)):
    names[name] = names[name].strip('\n')

# Create a template letter to print.
with open('./Input/Letters/starting_letter.txt', 'r') as letter:
    template = letter.read()

# Save the letters in the folder "ReadyToSend".
for name in range(len(names)):
    # Replace the [name] placeholder with the actual name.
    draft = template.replace(NAME_HOLDER, names[name])
    with open(f'./Output/ReadyToSend/letter_for_{names[name]}.txt', 'w') as final_letter:
        final_letter.write(draft)
