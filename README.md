# Evihu-Mwaflash
Clean continuous flash
#!/usr/bin/env python
import subprocess
from time import sleep
x=0
while (x<5):
	try:
 	 result = subprocess.check_output(['ihu_update', '--profile', 'developer'])
 	 print(result)
	except Exception as e:
 	 print('failure: {}.'.format(e))
	else:
 	 print('success')
++x
