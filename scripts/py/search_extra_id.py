# # ids_only_file = '/home/nknyazeva/courseWork5/data/result/oma_ensembl_id_human.txt'
# # ids_with_coords_file = '/home/nknyazeva/courseWork5/data/result/oma_exon_coordinates_human.txt'
# # name_out_file = '/home/nknyazeva/courseWork5/data/result/new_extra_id_human.txt'
#
# ids_only_file = '/home/nknyazeva/courseWork5/data/result/oma_ensembl_id_macaca.txt'
# ids_with_coords_file = '/home/nknyazeva/courseWork5/data/result/oma_exon_coordinates_macaca.txt'
# name_out_file = '/home/nknyazeva/courseWork5/data/result/new_extra_id_macaca.txt'
#
# result = []
# with open(ids_only_file, 'r') as ids_only:
#     with open(ids_with_coords_file, 'r') as ids_with_coords:
#
#         lines_with_coords = ids_with_coords.read().splitlines()
#         lines_ids_only = ids_only.read().splitlines()
#
#         for line_id_only in lines_ids_only:
#             count = 0
#             for line_with_coord in lines_with_coords:
#
#                 id = line_id_only.split()[1]
#
#                 if id in line_with_coord:
#                     count = 1
#
#             if count == 0:
#                 result.append(line_id_only)
#
# print 'u'
# print result
# # with open(name_out_file, 'w') as output:
# #     for item in result:
# #         output.write(item + '\n')


ids_only_file = '/home/nknyazeva/courseWork5/data/result/oma_ensembl_id_human.txt'
ids_with_coords_file = '/home/nknyazeva/courseWork5/data/result/oma_exon_coordinates_human.txt'
name_out_file = '/home/nknyazeva/courseWork5/data/result/new_extra_id_human.txt'

# ids_only_file = '/home/nknyazeva/courseWork5/data/result/oma_ensembl_id_macaca.txt'
# ids_with_coords_file = '/home/nknyazeva/courseWork5/data/result/oma_exon_coordinates_macaca.txt'
# name_out_file = '/home/nknyazeva/courseWork5/data/result/new_extra_id_macaca.txt'

result = []
with open(ids_only_file, 'r') as ids_only:

    lines_ids_only = ids_only.read().splitlines()

    for line_id_only in lines_ids_only:
        id = line_id_only.split()[1]

        count = 0

        for line_id_only2 in lines_ids_only:

            id2  = line_id_only2.split()[1]

            if id == id2:

                count = count + 1

        if count > 1:
            result.append(line_id_only)






# with open(ids_with_coords_file, 'r') as ids_with_coords:
#
#     lines_with_coords = ids_with_coords.read().splitlines()
#
#     for line_with_coord in lines_with_coords:
#


print 'u'
print result
# with open(name_out_file, 'w') as output:
#     for item in result:
#         output.write(item + '\n')
