import numpy as np
from gnuradio import gr

class blk(gr.sync_block): 
    def __init__(self, example_param=2.0):
        gr.sync_block.__init__(
            self,
            name='e_Acum',
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.accum = 0.0  # Valor acumulado inicial

    def work(self, input_items, output_items):
        x = input_items[0]   # Señal de entrada
        y = output_items[0]  # Señal acumulada

        # Acumulación con estado
        for i in range(len(x)):
            self.accum += x[i]
            y[i] = self.accum

        return len(y)

