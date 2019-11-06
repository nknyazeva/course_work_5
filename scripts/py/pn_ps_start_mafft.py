import subprocess

# for i in range(0, 75):
for i in range(20, 75):
    if len(str(i)) < 2:
        str_i = '0' + str(i)
    else:
        str_i = str(i)

    name_file = '/home/nknyazeva/courseWork5/scripts/pn_ps_mafft/mafft_100.%s.sh' % str_i

    parameters = ['qsub', str(name_file)]
    print('parameters %s' % parameters)
    subprocess.call(parameters)

