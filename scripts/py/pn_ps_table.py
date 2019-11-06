import pandas as pd
in_file = '/Users/anastasia/IdeaProjects/course_work_5/test_data/all_pn_ps_table.txt'

data = pd.read_table(in_file, names=["id", "pn", "ps"])

data_human = pd.DataFrame(columns=["id", "pn", "ps"])
data_macaca = pd.DataFrame(columns=["id", "pn", "ps"])

for id in data.id:
    if 'HUMAN' in id:
        data_human = data_human.append(data[id == data.id])
    else:
        data_macaca = data_macaca.append(data[id == data.id])

print 'macaca pn: %s  ps: %s' % (sum(data_macaca.pn)/len(data_macaca), sum(data_macaca.ps)/len(data_macaca))

print 'human pn: %s  ps: %s' % (sum(data_human.pn)/len(data_human), sum(data_human.ps)/len(data_human))



