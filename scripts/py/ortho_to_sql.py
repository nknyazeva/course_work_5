import re

# in_file = "/home/nknyazeva/courseWork5/data/macaca_mulatta/ortho_HSapiens_Mmulatta/InParanoid.H.sapiens-M.mulatta.tar"
# out_file = "/home/nknyazeva/courseWork5/data/macaca_mulatta/ortho_HSapiens_Mmulatta/ortho_H.sapiens-M.mulatta.sql"

in_file = "/Users/anastasia/IdeaProjects/course_work_5/test_data/InParanoid.H.sapiens-M.mulatta.tar"
out_file = "/Users/anastasia/IdeaProjects/course_work_5/test_data/ortho_H.sapiens-M.mulatta_sorted.sql"

f = open(in_file, "r")
file = []
for line in f:
    file.append(line)
f.close()


groups = {}
for i in range(len(file)):
    line = file[i]
    if 'Group of orthologs #' == line[:20]:
        n = re.search(r'#(\d+).', line).group(1)
        groups[n] = []
        next_line = file[i + 1]
        score_h = re.search(r'H.sapiens:[\d]+', next_line).group(0)
        score_m = re.search(r'M.mulatta:[\d]+', next_line).group(0)
        groups[n].append(score_h)
        groups[n].append(score_m)

        index = 2
        next_line = file[i + index]
        while 'Group of orthologs #' != next_line[:20]:
            if file[i + index + 1][0] != '#':
                if 'Bootstrap' != next_line[:9] and '_' != next_line[0]:
                    list_id = next_line.split('\t')
                    if list_id[0].strip() == '':
                        groups[n].append('None')
                    else:
                        groups[n].append(list_id[0].strip())
                    if list_id[3].strip() == '':
                        groups[n].append('None')
                    else:
                        groups[n].append(list_id[3].strip())
                index += 1
                next_line = file[i + index]
            else:
                break

file_write = open(out_file, "w")
for n in groups:
    # new!
    if len(groups[n]) == 4:
        file_write.write(str(n) + "\t" + '\t'.join(groups[n]) + '\n')
    #old
    #file_write.write(str(n) + "\t" + '\t'.join(groups[n]) + '\n')
file_write.close()

# 312 - more than one ortho
# 16322 - pairs
