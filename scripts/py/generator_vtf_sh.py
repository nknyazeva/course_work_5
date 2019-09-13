

dir_sh = '/mnt/lustre/nknyazeva/courseWork5/scripts/vcf_to_fasta_py/start_sh/'
# dir_sh = '/mnt/lustre/nknyazeva/courseWork5/scripts/vcf_to_fasta_macaca/start_sh/'

for i in range(71):
    i = str(i)
    if len(i) < 2:
        i = '0' + i
    name_file_out = dir_sh + 'vcf_to_fasta.' + i + '.sh'

    file_out = open(name_file_out, 'w')

    result_code = ''

    result_code = result_code + '#!/bin/bash' + '\n'
    result_code = result_code + '#PBS -l walltime=100:00:00' + '\n'
    result_code = result_code + '#PBS -d .' + '\n' + '\n'
    result_code = result_code + 'python /mnt/lustre/nknyazeva/courseWork5/scripts/vcf_to_fasta_py/vcf_to_fasta.' + i + '.py'
    # result_code = result_code + 'python /mnt/lustre/nknyazeva/courseWork5/scripts/vcf_to_fasta_macaca/vcf_to_fasta.' + i + '.py'
    file_out.write(result_code)
    file_out.close()

