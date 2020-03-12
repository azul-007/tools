#!/usr/bin/python3

#Author: azul007
#Date: 03/11/2020

def bin_num():	

	for num in range(256):

		bin_a = bin(num)
		bin_a = bin_a[2:] #Strip "0b"
		
		if len(bin_a) < 8:

			diff = 8 - len(bin_a)
		
			add_zero = "0" * diff
	
			print(num, "\t", str(add_zero + bin_a))
		else:

			print(num, "\t", bin_a)
		
bin_num()



