#!python

import re

TABLE = 0
START_TIME = 1
END_TIME = 2
TITLE = 3
DM = 4
DAY = 5

def print_page(o, table, start_time, end_time, title, dm, day):
    o.write('\\begin{center}\n')
    o.write('\\begin{huge}\n')
    o.write(title + '\n')
    o.write('\\end{huge}\n')
    o.write('\\end{center}\n')

    o.write('\\begin{tabular}{rl}\n')
    o.write('DM: & ' + dm + '\\\\\n')
    o.write('Day: & ' + day + '\\\\\n')

    o.write('Time: & ')
    if len(start_time) > 0:
        o.write(start_time)
    if len(end_time) > 0:
        o.write(' - ' + end_time)
    o.write('\\\\\n')
    o.write('Table: & ' + table + '\\\\\n')
    o.write('\\end{tabular}\n\n')

    o.write('\\vspace{35px}\n\n')

    o.write('\\begin{tabular}{|p{0.5cm}|p{14cm}|}\n')
    o.write('    \\hline\n')
    o.write('    \\multicolumn{2}{|c|}{\\large{Players}} \\\\ \\hline\n')
    o.write('    1 & \\\\ \\hline\n')
    o.write('    2 & \\\\ \\hline\n')
    o.write('    3 & \\\\ \\hline\n')
    o.write('    4 & \\\\ \\hline\n')
    o.write('    5 & \\\\ \\hline\n')
    o.write('    6 & \\\\ \\hline\n')
    o.write('    7 & \\\\ \\hline\n')
    o.write('\\end{tabular}\n\n')
    
    o.write('\\vspace{15px}\n\n')
    
    o.write('\\begin{tabular}{|p{0.5cm}|p{14cm}|}\n')
    o.write('    \\hline\n')
    o.write('    \\multicolumn{2}{|c|}{\\large{Waitlist}} \\\\ \\hline\n')
    o.write('    1 & \\\\ \\hline\n')
    o.write('    2 & \\\\ \\hline\n')
    o.write('    3 & \\\\ \\hline\n')
    o.write('    4 & \\\\ \\hline\n')
    o.write('\\end{tabular}\n\n')
    
    o.write('\\newpage\n\n')

with open('output.tex', 'w') as o:
    o.write("""\\documentclass[12pt]{article}
\\usepackage{fullpage}
\\usepackage{tabularx}
\\usepackage{nopageno}

\\setlength\extrarowheight{7pt}

\\begin{document}
""")
    with open('games.txt', 'r') as g:
        for line in g:
            parts = re.split(r'\t', line)
            print_page(o, parts[TABLE], parts[START_TIME], parts[END_TIME], parts[TITLE], parts[DM], parts[DAY])
        
        for i in range(1, 10):
            print_page(o, '', '', '', '', '', '')

    o.write('\\end{document})\n')
