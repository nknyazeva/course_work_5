import os

in_dir = '/mnt/lustre/nknyazeva/courseWork5/data/result/genes/'
out_file = '/mnt/lustre/nknyazeva/courseWork5/data/result/all_shared_snp.txt'
# in_dir = '/Users/anastasia/IdeaProjects/course_work_5/test_data/to_muscle'
# out_file = '/Users/anastasia/IdeaProjects/course_work_5/test_data/to_muscle/test.txt'


list_files = []
for (dirpath, dirnames, filenames) in os.walk(in_dir):
    for file in filenames:
        file_path = dirpath + '/' + file
        list_files.append(file_path)
print('Len list_files' + str(len(list_files)))

file_out = open(out_file, 'w')

for file in list_files:
    if 'shared' in file:
        if os.stat(file).st_size != 0:
            result = file + '\t'

            f = open(file, 'r')
            for line in f:
                result = result + line.strip() + '\t'
            result = result + '\n'

            f.close()
            file_out.write(result)

file_out.close()

