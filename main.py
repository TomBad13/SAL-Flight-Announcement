#[NUMBER] [AUTOMATIC CALLSIGNS] [SAME DATE] [DATE]
import sys,subprocess
Number = int(sys.argv[1])
if Number > 1:
    AutoCallsign = sys.argv[2].upper()
else:
    AutoCallsign = "N"
SameDate = sys.argv[3].upper()
if SameDate == "Y":
    Date = sys.argv[4]
else:
    Date = None
subprocess.run(["python", "Execute.py", Number, AutoCallsign, SameDate, Date])
