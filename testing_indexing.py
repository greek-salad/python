first_name =input("What is your first name?")
surname = input('What is your surname?')
middle_name_question = input('Do you have a middle name?')
if middle_name_question in ['n','no','N','No','NO']:
    initials = first_name[0] + '.' + surname[0]
    print('Your initials are ' + initials)
else:
    middle_name = input('What is your middle name?')
    initials = first_name[0] + '.' + middle_name[0] + '.' + surname[0]
    print('Your initials are ' + initials)
