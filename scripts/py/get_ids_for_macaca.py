in_file = '/home/nknyazeva/courseWork5/data/macaca_mulatta/ortho_HSapiens_Mmulatta/common_ortho_H.sapiens-M.mulatta.sql'
out_file = '/home/nknyazeva/courseWork5/data/result/oma_id_macaca.sql'

f_in = open(in_file, 'r')
f_out = open(out_file, 'w')
for line in f_in:
    line = line.strip().split()
    f_out.write(line[6] + '\n')
f_in.close()
f_out.close()
