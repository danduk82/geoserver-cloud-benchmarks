import sys
import os.path

MYPATH = os.path.join(os.path.dirname(__file__), "../generated")
if MYPATH not in sys.path:
    sys.path.append(MYPATH)