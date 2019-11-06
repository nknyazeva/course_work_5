name_in_file = '/home/nknyazeva/courseWork5/data/result/oma_id_macaca.sql'
name_oma_file = '/home/nknyazeva/courseWork5/data/oma/oma-uniprot.txt'
name_out_file = '/home/nknyazeva/courseWork5/data/result/oma_id_macaca_new.sql'

oma_uniprot = {}
with open(name_oma_file, 'r') as oma_file:
    for line in oma_file:
        line = line.strip().split()
        oma_uniprot[line[1]] = line[0]

with open(name_in_file, 'r') as in_file:
    with open(name_out_file, 'w') as out_file:
        for line in in_file:
            id = line.strip()
            if 'MACMU' != line[0:5]:
                if id in oma_uniprot.keys():
                    out_file.write(oma_uniprot[id] + '\n')
                elif id.split('_')[0] in oma_uniprot.keys():
                    out_file.write(oma_uniprot[id.split('_')[0]] + '\n')
            else:
                out_file.write(line)

