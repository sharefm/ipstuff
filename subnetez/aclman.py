'''
Created on Jan 31, 2014

@author: sim

this script take cisco router configuration file and finds access-list statements that are used to redirect traffic to caches
the statements should start with "access-list" and has an 180< acl# <190 and contains "permit"
the wild card mask is extracted from that statement, the wildard mask is identified by it's starting zero
which is a special case fo rthe config file I'm dealing with, there should be better ways to identify it

'''

from subnetez import subnetez
conf = open("c:\\7600.conf",'r')
lines = conf.readlines()
tot = 0
i = subnetez()
for line in lines:
    
    if line.startswith("access-list"):        
        l = line.split()        
        if l[0] == "access-list" and int(l[1])>180 and int(l[1])<190 and l[2].strip() == "permit":                   
            
            for w in line.split():                
                if w.strip() != "ip" and w.strip() != "any" and w.strip().startswith("0"):
                    '''filters all words except for the wildcard mask'''
                    prefix = w.strip().split('.')
                    i.setWild(prefix)
                    '''print line, i.getSize()'''
                    tot = tot + i.getSize()        

print "total cached IP addresses = ",tot

