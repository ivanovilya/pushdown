class Pushdown(object):
    def __init__(self, fileName):
        sep = '\n'
        with open(fileName) as fin:
            text = fin.read()
            
        lines = text.split(sep)
        sep = '\t'
        nmk = lines[0].split(sep)
        self.n = int(nmk[0]) 
        self.m = int(nmk[1]) 
        self.k = int(nmk[2])
        #print self.n, self.m, self.k
        
        second = lines[1].split(sep)
        
        self.state = int(second[0])
        self.stack = second[1]
        #print self.state, len(self.stack), self.stack
        #print lines[2: 2 + self.n* (self.m + 1) + 1]
        self.phi = self.createMap(lines[2: 2 + self.n* (self.m + 1) + 1])
        #print self.phi
        #print lines[3 + self.n* (self.m + 1): 4 + 2 * self.n* (self.m + 1)]
        self.psi = self.createMap(lines[3 + self.n* (self.m + 1): 4 + 2 * self.n* (self.m + 1)])
        #print self.psi
        #print lines[4 + 2*self.n* (self.m + 1): 5 + 3 * self.n* (self.m + 1)]
        self.eta = self.createMap(lines[4 + 2*self.n* (self.m + 1): 5 + 3 * self.n* (self.m + 1)])
        #print self.eta
        
    def createMap(self, lines):
        #print lines[0]
        result = {}
        for i in range(self.n):
            result[i] = {}
        for line in lines[1:]:
            split_line = line.split('\t')
            #print split_line
            result[int(split_line[0])][int(split_line[1])] = split_line[2] 
        return result
    
    def calculatePeriod(self, verbose=0, upper_bound=1000000000):
        if verbose > 0:
            print(0, self.state, self.stack)
        result = 1
        while(self.step() != 1):
            result = 1
        if verbose > 0:
            print(result, self.state, self.stack)
        while(self.step() != 1):
            result += 1
            if result > upper_bound:
                print("endless loop")
                return result
            if verbose > 0:
                 print(result, self.state, self.stack)
            
        return result
    
    def step(self):
        #print self.state, self.z(), self.psi
        result = self.psi[self.state][self.z()]
        next_state = int(self.phi[self.state][self.z()])
        next_stack = self.nextStack()
        self.state = next_state
        self.stack = next_stack
        return int(result)
    
    def z(self):
        if len(self.stack) == 0:
            return 0
        else:
            return int(self.stack[-1])
        
    def nextStack(self):
        if self.eta[self.state][self.z()] == "0":
            return self.stack[:-1]
        else:
            return self.stack[:-1] + self.eta[self.state][self.z()]