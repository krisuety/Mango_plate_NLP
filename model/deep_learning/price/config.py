class Config(object):
    def __init__(self, config):
        self.use_cuda = config['use_cuda']
        self.D = config['D']
        self.H = config['H']
        self.H_f = config['H_f']
        self.O = config['O']
        self.num_directions = config['num_directions']
        self.bidirec = config['bidirec']
        self.STEP = config['STEP']
        self.batch_size = config['batch_size']
        self.r = config['r']
        self.num_layers = config['num_layers']
        self.da = config['da'] 

