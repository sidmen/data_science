import os
from pathlib import Path

CWD = os.getcwd()
project_dir = Path(CWD).parent.parent


path_to_file = str(project_dir) + '\configuration.csv'
os.chdir(project_dir)
print(path_to_file)
