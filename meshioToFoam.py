import sys
import meshio

from openfoam.folderStructure import *
from writers.fileWriter import *

# Reading arguments
file_in = sys.argv[1]
file_out = sys.argv[2]


# Reading the mesh
mesh = meshio.read(file_in)


# Creating folder structure
createFolderStructure(file_out)


# Writing files
writePointsFile(mesh, file_out)
writeBoundaryFile(mesh, file_out)
