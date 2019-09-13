# in_file = '/Users/anastasia/IdeaProjects/course_work_5/test_data/test_ortho_coordinates_with_double.sql'
# out_file = '/Users/anastasia/IdeaProjects/course_work_5/test_data/test_ortho_coordinates.sql'

in_file = '/mnt/lustre/nknyazeva/courseWork5/data/result_2/ortho_coordinates_with_double.sql'
out_file = '/mnt/lustre/nknyazeva/courseWork5/data/result_2/ortho_coordinates.sql'

f_in = open(in_file, 'r')
lines = f_in.read().split('\n')

lines_wo_double = list(dict.fromkeys(lines))

f_out = open(out_file, 'w')
for line in lines_wo_double:
    f_out.write(line + '\n')
f_in.close()
f_out.close()


