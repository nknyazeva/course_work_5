import os

file_in = '/mnt/lustre/nknyazeva/courseWork5/data/result/ortho_coordinates.sql'
path = '/mnt/lustre/nknyazeva/courseWork5/data/result/genes/ortho_'

# path = "/Users/anastasia/IdeaProjects/course_work_5/test_data/test_ortho/ortho_"
# file_in = '/Users/anastasia/IdeaProjects/course_work_5/test_data/test_ortho_coordinates.sql'

genes_list = open(file_in, 'r')

for line in genes_list:

    values = line.strip().split('\t')
    if len(values) != 1:

        main_name = values[0] + '_' + values[2]

        os.mkdir(path + main_name)
        os.mkdir(path + main_name + '/' + values[0])
        os.mkdir(path + main_name + '/' + values[2])

genes_list.close()