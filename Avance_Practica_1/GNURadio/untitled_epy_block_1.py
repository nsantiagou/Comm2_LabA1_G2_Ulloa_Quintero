import numpy as np
from gnuradio import gr

class blk(gr.sync_block): 

    def __init__(self, example_param=2.0):
        gr.sync_block.__init__(
            self,
            name='e_Diff',
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.e_Acum = 0

    def work(self,input_items,output_items):
        x = input_items[0]  
        y0 = output_items[0]
        diff = np.diff(np.concatenate(([self.e_Acum],x)))
        y0[:] = diff 
        self.e_Acum = x[-1]
        return len(y0)
