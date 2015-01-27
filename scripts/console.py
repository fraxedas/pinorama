import subprocess as sub

def run(command):
	p = sub.Popen(command,stdout=sub.PIPE,stderr=sub.PIPE)
	output, errors = p.communicate()
	return output