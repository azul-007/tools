import re
import sys
import time
import os.path
import paramiko

user_file = input("Enter user file name: ")

#Verify the validity of the username/passwd file
if os.path.isfile(user_file) == True:
    
    print("\n* Username/Password file is valid")

else:

    print("\n* File {} does not exist".format(user_file))
    sys.exit()


#Checking commands file
cmd_file = input("\nEnter commands file name: ")

#Verify the valide commands file
if os.path.isfile(cmd_file) == True:

    print("\n* Command file is valid. Sending commands to devices." + "\n")

else:

    print("\n* File {} does not exist.".format(cmd_file))
    sys.exit()


#Open SSHv2 connection to the device
def ssh_conn(ip):

    global user_file
    global cmd_file

    #Create SSH connection
    try:

        #Define SSH params
        selected_user_file = open(user_file, 'r')

        #Starting from the beginning of the file
        selected_user_file.seek(0)

        #Grab username
        username = selected_user_file.readlines()[0].split(',')[0].rstrip("\n")

        #Starting from the beginning of the file...again
        selected_user_file.seek(0)

        #Grab password
        password = selected_user_file.readlines()[0].split(',')[1].rstrip("\n")

        #Log into switches
        session = paramiko.SSHClient()

        #Allows auto-accepting unknown host keys
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #Connect to the device
        session.connect(ip.rstrip("\n"), username=username, password=password)

        #Start an interactive shell session on the router
        connection = session.invoke_shell()

        #Setting terminal length for entire output 
        connection.send("enable\n")
        connection.send("terminal length 0\n")
        time.sleep(1)

        #Entering global config mode
        connection.send("\n")
        connection.send("configure terminal\n")
        time.sleep(1)

        #Open user selected file for reading
        selected_cmd_file = open(cmd_file,'r')

        #Starting from the beginning of the cmd file
        selected_cmd_file.seek(0)

        #Writing each line in the file to the device
        for each_line in selected_cmd_file.readlines():

            connection.send(each_line + "\n")
            time.sleep(2)

        #close user file
        selected_user_file.close()

        #Close cmd file
        selected_cmd_file.close()

        #Checking command output for IOS 
        router_output = connection.recv(65535)
       
        if re.search(b"% Invalid input", router_output):

            print("There was at least one IOS syntax error on device {}".format(ip))

        else:

            print("\nDONE for device {} Data sent to file at {} \n".format(ip, str(datetime.datetime.now())))
        
        #Search for CPU Utilization values within the output of "show processes top once"
        cpu = re.search(b"%Cpu\(s\):(\s)+(.+?)(\s)* us,",router_output)

        #Extract the second group. Matches the actual value of the CPU utilization and decoding to the UTF-8 format from the binary data type
        utilization = cpu.group(2).decode("utf-8")

        with open("cpu.txt","a") as f:
            f.write(utilization + "\n")

        

        #Closing connection
        session.close()

    except paramiko.AuthenticationException:
        print("Invalid username or password. Closing program")