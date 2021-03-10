#!/usr/bin/python3
import os, sys, subprocess

if len(sys.argv) != 3:
	print(f"{sys.argv[0]} <url filename path> <output file path>\nEx: {sys.argv[0]} url.txt output.txt\n")
	sys.exit(1)

file = open(sys.argv[2], "w")

with open(sys.argv[1]) as f:
	for i in f:
		cmd = "node src/drivers/npm/cli.js " + i
		print(f"Scanning IP: {i}")

		try:
			output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
			file.write(output.decode())
		except subprocess.CalledProcessError:
			print("Execution of '%s' failed!\n" % cmd)
			sys.exit(1)
file.close()