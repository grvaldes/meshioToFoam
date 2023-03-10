import numpy as np
from .common import *

class polyMesh:

    def __init__(self, mesh, fileType):
        self.origin = fileType
        self.points = mesh.points
        self.boundFaces = self.getCellsFromMeshio(mesh, 2)
        self.cells = self.getCellsFromMeshio(mesh, 3)
        self.pointZones = self.getZonesFromMeshio(mesh, 1)
        self.faceZones = self.getZonesFromMeshio(mesh, 2)
        self.cellZones = self.getZonesFromMeshio(mesh, 3)

        self.cleanPoints()

        self.faceCenter = {}
        self.cellCenter = {}

        self.getFacesCenter()
        self.getCellsCenter()

        self.faceArea = {}
        self.cellVolume = {}

        self.neighbour = {}
        self.owner = {}
        self.boundary = {}
        self.innerFaces = {}

        self.createInternalFaces()



    
    def getCellsFromMeshio(self, mesh, ndim):
        cells = []

        for cellI in mesh.cells:
            if ndim == topological_dimension[cellI.type]:
                dict = {
                    "type": cellI.type,
                    "nPts": cellI.data.shape[-1],
                    "points": cellI.data
                }
                cells.append(dict) 

        return cells

    
    def getZonesFromMeshio(self, mesh, ndim):
        zones = {}

        if ndim == 1:
            if mesh.point_data == {}:
                for key, zoneI in mesh.point_sets.items():
                    zones[key] = zoneI
            elif mesh.point_sets == {}:
                for key, zoneI in mesh.point_data.items():
                    zones[key] = zoneI
            else:
                Warning("No point sets in the mesh.")
        
        elif ndim > 1:
            if self.origin == "msh":
                if ndim == 2:
                    zones_array = mesh.cell_data["gmsh:physical"][0]
                elif ndim == 3:
                    zones_array = mesh.cell_data["gmsh:physical"][1]

                for key, value in mesh.field_data.items():
                    if ndim == value[-1]:
                        zones[key] = np.nonzero(zones_array == value[0])[0]

            elif self.origin == "inp":
                for key, value in mesh.cell_sets_dict.items():
                    if key != "All":
                        for inKey, inValue in value.items():
                            if ndim == topological_dimension[inKey]:
                                zones[key + "_" + inKey] = inValue

        return zones
        

    def getFacesCenter(self):
        if self.faceCenter == {}:
            for listI in self.boundFaces:
                x = np.mean(self.points[listI["points"],0], 1)
                y = np.mean(self.points[listI["points"],1], 1)
                z = np.mean(self.points[listI["points"],2], 1)

                self.faceCenter[listI["type"]] = np.array(np.vstack((x, y, z))).T

        try:
            for listI in self.innerFaces:
                x = np.mean(self.points[listI["points"],0], 1)
                y = np.mean(self.points[listI["points"],1], 1)
                z = np.mean(self.points[listI["points"],2], 1)

                self.faceCenter[listI["type"]] = np.array(np.vstack((x, y, z))).T
        except:
            print("Inner faces not defined yet.")


    def getCellsCenter(self):
        for listI in self.cells:
            x = np.mean(self.points[listI["points"],0], 1)
            y = np.mean(self.points[listI["points"],1], 1)
            z = np.mean(self.points[listI["points"],2], 1)

            self.cellCenter[listI["type"]] = np.array(np.vstack((x, y, z))).T


    def cleanPoints(self):
        nodes = np.ones(len(self.points), dtype=bool)

        for k, v in self.pointZones.items():
            if "Constraints" in k:
                nodes[v[0]] = False

        self.pointZones = {k: v for k, v in self.pointZones.items() if "Constraints" not in k}
        self.points = self.points[nodes,:]



    def createInternalFaces(self):
        cellFaces = self.assignCellFaces()
        allFaces = []

        count = 0

        for kOut, vOut in cellFaces.items():
            for _, vIn in vOut.items():
                allFaces.append([count, int(kOut), vIn])
                count += 1

        return 0

    
    def assignCellFaces(self):
        cellFace = {}
        ind = 0

        for elType in self.cells:
            if elType["type"] == "hexahedron":
                of_elem = of_hex
            elif elType["type"] == "tetra":
                of_elem = of_tet
            elif elType["type"] == "wedge":
                of_elem = of_psm
            elif elType["type"] == "pyramid":
                of_elem = of_pyr

            for elem in elType["points"]:
                cellFace[ind] = {}
            
                for k, v in of_elem.items():
                    cellFace[ind][k] = elem[v]
                
                ind += 1

        return cellFace



    def checkFaceOrientations(self):
        pass