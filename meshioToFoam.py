import sys

import meshiofoam as meshio
from openfoam.folderStructure import *
from writers.fileWriter import *
from openfoam.polyMesh import *

# Reading arguments
file_in = sys.argv[1]
file_out = sys.argv[2]

# Reading the mesh
mesh = meshio.read(file_in)

# Adjusting mesh object according to mesh origin
poly = polyMesh(mesh, file_in.split(".")[-1])

# Creating folder structure
createFolderStructure(file_out)

# Writing files
writePointsFile(poly, file_out)
writeCellsFile(poly, file_out)
writeFacesFile(poly, file_out)
writeOwnerFile(poly, file_out)
writeNeighbourFile(poly, file_out)
writeBoundaryFile(poly, file_out)
writeSets(poly, file_out)
writePointZones(poly, file_out)
writeFaceZones(poly, file_out)
writeCellZones(poly, file_out)
createFoamFile(file_out)
