# coding=utf-8
'2.12 Sanitizing and cleaning up text'


s = 'pýtĥöñ\fis\tawesome\r\n'

print s

remap = {
	ord('\t'): ' ',
	ord('\f'): ' ',
	ord('\r'): None # Deleted
}

a = s.translate(remap)
print a