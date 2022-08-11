# default_args_5.py
def greeting(ip, style='-', spacing=10, padding=' '):
    op_length = len(ip) + 10
    styled_line = style * op_length
    print(styled_line)
    print(f'{ip:{padding}^{op_length}}')
    print(styled_line)

greeting('hi')
greeting('bye', spacing=5)
greeting('hello', style='=')
greeting('good day', ':', 2)
greeting('good day', '(*)', 2)
greeting('good day', ':', 2, '_')
greeting(spacing=5, ip='Oh!')
