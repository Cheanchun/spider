import json
fp = open('page.txt',mode='r')
content = fp.readline()
while content:
    data_1 = eval(content)
    data_2 = eval(fp.readline())
    print data_1.keys()
    print data_2.keys()


