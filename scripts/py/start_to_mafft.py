import subprocess

# for i in range(0, 71):
for i in range(0, 20):
    if len(str(i)) < 2:
        str_i = '0' + str(i)
    else:
        str_i = str(i)
    for j in range(10):
        str_j = str(j)
        name_file = '/mnt/lustre/nknyazeva/courseWork5/scripts/to_mafft_GRCh38/by_10/mafft_%s_%s.sh' % (str_i, str_j)

        parameters = ['qsub', str(name_file)]
        print('parameters %s' % parameters)
        subprocess.call(parameters)

