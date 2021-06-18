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

import sys
sys.path.append('..')

import os
dir = os.path.abspath(__file__)
dir = os.path.dirname(dir)
print("Run Python script in "+dir+"...")
os.chdir(dir)

import math
from pythonModule.packingCloud import packingCloud,packingBox

def main():
    argList = sys.argv
    diameter = float(sys.argv[sys.argv.index("-d")+1])
    print("The diameter of particle is %f m" % diameter)

    nParticles = int(sys.argv[sys.argv.index("-np")+1])
    print("The number of particles in one parcel is %d" % nParticles)

    startX = float(sys.argv[sys.argv.index("-sx")+1])
    startY = float(sys.argv[sys.argv.index("-sy")+1])
    startZ = float(sys.argv[sys.argv.index("-sz")+1])
    print("The bed start point is (%f %f %f) m" % (startX, startY, startZ))

    length = float(sys.argv[sys.argv.index("-l")+1])
    width = float(sys.argv[sys.argv.index("-w")+1])
    height = float(sys.argv[sys.argv.index("-h")+1])
    print("The bed size is (%f %f %f)(Radically) m" % (length, width, height))

    scaleSize = float(sys.argv[sys.argv.index("-s")+1])
    print("The scaleSize is %f" % scaleSize)

    volFraction = float(sys.argv[sys.argv.index("-vf")+1])
    print("The volume fraction is %f" % volFraction)

    fixHeight = float(sys.argv[sys.argv.index("-fh")+1])
    fixNumber = int(length*width*fixHeight*volFraction /
                    (math.pi*4/3*(diameter/2)**3)/nParticles)
    print("Limit bed height at %f m" % fixHeight)
    print("Fix parcel number at %d" % fixNumber)

    box = packingBox([startX, startY, startZ], [
                     startX+length, startY+width, startZ+height])
    #box = packingBox([0., 0., 0], [1e-32, 1e-32, 1e-32])
    cloud = packingCloud(box)
    cloud.generateParcels(diameter, nParticles, fixNumber, scaleSize)
    cloud.writeKinematicCloudPositions()


if __name__ == '__main__':
    main()
