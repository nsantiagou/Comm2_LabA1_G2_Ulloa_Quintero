import numpy as np
from gnuradio import gr


class blk(gr.sync_block):
    def __init__(self, example_param=3.0):
        gr.sync_block.__init__(
            self,
            name='Primedios_de_tiempo',
            in_sig = [np.float32],
            out_sig = [np.float32,np.float32,np.float32,np.float32,np.float32]
        )
        self.acum_anterior = 0
        self.Ntotales = 0
        self.acum_anterior1 = 0
        self.acum_anterior2 = 0

    def work(self, input_items, output_items):
        x = input_items[0]
        y0 = output_items[0]
        y1 = output_items[1]
        y2 = output_items[2]
        y3 = output_items[3]
        y4 = output_items[4]

        # Calculo del p r o m e d i o

        N = len( x )
        self.Ntotales = self.Ntotales + N
        acumulado = self.acum_anterior + np.cumsum ( x )
        self.acum_anterior = acumulado[N -1]
        y0[:]= acumulado / self.Ntotales

        # Calculo de la media c u a d r a t i c a
        x2 = np.multiply(x , x )
        acumulado1 = self.acum_anterior1 + np.cumsum(x2)
        self.acum_anterior1 = acumulado[N -1]
        y1[:] = acumulado1 / self.Ntotales

        # Calculo de la RMS
        y2[:] = np.sqrt(y1)

        # Calculo de la p o t e n c i a p r o m e d i o
        y3[:] = np.multiply( y2 , y2 )

        # Calculo de la d e s v i a c i o n e s t a n d a r
        x3 = np.multiply(x - y0 ,x - y0 )
        acumulado2 = self.acum_anterior2 + np.cumsum( x3 )
        self.acum_anterior2 = acumulado2[N -1]
        y4[:] = np.sqrt( acumulado2 / self.Ntotales )

        return len( x )
