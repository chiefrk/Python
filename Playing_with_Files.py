#open a new file and write contents
with open('C:\\Users\\mramakri\\OneDrive - Informatica\\Documents\\Python Scripts\\Write_Op.txt', mode='w') as nf:
    nf.write('This is a new file being created by a python code\nThis is the second line of the file\nThis is the third line of the file\n')
#read file contents from the fle created in the last step
with open('C:\\Users\\mramakri\\OneDrive - Informatica\\Documents\\Python Scripts\\Write_Op.txt', mode='r') as rf:
    op=rf.readlines()
    print(op)
    rf.seek(0)
    op=rf.read()
    print(op)
#append contents to end of the file
with open('C:\\Users\\mramakri\\OneDrive - Informatica\\Documents\\Python Scripts\\Write_Op.txt', mode='a') as af:
    af.write('This is the fourth line')
with open('C:\\Users\\mramakri\\OneDrive - Informatica\\Documents\\Python Scripts\\Write_Op.txt', mode='r') as rf:
    rf.seek(0)
    op=rf.read()
    print(f'The output of the append operation is {op}')
