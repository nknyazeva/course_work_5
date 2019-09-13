# import sys
# import os

# dir_coord = '/Users/anastasia/IdeaProjects/course_work_5/test_data/test_coord/'
# dir_sh = '/Users/anastasia/IdeaProjects/course_work_5/test_data/test_vcf_to_fasta_sh/'

dir_coord = '/mnt/lustre/nknyazeva/courseWork5/data/result/coord/'
dir_sh = '/mnt/lustre/nknyazeva/courseWork5/scripts/to_muscle_sh/'


def getFileNameIn(ids):
    result = ''

    result = result + '/mnt/lustre/nknyazeva/courseWork5/data/result/genes/ortho_'
    result = result + ids[0]
    result = result + '_'
    result = result + ids[1]
    result = result + '/'
    result = result + 'all_'
    result = result + ids[0]
    result = result + '_'
    result = result + ids[1]
    result = result + '.fasta'

    #["cmd1", "name_part1" + id + ".fasta", "cmd2"]

    return result

def getFileNameOut(ids):
    result = ''

    result = result + '/mnt/lustre/nknyazeva/courseWork5/data/result/genes/ortho_'
    result = result + ids[0]
    result = result + '_'
    result = result + ids[1]
    result = result + '/'
    result = result + 'all_'
    result = result + ids[0]
    result = result + '_'
    result = result + ids[1]
    result = result + '_align.afa'

    return result


for i in range(71):
    i = str(i)
    if len(i) < 2:
        i = '0' + i
    name_file_in = dir_coord + 'ortho_coordinates_100.' + i
    name_file_out = dir_sh + 'to_muscle.' + i + '.sh'

    file_out = open(name_file_out, 'w')

    result_code = ''

    result_code = result_code + '#!/bin/bash' + '\n'
    result_code = result_code + '#PBS -l walltime=100:00:00' + '\n'
    result_code = result_code + '#PBS -d .' + '\n'
    result_code = result_code + '\n'

    file_in = open(name_file_in, 'r')

    for line in file_in:
        line = line.strip().split()

        id_macaca = line[0]
        id_human = line[2]
        ids = [id_macaca, id_human]

        result_code = result_code + 'muscle -in '
        result_code = result_code + getFileNameIn(ids)
        result_code = result_code + ' -out '
        result_code = result_code + getFileNameOut(ids)
        result_code = result_code + ' -maxiters 1 -diags' + '\n' + '\n'

    file_out.write(result_code)

    file_in.close()
    file_out.close()



