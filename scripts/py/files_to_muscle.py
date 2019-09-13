from os import listdir
import sys

name_file = sys.argv[1]

file_in = open(name_file, 'r')
for line in file_in:
    line = line.strip().split()

    gene_mm = line[0]
    gene_hs = line[2]

    directory = '/home/nknyazeva/courseWork5/data/result/genes/ortho_%s_%s/' % (gene_mm, gene_hs)

    #directory = '/home/nknyazeva/courseWork5/data/ortho_sorted/genes/ortho_1/'
    #directory = '/Users/anastasia/IdeaProjects/course_work_5/test_data/to_muscle/'
    out_file = directory + 'all_' + gene_mm + '_' + gene_hs + '.fasta'

    files_mm = listdir(directory + gene_mm)
    files_hs = listdir(directory + gene_hs)

    try:
        file_out = open(out_file, "w")

        for file in files_mm:
            file_in = open(directory + gene_mm + '/' + file, "r")
            for line in file_in:
                if line[0] == '>':
                    id = file[17:][:-6]
                    file_out.write(line.strip() + '|' + id + '\n')
                else:
                    file_out.write(line)
            file_in.close()

        for file in files_hs:
            file_in = open(directory + gene_hs + '/' + file, "r")
            for line in file_in:
                if line[0] == '>':
                    id = file[15:][:-6]
                    file_out.write(line.strip() + '|' + id + '\n')
                else:
                    file_out.write(line)
            file_in.close()

        file_out.close()

    except Exception as e:
        print('ERROR in ' + str(out_file))
        print("ERROR_MESSAGE:")
        print(e)


