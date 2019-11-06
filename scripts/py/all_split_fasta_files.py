# file_in = '/mnt/lustre/nknyazeva/courseWork5/data/result/genes_GRCh38/ortho_MACMU18455_HUMAN23250/all_MACMU18455_HUMAN23250.fasta'
# file_out_macaca = '/mnt/lustre/nknyazeva/courseWork5/data/result/genes_GRCh38/ortho_MACMU18455_HUMAN23250/MACMU18455.fasta'
# file_out_human = '/mnt/lustre/nknyazeva/courseWork5/data/result/genes_GRCh38/ortho_MACMU18455_HUMAN23250/HUMAN23250.fasta'

name_file_in = '/home/nknyazeva/courseWork5/data/result/coord/ortho_coordinates.sql'


def getFileName(ids):
    result = ''

    result = result + '/mnt/lustre/nknyazeva/courseWork5/data/result/genes_GRCh38/ortho_'
    result = result + ids[0]
    result = result + '_'
    result = result + ids[1]
    result = result + '/'
    result = result + 'all_'
    result = result + ids[0]
    result = result + '_'
    result = result + ids[1]
    result = result + '.fasta'

    return result

def getOutFileName(ids, org):
    result = ''

    result = result + '/mnt/lustre/nknyazeva/courseWork5/data/result/genes_GRCh38/ortho_'
    result = result + ids[0]
    result = result + '_'
    result = result + ids[1]
    result = result + '/'
    result = result + org
    result = result + '.fasta'

    return result


with open(name_file_in, 'r') as file_in:

    for line in file_in:
        line = line.strip().split()
        print(line)
        if len(line) != 0:

            id_macaca = line[0]
            id_human = line[2]
            ids = [id_macaca, id_human]
            in_file = open(getFileName(ids), 'r')

            seq_macaca = {}
            seq_human = {}

            processing = True
            active_genotype = 'macaca'

            while processing:
                line = in_file.readline()

                if len(line) == 0:
                    processing = False

                if processing:
                    if line[0] == '>':

                        id = line.strip()

                        if 'HUMAN' in line:
                            active_genotype = 'human'
                            seq_human[id] = ''
                            line = in_file.readline()
                        else:
                            active_genotype = 'macaca'
                            seq_macaca[id] = ''
                            line = in_file.readline()

                    if active_genotype == 'macaca':
                        seq_macaca[id] = seq_macaca[id] + line.strip()
                    if active_genotype == 'human':
                        seq_human[id] = seq_human[id] + line.strip()
            in_file.close()

            file_out_macaca = open(getOutFileName(ids, ids[0]), 'w')
            for key in seq_macaca.keys():
                file_out_macaca.write(key + '\n')
                file_out_macaca.write(seq_macaca[key] + '\n')
            file_out_macaca.close()

            file_out_human = open(getOutFileName(ids, ids[1]), 'w')
            for key in seq_human.keys():
                file_out_human.write(key + '\n')
                file_out_human.write(seq_human[key] + '\n')
            file_out_human.close()

