# Fungsi split buatan
def my_split(string, delimiter=','):
    segments = []
    segment = ''
    for char in string:
        if char == delimiter:
            segments.append(my_strip(segment))  # Strip leading and trailing whitespace
            segment = ''
        else:
            segment += char
    segments.append(my_strip(segment))  # Strip leading and trailing whitespace
    return segments