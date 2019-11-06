name_file_in = '/home/nknyazeva/courseWork5/data/result/test.txt'
name_file_out = '/home/nknyazeva/courseWork5/data/result/gff_ortho_coord.txt'

with open(name_file_in, 'r') as file_in:
    with open(name_file_out, 'w') as file_out:
        for line in file_in:
            line = line.strip().split('   ')
            print line
            string_one = eval(line[1])
            string_second = eval(line[3])

            chr_one = 'chr' + string_one[0]
            chr_second = 'chr' + string_second[0]
            print line[1]
            start_one = string_one[2][0]
            end_one = string_one[-1][1]
            start_second = string_second[2][0]
            end_second = string_second[-1][1]
            coord_one = chr_one + ':' + start_one + '-' + end_one
            coord_second = chr_second + ':' + start_second + '-' + end_second
            file_out.write(line[0] + '\t' + coord_one + '\t' + line[2] + '\t' + coord_second + '\n')
