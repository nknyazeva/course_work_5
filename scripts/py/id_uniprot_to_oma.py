in_file_oma_uniprot = "/home/nknyazeva/courseWork5/data/oma/oma-uniprot.txt"
in_file_ortho = "/home/nknyazeva/courseWork5/data/macaca_mulatta/ortho_HSapiens_Mmulatta/common_ortho_H.sapiens-M.mulatta.sql"
in_file_annotations = "/home/nknyazeva/courseWork5/data/oma/oma-uniprot.txt/oma-protein-annotations.txt"

# out_file = "/home/nknyazeva/courseWork5/data/macaca_mulatta/ortho_HSapiens_Mmulatta/oma_id_ortho_coordinates.txt"
out_file = "/home/nknyazeva/courseWork5/data/macaca_mulatta/ortho_HSapiens_Mmulatta/oma_id_ortho.txt"


f = open(in_file_oma_uniprot, "r")
oma_uniprot = {}
for line in f:
    if line[0] != '#':
        line = line.strip().split('\t')
        oma_uniprot[line[1]] = line[0]
f.close()

file_write = open(out_file, "w")

f_ortho = open(in_file_ortho, "r")
for line in f_ortho:
    line = line.strip().split('\t')
    oma_id_macaca = line[6]
    uni_id_homo = line[5]
    if uni_id_homo in oma_uniprot.keys():
        oma_id_homo = oma_uniprot[uni_id_homo]
        file_write.write(oma_id_macaca + '\t' + oma_id_homo + '\n')

f_ortho.close()
file_write.close()

