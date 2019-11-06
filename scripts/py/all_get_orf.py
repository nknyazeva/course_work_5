# in_file = '/mnt/lustre/nknyazeva/courseWork5/data/result/genes_GRCh38/ortho_MACMU18455_HUMAN23250/MACMU18455.fasta'
# new_coords = 'join(complement(164891789..164891918), complement(164891367..164891599), complement(164890725..164890850), complement(164889885..164889941), complement(164888928..164889042), complement(164888707..164888741), complement(164888441..164888521), complement(164886998..164887121), complement(164886747..164886867), complement(164885859..164885956), complement(164885524..164885629), complement(164885388..164885430), complement(164884597..164884696), complement(164883960..164884012), complement(164883496..164883552))'
#  out_file = '/mnt/lustre/nknyazeva/courseWork5/data/result/genes_GRCh38/ortho_MACMU18455_HUMAN23250/orf_MACMU18455.fasta'

name_file_in = '/home/nknyazeva/courseWork5/data/result/oma_id_pair_coordinates.sql'


def readfile(in_file):
    file_in = open(in_file, 'r')
    seq = {}
    processing = True
    while processing:
        line = file_in.readline()
        if len(line) == 0:
            processing = False
            break
        if line[0] == '>':
            id = line.strip()
            seq[id] = ''
            line = file_in.readline()
        seq[id] = seq[id] + line.strip()
    file_in.close()
    return seq

def write_file(out_file, dct):
    file_out = open(out_file, 'w')
    for key in dct:
        file_out.write(key + '\n')
        file_out.write(dct[key] + '\n')
    file_out.close()

def getFileName(ids, org):
    result = ''

    result = result + '/mnt/lustre/nknyazeva/courseWork5/data/result/genes_GRCh38/ortho_'
    result = result + ids[0]
    result = result + '_'
    result = result + ids[1]
    result = result + '/'
    result = result + org
    result = result + '.fasta'

    return result

def getOutFileName(ids, org):
    result = ''

    result = result + '/mnt/lustre/nknyazeva/courseWork5/data/result/genes_GRCh38/ortho_'
    result = result + ids[0]
    result = result + '_'
    result = result + ids[1]
    result = result + '/orf_'
    result = result + org
    result = result + '.fasta'

    return result

list_file_name = []

with open(name_file_in, 'r') as file_in:

    for line in file_in:
        line = line.strip().split()
        if len(line) != 0:

            id_macaca = line[0]
            id_human = line[3]
            ids = [id_macaca, id_human]

            coord_macaca = line[2]
            coord_human = line[5]

            coords = [coord_macaca, coord_human]

            for i in range(len(ids)):
                org = ids[i]
                org_coords = coords[i]

                if org_coords.find('join') == 0:
                    if org_coords.find('complement') == -1:
                        coords_int = []
                        org_coords = org_coords[5:-1]
                        org_coords = org_coords.split(',')
                        for coord in org_coords:
                            c = coord.split('..')
                            c = map(int, c)
                            coords_int.append(c)

                        init = coords_int[0][0]
                        for i in range(len(coords_int)):
                            for j in range(2):
                                coords_int[i][j] = coords_int[i][j] - init
                    else:
                        coords_int = []
                        # org_coords = org_coords[5:-1]
                        # org_coords = org_coords.split(',')
                        # for coord in org_coords:
                        #     coord = coord[12:-1]
                        #     c = coord.split('..')
                        #     c = map(int, c)
                        #     coords_int.append(c)
                        #
                        # coords_int.reverse()
                        # init = coords_int[0][0]
                        # for i in range(len(coords_int)):
                        #     for j in range(2):
                        #         coords_int[i][j] = coords_int[i][j] - init
                        coords_int = None
                else:
                    if org_coords.find('complement') == -1:
                        coords_int = []
                        coord = org_coords
                        c = coord.split('..')
                        c = map(int, c)
                        coords_int.append(c)

                        init = coords_int[0][0]
                        for i in range(len(coords_int)):
                            for j in range(2):
                                coords_int[i][j] = coords_int[i][j] - init
                    else:
                        coords_int = []
                        coord = org_coords[11:-1]
                        c = coord.split('..')
                        c = map(int, c)
                        coords_int.append(c)

                        init = coords_int[0][0]
                        for i in range(len(coords_int)):
                            for j in range(2):
                                coords_int[i][j] = coords_int[i][j] - init

                if coords_int != None:
                    list_file_name.append(getOutFileName(ids, org))

                    # seq = readfile(getFileName(ids, org))
                    #
                    # coding_seq = {}
                    # for id in seq:
                    #     line = ''
                    #     for i in coords_int:
                    #         line = line + seq[id][i[0]:i[1] + 1]
                    #     coding_seq[id] = line
                    #
                    # write_file(getOutFileName(ids, org), coding_seq)

out_file = '/home/nknyazeva/courseWork5/data/result/pn_ps_file_name.txt'
f_out = open(out_file, 'w')
for i in list_file_name:
    f_out.write(i + '\n')
f_out.close()
