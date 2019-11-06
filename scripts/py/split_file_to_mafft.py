for i in range(0, 71):
    if len(str(i)) < 2:
        i = '0' + str(i)
    else:
        i = str(i)
    in_file  = '/mnt/lustre/nknyazeva/courseWork5/scripts/to_mafft_GRCh38/to_muscle.%s.sh' % i
    print(in_file)

    out_dir = '/mnt/lustre/nknyazeva/courseWork5/scripts/to_mafft_GRCh38/by_10/'

    def split_list(alist, wanted_parts=1):
        length = len(alist)
        return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts]
                 for i in range(wanted_parts) ]

    file = open(in_file, 'r')

    list_line = []
    for line in file:
        if line[0] == 'm':
            list_line.append(line)

    split_list = split_list(list_line, wanted_parts=10)

    for i in range(len(split_list)):
        name_out_file = out_dir + 'mafft_' + in_file.split('.')[1] + '_' + str(i) + '.sh'
        file_out = open(name_out_file, 'w')
        result = ''
        result = result + '#!/bin/bash\n#PBS -l walltime=1000:00:00\n#PBS -d .\n\n'
        lines = '\n'.join(split_list[i])
        result = result + lines
        file_out.write(result)
        file_out.close()

    file.close()

