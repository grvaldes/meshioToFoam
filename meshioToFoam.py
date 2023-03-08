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
writePointsFile(mesh, file_out)
writeBoundaryFile(mesh, file_out)
