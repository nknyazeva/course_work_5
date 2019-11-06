import subprocess

for i in range(0, 71):
    if len(str(i)) < 2:
        str_i = '0' + str(i)
    else:
        str_i = str(i)
    name_file = '/mnt/lustre/nknyazeva/courseWork5/scripts/vcf_to_fasta_GRCh38/start_sh/vcf_to_fasta.%s.sh' % str_i

    parameters = ['qsub', str(name_file)]
    subprocess.call(parameters)

