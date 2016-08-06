class MaxPushdownGeneratorSpecialCase(object):
    def __init__(self, n, fileName):
        self.sim_n = n
        self.n = 11 * n
        self.m = 2
        self.k = 2
        
        with open(fileName, 'w') as fout:
            fout.write(str(self.n))
            fout.write('\t')
            fout.write(str(self.m))
            fout.write('\t')
            fout.write(str(self.k))
            fout.write('\n')
            fout.write('0')
            fout.write('\t\n')
            
            fout.write('phi\n')
            for q in range(self.n):
                for z in range(self.m+1):
                    fout.write(str(q) + '\t' + str(z) + '\t' + str(self.phi(q,z)) + '\n')
 
            fout.write('psi\n')
            for q in range(self.n):
                for z in range(self.m+1):
                    fout.write(str(q) + '\t' + str(z) + '\t' + str(self.psi(q,z)) + '\n')
            
            fout.write('eta\n')
            for q in range(self.n):
                for z in range(self.m+1):
                    fout.write(str(q) + '\t' + str(z) + '\t' + str(self.eta(q,z)) + '\n')
                    
    def psi(self, q, z):
        if q == 0 and z == 0:
            return 1
        return 0
    
    def phi(self, q, z):
        num, level = getNumAndLevel(q)
        
        if level > 0 and num == 2 and z == 2:
            return getState(0, level - 1)
        
        if level < self.sim_n - 1 and num == 10:
            return getState(0, level + 1)
            
        if num == 0 and z == 1:
            return getState(1, level)
        
        if num == 0 and z == 2:
            return getState(2, level)
        
        if num == 0 and z == 0:
            return getState(3, level)
        
        if num == 3:
            return getState(4, level)
            
        if num == 4:
            return getState(5, level)
        
        if num == 1 and z == 1:
            return getState(5, level)
        
        if num == 5:
            return getState(6, level)
            
        if num == 6:
            return getState(7, level)

            
        if num == 2 and z == 1:
            return getState(7, level)
        
        if num == 7:
            return getState(8, level)
        
        if num == 8:
            return getState(9, level)
            
        if num == 1 and level < self.sim_n - 1 and z == 2:
            return getState(9, level)
            
        if num == 9 and level < self.sim_n - 1:
            return getState(10, level)
        
        if num == 1 and level == self.sim_n - 1 and z == 2:
            return getState(0, level)

        if num == 9 and level == self.sim_n - 1:
            return getState(0, level)
        
        return q
        
                    
    def eta(self, q, z):
        num, level = getNumAndLevel(q)
        
        if level > 0 and num == 2 and z == 2:
            return '0'
        
        if level < self.sim_n - 1 and num == 10:
            return '11'
            
        if num == 0 and z == 1:
            return '0'
        
        if num == 0 and z == 2:
            return '0'
        
        if num == 0 and z == 0:
            return '11'

        if num == 3:
            return '11'
            
        if num == 4:
            return '11'
        
        if num == 1 and z == 1:
            return '11'
        
        if num == 5:
            return '21'
            
        if num == 6:
            return '21'

        if num == 2 and z == 1:
            return '21'
        
        if num == 7:
            return '11'
        
        if num == 8:
            return '21'
            
        if num == 1 and level < self.sim_n - 1 and z == 2:
            return '21'
            
        if num == 9 and level < self.sim_n - 1:
            return '21'
        
        if num == 1 and level == self.sim_n - 1 and z == 2:
            return '0'

        if num == 9 and level == self.sim_n - 1:
            return '1'
        
        return '0'
    
    def theoryEstimate(self):
        return 15*4**self.sim_n - 19

def getState(num, level):
    return num + 11 * level
    
def getNumAndLevel(q):
    num = q % 11
    level = q / 11
    return num, level


class MaxPushdownGenerator(object):
    def __init__(self, n, m, k, fileName):
        self.n = n
        self.m = m
        self.k = k
        with open(fileName, 'w') as fout:
            fout.write(str(n))
            fout.write('\t')
            fout.write(str(m))
            fout.write('\t')
            fout.write(str(k))
            fout.write('\n')
            fout.write('0')
            fout.write('\t\n')
            
            fout.write('phi\n')
            for q in range(n):
                for z in range(m+1):
                    fout.write(str(q) + '\t' + str(z) + '\t' + str(self.phi(q,z)) + '\n')
 
            fout.write('psi\n')
            for q in range(n):
                for z in range(m+1):
                    fout.write(str(q) + '\t' + str(z) + '\t' + str(self.psi(q,z)) + '\n')
            
            fout.write('eta\n')
            for q in range(n):
                for z in range(m+1):
                    fout.write(str(q) + '\t' + str(z) + '\t' + str(self.eta(q,z)) + '\n')
    
    def phi(self, q, z):
        if z == self.m and q != 0:
            return q-1
        if z == self.m - 1 and q != self.n - 1:
            return q + 1
        return q
    
    def psi(self, q, z):
        if q == 0 and z == 0:
            return 1
        return 0
    
    def eta(self, q, z):
        if z == 0:
            return repeat(self.k, '1')
        if z == self.m:
            return '0';
        if z == self.m - 1 and q == self.n - 1:
            return '0'
        if z == self.m - 1 and q != self.n - 1:
            return str(self.m) + repeat(self.k - 1, '1')
        return repeat(self.k, str(z + 1))
    
    def theoryEstimate(self):
        k = self.k
        m = self.m
        n = self.n
        if k == 2 and m == 2:
            return 4*n - 1
        else:
            m = m - 1
            return (k**m - 1)/(k-1) + k**m * ( (1+k**(m-1))*((k**m - k**(m-1))**(n-1) - 1)/(k**m - k**(m-1) - 1) + (k**m - k**(m-1))**(n-1) )
        
def repeat(ntimes, symbol):
    result  = ''
    for i in range(ntimes):
        result += symbol
    return result
    
    

class MaxRocaGenerator(object):
    def __init__(self, n, s, k, fileName):
        self.n = n
        self.m = m = 1
        self.k = k
        self.s = s
        self.h = ((k-1)*(n-s+1) + 2) % s
        with open(fileName, 'w') as fout:
            fout.write(str(n))
            fout.write('\t')
            fout.write(str(m))
            fout.write('\t')
            fout.write(str(k))
            fout.write('\n')
            fout.write(str(self.h))
            fout.write('\t\n')
            
            fout.write('phi\n')
            for q in range(n):
                for z in range(m+1):
                    fout.write(str(q) + '\t' + str(z) + '\t' + str(self.phi(q,z)) + '\n')
 
            fout.write('psi\n')
            for q in range(n):
                for z in range(m+1):
                    fout.write(str(q) + '\t' + str(z) + '\t' + str(self.psi(q,z)) + '\n')
            
            fout.write('eta\n')
            for q in range(n):
                for z in range(m+1):
                    fout.write(str(q) + '\t' + str(z) + '\t' + str(self.eta(q,z)) + '\n')
    
    def phi(self, q, z):
        if z == 0:
            if q == self.h:
                return self.s
            else:
                return self.s + (self.h - (q - self.s) - 1) % self.s / (self.k - 1)
            
        else:
            if q < self.s:
                return (q + 1) % self.s
            else:
                if q + 1 == self.n:
                    return 0
                else:
                    return q + 1
        return q
    
    def psi(self, q, z):
        if q == self.h and z == 0:
            return 1
        return 0
    
    def eta(self, q, z):
        if q >= self.s:
            return repeat(self.k, str(1))
        else:
            if z == 0:
                if q == self.h:
                    return repeat(self.k, str(1))
                else:
                    return repeat(self.k - 1 - ((self.h - (q - self.s) - 1) % self.s) % (self.k - 1), str(1))    
            else:
                return '0'
        print ('eta error', 'q = ', q, 'z = ', z, 'h = ', self.h)
        return '0'
    
    def theoryEstimate(self):
        k = self.k
        s = self.s
        n = self.n
        summ = 0
        for i in range(s-1):
            summ += i/(k-1)
        
        return  s*k*(n -s +1) + s - s*(s-1)/2 - summ