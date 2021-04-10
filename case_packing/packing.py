"""
Copyright 2021 Chen Xiaoxiao

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os
dir = os.path.abspath(__file__)
dir = os.path.dirname(dir)
print("Run Python script in "+dir+"...")
os.chdir(dir)

import sys
sys.path.append('..')

from pythonModule.packingCloud import *

def main():
    argList = sys.argv

    diameter = float(sys.argv[sys.argv.index("-d")+1])
    print("The diameter of particle is %f" % diameter)

    nParticles = int(sys.argv[sys.argv.index("-nP")+1])
    print("The number of particles in one parcel is %d" % nParticles)

    height = float(sys.argv[sys.argv.index("-h")+1])

    box = packingBox([0., 0., -0.1], [1.0, 0.05, -0.1+height])
    #box = packingBox([0., 0., 0], [1e-32, 1e-32, 1e-32])
    cloud = packingCloud(box)
    cloud.generateParcels(diameter, nParticles)
    cloud.writeKinematicCloudPositions()


if __name__ == '__main__':
    main()