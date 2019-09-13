import sys

file_in = sys.argv[1]
path = file_in.split('/')
dir = path[:-1]
name = path[-1].split('_')
name_out = []
name_out.append('shared')
name_out.append('snp')
name_out.append(name[1])
name_out.append(name[2] + '.txt')
name_out = '_'.join(name_out)
dir.append(name_out)

file_out = '/'.join(dir)


def read_file(name_file):
    file = open(name_file, 'r')
    seq_macaca = {}
    seq_human = {}

    processing = True
    active_genotype = 'macaca'

    while processing:
        line = file.readline()

        if len(line) == 0:
            processing = False

        if processing:
            if line[0] == '>':

                id = line.strip()

                if 'HUMAN' in line:
                    active_genotype = 'human'
                    seq_human[id] = ''
                    line = file.readline()
                else:
                    active_genotype = 'macaca'
                    seq_macaca[id] = ''
                    line = file.readline()

            if active_genotype == 'macaca':
                seq_macaca[id] = seq_macaca[id] + line.strip()
            if active_genotype == 'human':
                seq_human[id] = seq_human[id] + line.strip()
    file.close()
    return seq_macaca, seq_human


def uppercase(matrix):
    for key in matrix:
        matrix[key] = matrix[key].upper()
    return matrix


def transpose_seq(seq_org):
    matrix = []
    for key in seq_org:
        matrix.append(list(seq_org[key]))
    matrix = zip(*matrix)
    return matrix


def search_snp_columns(transp_org):
    interesting_columns = []
    for i in range(len(transp_org)):
        column = transp_org[i]
        uniq_key = list(set(column))
        if len(uniq_key) > 1:
            interesting_columns.append(i)
    return interesting_columns



seq_macaca, seq_human = read_file(file_in)

seq_macaca = uppercase(seq_macaca)
seq_human = uppercase(seq_human)

transp_macaca = transpose_seq(seq_macaca)
transp_human = transpose_seq(seq_human)

columns_macaca = search_snp_columns(transp_macaca)
columns_human = search_snp_columns(transp_human)

snp = {}
for i in columns_macaca:
    if i in columns_human:
        positions_macaca = list(set(transp_macaca[i]))
        positions_human = list(set(transp_human[i]))
        counter = 0
        for nucl in positions_macaca:
            if nucl != '-':
                if nucl in positions_human:
                    counter = counter + 1
        if counter > 1:
            snp[i] = [positions_macaca, positions_human]

out_file = open(file_out, 'w')
for i in snp:
    out_file.write(str(i) + '\t' + str(snp[i]) + '\n')
out_file.close()




















