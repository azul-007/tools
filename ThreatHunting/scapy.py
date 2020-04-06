import sys
import logging
import subprocess
from datetime import datetime

try:
	from scapy.all import *

except ImportError:
	print("Scapy is not installed.")
	sys.exit()

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
logging.getLogger("scapy.interactive").setLevel(logging.ERROR)
logging.getLogger("scapy.loading").setLevel(logging.ERROR)