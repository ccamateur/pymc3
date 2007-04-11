from PyMC2 import Sampler, JointMetropolis
from PyMC2.examples import model_for_joint
from pylab import plot, show,title, xlabel, ylabel, figure

from numpy.testing import *
PLOT=True

class test_Joint(NumpyTestCase):
    def check(self):
        M = Sampler(model_for_joint)
        M.sample(iter=30000,burn=0,thin=100)
        if PLOT:
            plot(M.A.trace.gettrace()[:,0],M.B.trace.gettrace()[:,0],'b.')
            title('First elements')
            xlabel('A')
            ylabel('B')
            figure()
            plot(M.A.trace.gettrace()[:,1],M.B.trace.gettrace()[:,1],'b.')
            title('Second elements')
            xlabel('A')
            ylabel('B')
            figure()
            plot(M.A.trace.gettrace()[:,0])
            figure()
            plot(M.A.trace.gettrace()[:,1])
            show()

if __name__ == '__main__':
    NumpyTest().run()
