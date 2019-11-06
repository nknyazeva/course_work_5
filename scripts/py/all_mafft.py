in_dir = '/home/nknyazeva/courseWork5/data/result/pn_ps/'

out_dir = '/home/nknyazeva/courseWork5/scripts/pn_ps_mafft/'
def getPutFileName(name):
    name = name[:-6]
    name = name + '_align_mafft.afa'
    return name

for i in range(75):
    i = str(i)
    if len(i) < 2:
        i = '0' + i
    name_file_in = in_dir + 'pn_ps_file_name_100.' + i 
    name_file_out = out_dir + 'mafft_100.' + i + '.sh'
    with open(name_file_in, 'r')as file_in:
        with open(name_file_out, 'w') as file_out:
            file_out.write('#!/bin/bash\n#PBS -l walltime=100:00:00\n#PBS -d .\n')
            for line in file_in:
                name_out_file = getPutFileName(line.strip())
                file_out.write('mafft %s > %s \n \n' % (line.strip(), name_out_file))






