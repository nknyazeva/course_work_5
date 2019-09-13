import re

in_file = '/mnt/lustre/nknyazeva/courseWork5/data/result/oma_id_pair_coordinates.sql'
out_file = '/mnt/lustre/nknyazeva/courseWork5/data/result/ortho_coordinates.sql'

# in_file = '/Users/anastasia/IdeaProjects/course_work_5/test_data/test_oma_id_pair_coordinates.sql'
# out_file = '/Users/anastasia/IdeaProjects/course_work_5/test_data/test_ortho_coordinates.sql'

file_in = open(in_file, 'r')
file_out = open(out_file, 'w')
for line in file_in:
    line = line.strip().split()
    id_mm = line[0]
    id_hs = line[3]
    chr_mm = 'chr' + line[1]
    chr_hs = line[4]
    coord_mm_tmp = re.findall(r'\d+', line[2])
    from_mm = coord_mm_tmp[0]
    to_mm = coord_mm_tmp[-1]
    coord_mm = chr_mm + ':' + min(from_mm, to_mm) + '-' + max(from_mm, to_mm)
    coord_hs_tmp = re.findall(r'\d+', line[5])
    from_hs = coord_hs_tmp[0]
    to_hs = coord_hs_tmp[-1]
    coord_hs = chr_hs + ':' + min(from_hs, to_hs) + '-' + max(from_hs, to_hs)
    file_out.write(id_mm + '\t' +
                   coord_mm + '\t' +
                   id_hs + '\t' +
                   coord_hs + '\n')

file_in.close()
file_out.close()