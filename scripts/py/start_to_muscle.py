import subprocess


script = '/mnt/lustre/nknyazeva/courseWork5/scripts/py/files_to_muscle.py'
dir_coord = '/mnt/lustre/nknyazeva/courseWork5/data/result/coord/'


for i in range(71):
    i = str(i)
    if len(i) < 2:
        i = '0' + i
    name_file = dir_coord + 'ortho_coordinates_100.' + i
    subprocess.call(["python", script, name_file])
