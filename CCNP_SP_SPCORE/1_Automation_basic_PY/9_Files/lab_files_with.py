# create variable of class list named 'intf' with dictionaries which contains follow items and keys
## {'int': 'interface', 'name': 'G0/0'}
## {'int': 'interface', 'name': 'G0/1'}
## {'int': 'interface', 'name': 'G0/2'}
## {'desc': 'description', 'name': 'Connected via Python'}
## {'cmd': 'no', 'status': 'shut'}

import os
os.chdir("/mnt/c/Users/tomas/OneDrive/Documents/Git/misc/CCNP_SP_SPCORE/Files")

intf = [{'int': 'interface', 'name': 'G0/0'}, 
        {'int': 'interface', 'name': 'G0/1'},
        {'int': 'interface', 'name': 'G0/2'},
        {'desc': 'description', 'name': 'Connected via Python'},
        {'cmd': 'no', 'status': 'shut'}
          ]



# craete a new variable named 'modify_intf' which creates a new file with write permission 
# called "r1.interface.cfg". Use the WITH statment.
# write the contents of the list 'intf' to r1.interface.cfg as follow
## intereface G0/0
##    description Connected via Python
##    no shut
## intereface G0/1
##    description Connected via Python
##    no shut
## intereface G0/2
##    description Connected via Python
##    no shut

with open('r1.interface.cfg', 'w') as modify_intf:
    modify_intf.write(intf[0]['int'] + ' ' + intf[0]['name'] + '\n')
    modify_intf.write('  ' + intf[3]['desc'] + ' ' + intf[3]['name'] + '\n')
    modify_intf.write('  ' + intf[4]['cmd'] + ' ' + intf[4]['status'] + '\n')

    modify_intf.write(intf[1]['int'] + ' ' + intf[1]['name'] + '\n')
    modify_intf.write('  ' + intf[3]['desc'] + ' ' + intf[3]['name'] + '\n')
    modify_intf.write('  ' + intf[4]['cmd'] + ' ' + intf[4]['status'] + '\n')

    modify_intf.write(intf[2]['int'] + ' ' + intf[2]['name'] + '\n')
    modify_intf.write('  ' + intf[3]['desc'] + ' ' + intf[3]['name'] + '\n')
    modify_intf.write('  ' + intf[4]['cmd'] + ' ' + intf[4]['status'] + '\n')



# ensure print(R1) prints the content of the file
temp = open('r1.interface.cfg', 'r')
R1 = temp.read()
print(R1)


