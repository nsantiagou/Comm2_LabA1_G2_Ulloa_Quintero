import numpy as np
from gnuradio import gr

class blk(gr.sync_block): 
    def __init__(self, example_param=1.0):
        gr.sync_block.__init__(
            self,
            name='e_Diff',
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.prev = 0.0

    def work(self, input_items, output_items):
        x = input_items[0]
        y = output_items[0]

        for i in range(len(x)):
            y[i] = x[i] - self.prev
            self.prev = x[i]

        return len(y)

