# nested_braces_6.py

def nested_braces(s):
    lvl = 0
    max_lvl = 0
    for x in s:
        if x == '{':
            lvl += 1
        if x == '}':
            lvl -= 1
        if lvl > max_lvl:
            max_lvl = lvl
        if lvl < 0:
            max_lvl = -1
            break
    if lvl != 0:
        max_lvl = -1
    print(max_lvl)
    
nested_braces('{{a+2}*{{b+{c*d}}+e*d}}')
nested_braces('{a}*b{')
nested_braces('}a+b{')
