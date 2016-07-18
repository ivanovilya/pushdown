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
        return repeat(k, str(z + 1))
    
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