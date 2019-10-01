#!python3
# -*- coding: utf-8 -*-

from pysnmp.hlapi import *

def SNMPv2Walk(community_string, ip):
	"""
	SNMPv2c Walk and Serial number extraction
	:param community_string: your set SNMPv2 community string
	:param ip: IPv4 address of the target host
	:return: version - String representation of device version
	:return: SNMP_response - Multi-line string response from device
	"""
	errorIndication, errorStatus, errorIndex, varBinds = next(
		getCmd(SnmpEngine(),
			   CommunityData(community_string, mpModel=0),
			   UdpTransportTarget((ip, 161)),
			   ContextData(),
			   ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))))

	if errorIndication:
		print(f"[-] {ip} -- SNMP Walk FAIL!!")
		print(errorIndication)
	elif errorStatus:
		print(f"[-] {ip} -- SNMP Walk FAIL!!")
		print('%s at %s' % (errorStatus.prettyPrint(),
							errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
	else:
		print(f"[+] {ip} -- SNMP Walk Success!")
		for varBind in varBinds:
			SNMP_response = ([x.prettyPrint() for x in varBind])

	for line in SNMP_response:
		split_response = line.split(',')

	for entry in split_response:
		entry.strip()

	for entry in split_response:
		if "Version" in entry:
			version = (entry.strip("Version "))
			print(f"[+] {ip} -- Version -- {version}")
			# 16.3.6
	return SNMP_response, version
  
if __name__ == "__main__":
    while True:
        com_str = input(f"Community String: ")
        ip_adr = input(f"IPv4 Address: ")
        try:
            SNMPv2Walk(com_str, ip_adr)
        except:
            
            print("\n")
