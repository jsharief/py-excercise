def student_names(filename):
    regs = {}
    names = []
    with open(filename, 'r') as file:
        for line in file:
          # line = line.rstrip('\n')
           mark_lst = line.split()# optional: remove newline
           tot = sum(int(x) for x  in mark_lst[2:6])
           print(sum(mark_lst[2:6]))
           regs[mark_lst[0]] = tot
    for name , tot in regs.items():
        if tot > 10:
           names.append(name)
    print(names)


student_names('students.txt')
