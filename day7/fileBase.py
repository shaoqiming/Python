# coding:UTF-8


def main():
    outfile = open('outefile.txt', 'w')
    outfile.writelines(["Hellow", ' ', "world"])
    outfile.close()
    infile = open('outefile.txt', 'r')
    print infile.read()


def ReadEmail():
    ftele1 = open('tele.txt', 'rb')
    ftele2 = open('email.txt', 'rb')
    #跳过第一行
    ftele1.readline()
    ftele2.readline()

    lines1 = ftele1.readlines()
    lines2 = ftele2.readlines()
    list1_name = []
    list1_tele = []
    list2_name = []
    list2_email = []
    for line in lines1:
        elements = line.split()
        list1_name.append(str(elements[0].decode('gbk')))
        list1_tele.append(str(elements[1].decode('gbk')))

    for line in lines2:
        elements1 = line.split()
        list2_name.append(str(elements1[0].decode('gbk')))
        list2_email.append(str(elements1[1].decode('gbk')))

    lines = []
    lines.append('姓名\t     电话\t     邮箱\n')

    for i in range(len(list1_name)):
        s = ''
        if list1_name[i] in list2_name:
            j = list2_name.index(list1_name[i])  #找到电话
            s = '\t'.join([list1_name[i], list1_tele[i], list2_email[i]])
            s += '\n'
        else:
            s = '\t'.join([list1_name[i], list1_tele[i], '--------'])
            s += '\n'

        lines.append(s)

    for i in range(len(list2_name)):
        s = ''
        if list2_name[i] not in list1_name:
            s = '\t'.join([list2_name[i], str('----'), list2_email[i]])
            s += '\n'
        lines.append(s)

    fetel3 = open('All.txt', 'w')
    fetel3.writelines(lines)

    ftele1.close()
    ftele2.close()
    fetel3.close()


ReadEmail()