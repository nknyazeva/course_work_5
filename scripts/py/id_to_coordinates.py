in_file_ortho = "/home/nknyazeva/courseWork5/data/macaca_mulatta/ortho_HSapiens_Mmulatta/oma_id_ortho.txt"
in_file_annotations = "/home/nknyazeva/courseWork5/data/oma/oma-protein-annotations.txt"
out_file = "/home/nknyazeva/courseWork5/data/macaca_mulatta/ortho_HSapiens_Mmulatta/oma_id_ortho_coordinates.txt"

# in_file_ortho = "/Users/anastasia/IdeaProjects/course_work_5/test_data/test_oma_id_ortho.txt"
# in_file_annotations = "/Users/anastasia/IdeaProjects/course_work_5/test_data/test_oma-protein-annotations.txt"
# out_file = "/Users/anastasia/IdeaProjects/course_work_5/test_data/test_oma_id_ortho_coordinates.txt"


f = open(in_file_ortho, "r")
oma_id = []
for line in f:
    if line[0] != '#':
        line = line.strip().split()
        oma_id.append(line)
f.close()
print('read oma_id_ortho.txt')


id_coord = {}

f_coord = open(in_file_annotations, "r")
for line in f_coord:
    if line[0] != '#':
        line = line.strip().split()
        coord = line[3]
        one_oma_id = line[0]
        id_coord[one_oma_id] = coord
f_coord.close()
print('read oma-protein-annotations.txt')

f_out = open(out_file, "w")
for pair_id in oma_id:
    if pair_id[0] in id_coord.keys() and pair_id[1] in id_coord.keys():
        f_out.write(pair_id[0] + '\t')
        f_out.write(id_coord[pair_id[0]] + '\t')
        f_out.write(pair_id[1] + '\t')
        f_out.write(id_coord[pair_id[1]] + '\n')

f_out.close()



