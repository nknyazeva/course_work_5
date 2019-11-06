in_file = '/mnt/lustre/nknyazeva/courseWork5/data/result/genes_GRCh38/ortho_MACMU18455_HUMAN23250/MACMU18455.fasta'
coords = '34606041..34606108, 34610816..34611002, 34615547..34615670, 34628717..34628893, 34630249..34630363, 34632693..34632870, 34634807..34634915, 34647068..34647201'
out_file = '/mnt/lustre/nknyazeva/courseWork5/data/result/genes_GRCh38/ortho_MACMU18455_HUMAN23250/orf_MACMU18455.fasta'

# in_file = '/mnt/lustre/nknyazeva/courseWork5/data/result/genes/ortho_MACMU06520_HUMAN17503/HUMAN17503.fasta'
# coords =  '111898736..111898796, 111929120..111929540, 111944960..111945060, 111947394..111947567, 111965191..111965277, 111968137..111968252, 111975289..111975472, 111982842..111982993, 111994251..111994404, 111997323..111997476, 112001201..112001286, 112003092..112003187, 112003904..112003984, 112008383..112008475, 112009948..112010066, 112019413..112019522, 112021422..112021581, 112022258..112022394, 112028351..112028864'
# out_file = '/mnt/lustre/nknyazeva/courseWork5/data/result/genes/ortho_MACMU06520_HUMAN17503/orf_HUMAN17503.fasta'

def readfile(in_file):
    file_in = open(in_file, 'r')
    seq = {}
    processing = True
    while processing:
        line = file_in.readline()
        if len(line) == 0:
            processing = False
            break
        if line[0] == '>':
            id = line.strip()
            seq[id] = ''
            line = file_in.readline()
        seq[id] = seq[id] + line.strip()
    file_in.close()
    return seq

def write_file(out_file, dct):
    file_out = open(out_file, 'w')
    for key in dct:
        file_out.write(key + '\n')
        file_out.write(dct[key] + '\n')
    file_out.close()


coords = coords.split(', ')
coords_int = []
for coord in coords:
    c = coord.split('..')
    c = map(int, c)
    coords_int.append(c)


init = coords_int[0][0]
for i in range(len(coords_int)):
    for j in range(2):
        coords_int[i][j] = coords_int[i][j] - init


seq = readfile(in_file)

coding_seq = {}
for id in seq:
    line = ''
    for i in coords_int:
        line = line + seq[id][i[0]:i[1] + 1]
    coding_seq[id] = line

write_file(out_file, coding_seq)
