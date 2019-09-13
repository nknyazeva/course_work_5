in_file = '/home/nknyazeva/courseWork5/data/result/id_human.sql'
file_ids = '/mnt/lustre/nknyazeva/courseWork5/data/oma/oma-uniprot.txt'
out_file = '/home/nknyazeva/courseWork5/data/result/oma_id_human.sql'

file_ids = open(file_ids, 'r')
dict_ids = {}
for line in file_ids:
    if line[0] != '#':
        line = line.strip().split('\t')
        dict_ids[line[1]] = line[0]
file_ids.close()

f_in = open(in_file, 'r')
f_out = open(out_file, 'w')
for line in f_in:
    line = line.strip()
    f_out.write(dict_ids[line] + '\n')
f_in.close()
f_out.close()


