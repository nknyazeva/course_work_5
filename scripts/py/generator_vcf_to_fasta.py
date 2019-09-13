# import sys
# import os

# dir_coord = '/Users/anastasia/IdeaProjects/course_work_5/test_data/test_coord/'
# dir_sh = '/Users/anastasia/IdeaProjects/course_work_5/test_data/test_vcf_to_fasta_sh/'

dir_coord = '/mnt/lustre/nknyazeva/courseWork5/data/result/coord/'

# dir_sh = '/mnt/lustre/nknyazeva/courseWork5/scripts/vcf_to_fasta_py/'
# DO NOT FORGET ABOUT HUMAN!!!!!!!!!!!!!!!!
# WE GENERATE SCRIPTS FOR MACACA ONLY TEMPORARLY!!!
dir_sh = '/mnt/lustre/nknyazeva/courseWork5/scripts/vcf_to_fasta_macaca/'


ref_macaca = '/home/nknyazeva/courseWork5/data/macaca_mulatta/reference/rheMac2.fa'
ref_human = '/home/nknyazeva/courseWork5/data/homo_sapiens/reference/hs37d5.fa'
refs = [ref_macaca, ref_human]

vcf_file_macaca = '/mnt/lustre/nknyazeva/courseWork5/data/macaca_mulatta/snp/133samples.clean.snps.filtered.removed.vcf.gz'
vcf_file_human = '/mnt/lustre/nknyazeva/courseWork5/data/homo_sapiens/snp_gz/ALL_wo_Y.chr.vcf.gz'
vcfs = [vcf_file_macaca, vcf_file_human]

haplotype_macaca = ['0A2', '0F6', '11414-01b', '11433-07b', '11433-08b', '17573', '18277', '19466', '1E3', '24898', '25P', '28499', '28500', '28507', '28518', '28535', '28555', '30119', '30136', '30158', '30423', '30424', '31505', '32510', '32538', '32754', '33674', '33707', '33V', '34597', '34600', '34602', '34762', '34770', '35044', '35045', '35046', '35048', '35049', '35051', '35055', '35059', '35060', '35061', '35082', '35086', '35087', '35088', '35089', '35090', '35091', '35095', '35096', '35144', '35150', '35154', '35160', '35162', '35250', '35252', '35253', '35254', '35256', '35259', '35490', '35496', '35502', '35717', '35718', '35722', '35724', '35728', '35730', '35732', '35864', '35865', '35866', '35868', '35871', '35872', '35873', '35874', '35875', '35876', '35883', '35895', '35902', '35907', '35916', '35919', '35921', '35923', '35957', '35969', '35972', '35975', '35976', '35990', '36013', '36332', '36355', '36357', '36359', '36371', '36374', '36389', '36390', '36394', '37730', '37732', '37733', '37734', '37735', '37738', '37739', '37740', '37741', '37742', '37745', '37746', '37854', '37945', '37950', '37N', '39345', '42T', '46N', '4D3', '5B2', '61R', '80S', '9C1', '9D4']
haplotype_human = ['HG03279', 'HG00242', 'NA20504', 'HG00614', 'HG02855', 'HG03607', 'HG01808', 'HG03479', 'NA19701', 'HG00475', 'HG01867', 'HG02035', 'HG02462', 'HG02281', 'HG03815', 'NA20891', 'HG01101', 'HG04131', 'HG02879', 'NA20585', 'HG03488', 'NA18629', 'NA18596', 'HG03123', 'HG01205', 'HG01060', 'HG03190', 'NA12762', 'HG02075', 'NA19026', 'HG01498', 'NA19317', 'HG01707', 'NA11843', 'NA20532', 'HG03202', 'HG01586', 'HG00274', 'NA20346', 'NA18574', 'HG03989', 'HG01168', 'NA18864', 'HG03875', 'HG00599', 'HG01965', 'HG03960', 'HG00743', 'HG01048', 'HG02090', 'HG02675', 'HG03945', 'NA18516', 'HG02337', 'NA19401', 'HG02772', 'HG01694', 'NA19007', 'HG02088', 'HG04225', 'HG01303', 'HG00553', 'NA18606', 'HG01855', 'NA20503', 'HG02687', 'HG02603', 'HG01932', 'HG03752', 'NA19117', 'HG00257', 'HG04106', 'NA20854', 'HG03706', 'HG03247', 'HG02793', 'NA19316', 'HG02922', 'HG01170', 'NA19430', 'NA20807', 'NA20289', 'HG01997', 'NA20299', 'NA19160', 'NA18626', 'HG00182', 'NA18530', 'NA12156', 'HG00112', 'HG01845', 'HG00143', 'HG02840', 'HG02497', 'NA20339', 'HG02562', 'HG01785', 'NA18941', 'HG01089', 'HG02541', 'HG02009', 'HG02144', 'HG00103', 'NA18917', 'HG03767', 'NA20543', 'HG03998', 'NA18511', 'HG03974', 'NA18635', 'HG03634', 'HG03342', 'NA21115', 'HG03270', 'HG01610', 'HG00150', 'HG01794', 'HG01519', 'NA18757', 'HG03867', 'HG00353', 'HG01933', 'NA19091', 'HG03388', 'HG00445', 'NA20853', 'NA19984', 'HG00620', 'NA19819', 'NA18877']
haplotypes = [haplotype_macaca, haplotype_human]


def getFileName(ids, org):
    result = ''

    result = result + '/mnt/lustre/nknyazeva/courseWork5/data/result/genes/ortho_'
    result = result + ids[0]
    result = result + '_'
    result = result + ids[1]
    result = result + '/'
    result = result + ids[org]

    if org == 0:
        result = result + '/consensus_macaca_'
    else:
        result = result + '/consensus_homo_'
    result = result + ids[org]
    result = result + '_'
    result = result + '" + str(id) +"'
    result = result + '.fasta'

    #["cmd1", "name_part1" + id + ".fasta", "cmd2"]

    return result

def getCommandSamtools(refs, coords, org, ids):

    result = ''

    result = result + '\t\t'
    result = result + 'samtools_cmd = ['
    result = result + '"samtools", '
    result = result + '"faidx", '
    result = result + '"' +refs[org] + '", '
    result = result + '"' +coords[org] + '"]' # samtools_cmd = ["samtools", "faidx", "/home/nknyazeva/courseWork5/data/macaca_mulatta/reference/rheMac2.fa", "chr1:169171018-169215524"]

    return result

def getCommandBcftools(refs, coords, org, ids):

    result = ''

    result = result + '\t\t'
    result = result + 'bcftools_cmd = ['
    result = result + '"/home/nknyazeva/tools/bcftools-1.9/bin/bcftools", '
    result = result + '"consensus", '
    result = result + '"-s", '
    result = result + 'str(id), '
    result = result + '"' + vcfs[org] + '"'

    result = result + ']' # bcftools_cmd = ["/home/nknyazeva/tools/bcftools-1.9/bin/bcftools", "consensus", "-s", str(id), "/mnt/lustre/nknyazeva/courseWork5/data/macaca_mulatta/snp/133samples.clean.snps.filtered.removed.vcf.gz"]

    return result


# for i in range(3):
for i in range(71):
    i = str(i)
    if len(i) < 2:
        i = '0' + i
    name_file_in = dir_coord + 'ortho_coordinates_100.' + i
    name_file_out = dir_sh + 'vcf_to_fasta.' + i + '.py'

    file_out = open(name_file_out, 'w')

    result_code = ''

   
    result_code = result_code + 'import subprocess' + '\n'

    file_in = open(name_file_in, 'r')

    for line in file_in:
        line = line.strip().split()

        id_macaca = line[0]
        id_human = line[2]
        ids = [id_macaca, id_human]

        coord_macaca = line[1]
        coord_human = line[3]
        coords = [coord_macaca, coord_human]

        # DO NOT FORGET ABOUT HUMAN!
        # BECAUSE OF MISTAKE WE ONLY REGENERATE MACACA SCRIPTS
        # !!!!!!!!!!!!!!!!!!!!!!!!!
        #for org in range(2):
        for org in range(1):


            result_code = result_code + 'for id in ' + str(haplotypes[org]) + ':' + '\n'

            result_code = result_code + '\ttry:' + '\n'

            result_code = result_code + getCommandSamtools(refs, coords, org, ids,) + '\n'

            result_code = result_code + '\t\tfile = open("' + getFileName(ids, org) + '", "w")' + '\n'

            result_code = result_code + getCommandBcftools(refs, coords, org, ids,) + '\n'
            
            result_code = result_code + '\t\tsamtools_process = subprocess.Popen(samtools_cmd, stdout=subprocess.PIPE)' + '\n'

            result_code = result_code + '\t\tprocess = subprocess.Popen(bcftools_cmd, stdin=samtools_process.stdout, stdout=file, stderr=subprocess.PIPE)' + '\n'

            result_code = result_code + '\t\tout, err = process.communicate()' + '\n'

            result_code = result_code + '\t\tif len(err) != 0:' + '\n'

            result_code = result_code + '\t\t\traise Exception(err)' + '\n'

            result_code = result_code + '' + '\n'


            # result_code = result_code + '\t\toutput = subprocess.check_output(bcftools_cmd, stdin=samtools_process.stdout)' + '\n'

            # result_code = result_code + '\t\tsamtools_process.wait()' + '\n'

            result_code = result_code + '\texcept Exception as e:' + '\n'

            filename = getFileName(ids, org)

            result_code = result_code + '\t\tprint("VCF_TO_FASTA_ERROR: '+filename+'")' + '\n'

            result_code = result_code + '\t\tprint("ERROR_MESSAGE:")' + '\n'

            result_code = result_code + '\t\tprint(e)' + '\n' + '\n'
    

    file_out.write(result_code)

    file_in.close()
    file_out.close()



