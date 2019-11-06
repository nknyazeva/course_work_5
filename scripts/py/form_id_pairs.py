coord_macaca_file = '/home/nknyazeva/courseWork5/data/result/oma_exon_coordinates_macaca.txt'
coord_human_file = '/home/nknyazeva/courseWork5/data/result/oma_exon_coordinates_human.txt'
id_pairs_file = '/home/nknyazeva/courseWork5/data/result/ortho_pairs.txt'
out_file = '/home/nknyazeva/courseWork5/data/result/ortho_pairs_coordinates.txt'


dict_coord_human = {}
with open(coord_human_file, 'r') as coord_human:
    for line in coord_human:
        line = line.strip()
        dict_coord_human[line.split()[0]] = line[11:]

dict_coord_macaca = {}
with open(coord_macaca_file, 'r') as coord_macaca:
    for line in coord_macaca:
        line = line.strip()
        dict_coord_macaca[line.split()[0]] = line[11:]
        
with open(id_pairs_file, 'r') as id_pairs:
    with open(out_file, 'w') as out_file:
        for line in id_pairs:
            line = line.strip()
            human_id = line.split()[0]
            macaca_id = line.split()[1]
            out_file.write(human_id + '\t')
            out_file.write(dict_coord_human[human_id] + '\t')
            out_file.write(macaca_id + '\t')
            out_file.write(dict_coord_macaca[macaca_id] + '\n')
