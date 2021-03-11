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

import numpy as np
import os


class packingCloud:
    def __init__(self, box):
        """
        [input]
        box: Instance of packingBox
        """
        self.parcels = []
        self.packingBox = box

    def generateParcels(self, diameter, nParticles):
        """
        [input]
        diameter:   particle diameter
        nParticles: particle number per parcel
        """
        # 估算颗粒团的尺寸
        # Estimate the size of the parcel
        size = diameter * nParticles**(1/3) * 2
        div = self.packingBox.divBySize(size)
        for i in range(div[0]):
            for j in range(div[1]):
                for k in range(div[2]):
                    position = np.array([
                        self.packingBox.AA[0] + i * size + size / 2,
                        self.packingBox.AA[1] + j * size + size / 2,
                        self.packingBox.AA[2] + k * size + size / 2])

                    self.parcels.append(kinematicParcel(size,
                                                        diameter,
                                                        nParticles,
                                                        position))

        print("Successfully generate %d parcels." % (div[0]*div[1]*div[2]))

    def writeKinematicCloudPositions(self):
        with open("./constant/kinematicCloudPositions.template", "r") as f:
            with open("./constant/kinematicCloudPositions", "w") as f_w:
                for line in f:
                    f_w.write(line)
                f_w.write("\n")
                f_w.write("(\n")
                for p in self.parcels:
                    f_w.write(
                        "(%.12f %.12f %.12f)\n" % (p.position[0],
                                                   p.position[1],
                                                   p.position[2]))
                f_w.write(")\n")


class kinematicParcel:
    def __init__(self, parcelSize, particleDiameter, nParticles, position):
        """
        [input]
        parcelSize:         parcel size
        particleDiameter:   particle diameter
        nParticles:         particle number per parcel
        position:           center of parcel(np.array)
        """
        self.parcelSize = parcelSize
        self.particleDiameter = particleDiameter
        self.nParticles = nParticles
        self.position = position


class packingBox:
    def __init__(self, AA, BB):
        """
        [input]
        AA: corner coordinate at left-bottom
        BB: corner coordinate at right-top
        """
        self.AA = AA
        self.BB = BB

        self.x = BB[0] - AA[0]
        self.y = BB[1] - AA[1]
        self.z = BB[2] - AA[2]
        # 作为盒子的尺寸， x、y、z必须为正
        # Note that x, y, z are always positive
        if self.x <= 0 or self.y <= 0 or self.z <= 0:
            print("Error: x, y, z need positive values.")
            exit()

    def divBySize(self, size):
        """
        [input]
        size: parcel size

        [output]
        div: list of divide number through x-direction, y-direction and z-direction
        """
        return int(self.x / size), int(self.y / size), int(self.z / size)
