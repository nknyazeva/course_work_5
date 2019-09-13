from os import listdir

gene_mm = 'MACMU00283'
gene_hs = 'HUMAN00253'

directory = '/home/nknyazeva/courseWork5/data/ortho_sorted/genes/bcftools/'
#directory = '/home/nknyazeva/courseWork5/data/ortho_sorted/genes/ortho_1/'
#directory = '/Users/anastasia/IdeaProjects/course_work_5/test_data/to_muscle/'
out_file = directory + 'all_' + gene_mm + '_' + gene_hs + '.fasta'

files_mm = listdir(directory + gene_mm)
files_hs = listdir(directory + gene_hs)


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

print('Done ' + str(out_file))

