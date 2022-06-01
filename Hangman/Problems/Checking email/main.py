def check_email(string):
    if (' ' not in string) and ('@' in string):
        return string.find('@') + 1 < string.rfind('.')   
    else:
        return False
