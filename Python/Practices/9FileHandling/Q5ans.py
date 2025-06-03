'''
Create a program that reads from source.txt and writes each line to target.txt, 
prefixing each line with its line number (e.g., 1: Hello world).
'''

def copy_with_line_numbers(source, target):
    with open(source, 'rt') as src, open(target, 'wt') as tgt:
        for line_num, line in enumerate(src, start=1):
            tgt.write(f"{line_num}: {line}")


copy_with_line_numbers('Q5ans1.txt', 'Q5ans2.txt')

