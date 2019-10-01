
# SNMPv2Walk.py #

10/1/2019
Python 3.7.2

This script dependent upon the following non-default modules (install with pip or git requests.txt):

pysnmp

Initiate this script script directly
from the command line 
ex. 

	$> python SNMPv2Walk.py

_________________________________________________________________________________
This script will execute the following tasks in this order



################
#Sample output:#
################

  $> python SNMPv2Walk.py

  Community String: *****
  IPv4 Address: 74.62.8.44
  [+] 74.62.21.162 -- SNMP Walk Success!
  [+] 74.62.21.162 -- Version -- 15.5(3)M6

  Community String: *****
  IPv4 Address: 8.8.8.8
  [-] 8.8.8.8 -- SNMP Walk FAIL!!
  No SNMP response received before timeout

# TODO: sys.argv[1] to pass IPs in directly from CMD line call.


