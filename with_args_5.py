# with_args_5.py

def greeting(ip):
    op_length = len(ip) + 10
    styled_line = '-' * op_length
    print(styled_line)
    print(f'{ip:^{op_length}}')
    print(styled_line)

greeting('hi')
weather = 'Today would be a nice sunny day'
greeting(weather)
