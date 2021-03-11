import os
os.chdir(os.path.dirname(__file__))

import sys
sys.path.append('..')

from pythonModule.packingCloud import *


def main():
    diameter = 0.0002
    nParticles = 5000
    # box = packingBox([0., 0., 0.], [0.5, 0.2, 0.8])
    box = packingBox([0.0, 0.0, 0], [1e-32, 1e-32, 1e-32])
    cloud = packingCloud(box)
    cloud.generateParcels(diameter, nParticles)
    cloud.writeKinematicCloudPositions()


if __name__ == "__main__":
    main()
