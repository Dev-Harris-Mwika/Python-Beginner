camelot_lines = []
with open(r"F:\Udacity\python_beg\file_to_read.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())
        
print(camelot_lines)

