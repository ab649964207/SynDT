import os
import sys
import subprocess

approach = sys.argv[1]
PDDLFolder =sys.argv[2] 
resultFile =sys.argv[3]
gameType = sys.argv[4]

# approach = "SynDT.py"
# PDDLFolder=r'.\domain\1.Sub\1.1 Take-away'  
# resultFile = r".\result.xls" 
# gameType='normal' 

PDDLlist = os.listdir(PDDLFolder)
PDDLlist = sorted(PDDLlist,key=lambda x: os.path.getmtime(os.path.join(PDDLFolder, x)))
for i in PDDLlist:
    if 'pddl' in i:
        # print(i) 
        i=PDDLFolder+'\\'+i
        subprocess.call("python \"%s\" \"%s\" \"%s\" \"%s\" "%(approach, i, resultFile, gameType))

    