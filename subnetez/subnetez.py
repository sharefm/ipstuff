'''
Created on Dec 12, 2013

@author: Sharef Mustafa

iptrans can calculate IPv4 CIDR, mask, wildcard mask and size of IP block just by giving it
one of those and it will calculate the others

No verification of input yet, nor exceptions too

setSize will calculate the nearest cidr that fits the given number of IPs i.e setSize(1000) ==> cidr = /22


'''
import math;

class subnetez:
    
    cidr = 0;
    size = 0;
    mask = [0,0,0,0]
    wild = [0,0,0,0]
    
    def setCidr(self, c):
        self.cidr = c        
        self.calculateMask()               
        self.CalculateWild()        
        self.calculateSize()
            
    def setMask(self,m):
        self.mask = m        
        self.calculateCidr()        
        self.CalculateWild()            
        self.calculateSize()
        
    
    def setWild(self,w):
        '''
        setWild will calculate the mask and then call setMask which will calculate cidr and size
        
        '''
        self.wild = w        
        for n in range(0,4):
            self.mask[n] = 255 - int(self.wild[n])
        self.setMask(self.getMask())
        
    
    def setSize(self, s):
        '''
        setSize will calculate the cidr and call setCidr to calculate mask and wildcard mask
        
        '''
        self.size = s        
        self.setCidr(int(32 - math.log(s,2)))
        
        
    def calculateCidr(self):
        '''
        calculateCidr requires the mask to be set 1st
        
        '''
        cidr = 0
        m = self.getMask()
        for k in range(0,4):
            if m[k] == 255:
                cidr = cidr + 8
            if m[k] != 0 and m[k] != 255:                
                cidr = cidr + int( 8 - math.log(256-m[k] , 2) )            
            self.cidr = cidr   
              
              
        
    def calculateMask(self):
        '''
        CalculatesMask require the cidr to be set 1st
        
        '''
        b = [255,255,255,255]
        bindex = (int)(self.cidr/8) + 1        
        byteMask = 256 - pow(2, ( 8*bindex) - (self.cidr) ) 
        
        for k in range(0,4):            
            if k < bindex-1:
                b[k] = 255
            if k == bindex-1:
                b[k] = byteMask
            if k > bindex-1:
                b[k] = 0                
        self.mask = b
    
    
    def CalculateWild(self):
        for k in range(0,4):
            self.wild[k] = 255 - self.mask[k]
    

    def calculateSize(self):
        '''
        calculateSize calculates the size of the IP block including subnetwork address and broadcast address
        i.e /24 will report a size of 256 , even though there will be 254 usable IPs
        i.e /22 will report a size of 256 , even though there will be 1022 usable IPs
        
        '''
        self.size = pow(2,(32-self.cidr))
            

    def getCidr(self):
        return int(self.cidr)      
    
    def getMask(self):
        return self.mask
    
    def getWild(self):
        return self.wild
    
    def getSize(self):
        return int(self.size)
    
    def printSubnet(self):
        print "/", i.getCidr() ,i.getMask(), i.getWild(), i.getSize()
    
    def genMasks(self,):
        '''
        this function is just to verify that the class is working properly, it will print
        the whole IPv4 subnet mask table , it will start from CIDR /0 till /32 and print:
        sequence# CIDR MASK WILDCARD-MASK SIZE-OF-IP-BLOCK
        
        i.e for cidr /19 it will print: 
        19 19 [255, 255, 224, 0] [0, 0, 31, 255] 8192
        
        if the class was be modified this function will hekp the developer verify if the modifications 
        were correct or not by comparing it's output with a ipv4 subneting cheat sheet
        '''
        maskBytes = [0,128,192,224,240,248,252,254,255]
        mask = [0,0,0,0]
        for a in range(0,33):
            for b in range(0,a/8):
                mask[b] = 255
            for c in range(a/8,4):
                mask[a/8] = maskBytes[a%8]
            self.setMask(mask)
            print a,self.getCidr(), self.getMask(), self.getWild(), self.getSize()
        
        
'''        
i = subnetez()
i.setSize(1000)
i.printSubnet()

i = subnetez()
i.setCidr(22)
i.printSubnet()

i = subnetez()
i.setMask([255,255,252,0])
i.printSubnet()
'''
i = subnetez()
i.setWild([0,0,3,255])
print i.getSize()
i.printSubnet()

#i = subnetez()
#i.genMasks()




