in_file = '/mnt/lustre/nknyazeva/courseWork5/data/homo_sapiens_GRCh38/reference/GRCh38_full_analysis_set_plus_decoy_hla.fa'
out_file = '/mnt/lustre/nknyazeva/courseWork5/data/homo_sapiens_GRCh38/reference/GRCh38.fa'

file_in = open(in_file, 'r')
file_out = open(out_file, 'w')
for line in file_in:
    if line[:4] == '>chr':
        result = '>' + line[4:]
    else:
        result = line
    file_out.write(result)

file_in.close()
file_out.close()


