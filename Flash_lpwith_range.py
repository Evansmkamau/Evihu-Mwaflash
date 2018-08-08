#!/usr/bin/env python
import subprocess
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
