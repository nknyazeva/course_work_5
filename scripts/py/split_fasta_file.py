file_in = '/mnt/lustre/nknyazeva/courseWork5/data/result/genes_GRCh38/ortho_MACMU18455_HUMAN23250/all_MACMU18455_HUMAN23250.fasta'
file_out_macaca = '/mnt/lustre/nknyazeva/courseWork5/data/result/genes_GRCh38/ortho_MACMU18455_HUMAN23250/MACMU18455.fasta'
file_out_human = '/mnt/lustre/nknyazeva/courseWork5/data/result/genes_GRCh38/ortho_MACMU18455_HUMAN23250/HUMAN23250.fasta'


# file_in = '/mnt/lustre/nknyazeva/courseWork5/data/result/genes/ortho_MACMU06520_HUMAN17503/all_MACMU06520_HUMAN17503.fasta'
# file_out_macaca = '/mnt/lustre/nknyazeva/courseWork5/data/result/genes/ortho_MACMU06520_HUMAN17503/MACMU06520.fasta'
# file_out_human = '/mnt/lustre/nknyazeva/courseWork5/data/result/genes/ortho_MACMU06520_HUMAN17503/HUMAN17503.fasta'

in_file = open(file_in, 'r')

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

file_out_macaca = open(file_out_macaca, 'w')
for key in seq_macaca.keys():
    file_out_macaca.write(key + '\n')
    file_out_macaca.write(seq_macaca[key] + '\n')
file_out_macaca.close()

file_out_human = open(file_out_human, 'w')
for key in seq_human.keys():
    file_out_human.write(key + '\n')
    file_out_human.write(seq_human[key] + '\n')
file_out_human.close()

