name_gff_file = '/home/nknyazeva/courseWork5/data/homo_sapiens_GRCh38/gff/Homo_sapiens.GRCh38.87.gff3'
name_id_file = '/home/nknyazeva/courseWork5/data/result/extra_extra_extra_id_human.txt'
out_file = '/home/nknyazeva/courseWork5/data/result/oma_exon_coordinates_human_extra_extra.txt'

# name_gff_file = '/home/nknyazeva/courseWork5/data/homo_sapiens_GRCh38/gff/Homo_sapiens.GRCh38.98.gff3'
# name_id_file = '/home/nknyazeva/courseWork5/data/result/oma_ensembl_id_human.txt'
# out_file = '/home/nknyazeva/courseWork5/data/result/oma_exon_coordinates_human.txt'

dict_id_exones = {}
with open(name_id_file, 'r') as id_file:
    for line in id_file:
        oma_id = line.strip().split()[1]
        id = line.strip().split('.')[0]
        with open(name_gff_file, 'r') as gff_file:
            for line_gff in gff_file:
                if id in line_gff:
                    if 'exon' in line_gff:
                        line_gff = line_gff.strip().split()
                        coords = [line_gff[3], line_gff[4]]
                        if oma_id in dict_id_exones:
                            dict_id_exones[oma_id].append(coords)
                        else:
                            dict_id_exones[oma_id] = [line_gff[0], line_gff[6], coords]


with open(out_file, 'w') as file_out:
    for id in dict_id_exones:
        file_out.write(id + '\t' + str(dict_id_exones[id]) + '\n')
