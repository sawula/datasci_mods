class Scale_linear(object):
    def __init__ (self):
        self.domain_lo = 0
        self.domain_hi = 0
        self.range_lo = 0
        self.range_hi = 0
        
    def domain(self, lo, hi):
        self.domain_lo = lo
        self.domain_hi = hi
        
    def range(self, lo, hi):
        self.range_lo = lo
        self.range_hi = hi
        
    def __call__ (self, domain_x):
        domain_span = self.domain_hi - self.domain_lo
        if domain_span == 0:
            raise Exception('The lower and upper values of the domain should not be equal. Reset the domain.')
        range_span = self.range_hi - self.range_lo
        range2domain = range_span / domain_span
        range_x = int((domain_x - self.domain_lo)*range2domain + self.range_lo)
        return range_x
