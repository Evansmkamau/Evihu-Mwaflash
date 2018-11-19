#!/usr/bin/env python
import subprocess #This line imports the subprocess module
for i in range(5):
        try:
                result = subprocess.check_output(['evihmu_update', '--profile', 'developer'])
                print(result)
        except Exception as e:
                print('failure: {}.'.format(e))
        else:
                print('success')
~                                                                                                                                                                                             
~                                       
