#!/usr/bin/python

'''
This creates a 33,362,176 wordlist 
of 16 character keyboard walks if running virtical only.

Includes:
 top to bottom and bottom to top
 lower case and upper case
 left to right and right to left

Now includes: (If running with the H or B options)
 horizontal

Excludes:
 rotational


Original Author: Ronald Broberg
Edited by: Austin Scott

'''

#####################
# Beginning Imports #
#####################

import sys


#######################
# Beginning Functions #
#######################

def combo(kbc):
	if w.lower() == 'y':
		f = open(fileName, 'w')
		print '''
Writing to %s in current directory

''' % fileName
	else:
		print '''

Outputting to STDOUT

'''
	for a in kbc:
        	for b in kbc:
                	for c in kbc:
                        	for d in kbc:
					if w.lower() == 'y':
						# write to f
						output = ''.join([a,b,c,d])
						output = str(output)
						output = output + '\n'
						f.write(output)
					else:
                                		print ''.join([a,b,c,d])

def hkwg(count):
	c = 0
	d = count
	for i in s:
		a = s[c:d]
		e = 0
		f = 4
		c = c + 1
		if d < 92:
			d = d + 1
		else:
			break
		kbh.append('%s' % a)


#######################
# Beginning Variables #
#######################

global w
global fileName

w = ''
fileName = ''

s = 'qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./`1234567890-=ZXCVBNM<>?ASDFGHJKL:"QWERTYUIOP{}~!@#$%^&*()_+'

kbelems=[
	'1qaz',
	'zaq1',
	'2wsx',
	'xsw2',]

kbh=[]

kbv=[
	'1qaz',
	'2wsx',
	'3edc',
	'4rfv',
	'5tgb',
	'6yhn',
	'7ujm',
	'8ik,',
	'9ol.',
	'0p;/',
	'!QAZ',
	'@WSX',
	'#EDC',
	'$RFV',
	'%TGB',
	'^YHN',
	'&UJM',
	'*IK<',
	'(OL>',
	')P:?',
	'zaq1',
	'xsw2',
	'cde3',
	'vfr4',
	'bgt5',
	'nhy6',
	'mju7',
	',ki8',
	'.lo9',
	'/;p0',
	'ZAQ!',
	'XSW@',
	'CDE#',
	'VFR$',
	'BGT%',
	'NHY^',
	'MJU&',
	'<KI*',
	'>LO(',
	'?:P)',
	'4esz',
	'5rdx',
	'6tfc',
	'7ygv',
	'8uhb',
	'9ijn',
	'0okm',
	'-pl,',
	'=[;.',
	'$ESZ',
	'%RDX',
	'^TFC',
	'&YGV',
	'*UHB',
	'(IJN',
	')OKM',
	'_PL<',
	'+{:>',
	'zse4',
	'xdr5',
	'cft6',
	'vgy7',
	'bhu8',
	'nji9',
	'mko0',
	',lp-',
	'.;[=',
	'ZSE$',
	'XDR%',
	'CFT^',
	'VGY&',
	'BHU*',
	'NJI(',
	'MKO)',
	'<LP_',
	'>:{+',]




#######################
# Beginning Execution #
#######################

if len(sys.argv) > 1:
	if sys.argv[1] == '-h':
		print '''

Useage: python kbwalk_words.py <optional: -h>

	-h 	=	Shows this help text.

Just run it and answer the questions. No command line options at this time.

If you want commandline options you can let me know.

Austin Scott austin.j.scott@lmco.com

'''
		quit()
	else:
		pass
else:
	pass

print '''


##############################################
# Keyboard-Walking Password Generator (KwPG) #
##############################################



'''
w = raw_input('Do you want to save this to a file? (y/n): ')

if w.lower() == 'y':
	fileName = raw_input('Name to save output as (MAX 16 Char Long): ')
	if len(fileName) > 16:
		fileName = str(fileName[0:16])
		fileName = str(fileName) + '.txt'
	else:
		fileName = str(fileName[0:len(fileName)])
		fileName = str(fileName) + '.txt'

choice = raw_input("Select whether you would like a list of Virtical, Horizaontal, or Both (V, H, or B): ")


if choice.lower() == 'v':
	print '''Generating now:

'''
	combo(kbv)
elif choice.lower() == 'h':
        hChoice = raw_input("Do you want to customize length of horizontal key walk?")
	if hChoice.lower() == 'y':
		tCount = raw_input('Specify length of horizontal key walk (1-10): ')
		try:
			tCount = int(tCount)
		except:
			print "Not a legal number. Defaulting to 4."
			cCount = 4
		if tCount > 0 :
			if tCount < 11:
				cCount = tCount
			else:
				print "Not legal number between 1 and 10. Proceeding with 4."
				cCount = 4
		else:
			print 'Not legal number between 1 and 10. Proceeding with 4.'
			cCount = 4
	elif hChoice.lower() == 'n':
		cCount = 4
	else:
		print "Not a choice! Useing default of 4."
		cCount = 4
	print ''' Generating now:

'''
	hkwg(cCount)
	combo(kbh)
elif choice.lower() == 'b':
	print ''' Generating now:

'''
	cCount = 4
	hkwg(cCount)
	kbb = kbv + kbh
	combo(kbb)
else:
	print 'That was not a choice!'
