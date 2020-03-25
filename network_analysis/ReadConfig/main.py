import sys
from ip_reach import ip_reach
from ssh_conn import ssh_conn
from ip_file_valid import ip_file_valid
from ip_addr_valid import ip_addr_valid
from create_threads import create_threads

#Save the list of IP addresses
ip_list = ip_file_valid()

#Verify the validity of each IP
try:

	ip_addr_valid(ip_list)

except KeyboardInterrupt:
	print("Program interrupted by user.")
	sys.exit()


#Verify reachability of each IP
try:

	ip_reach(ip_list)

except KeyboardInterrupt:
	print("Program interrupted by user.")
	sys.exit()

#Calling threads creation for each ssh connection
create_threads(ip_list, ssh_conn)