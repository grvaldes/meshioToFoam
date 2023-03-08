import numpy as np

topological_dimension = {
    "line": 1,
    "polygon": 2,
    "triangle": 2,
    "quad": 2,
    "tetra": 3,
    "hexahedron": 3,
    "wedge": 3,
    "pyramid": 3,
    "line3": 1,
    "triangle6": 2,
    "quad9": 2,
    "tetra10": 3,
    "hexahedron27": 3,
    "wedge18": 3,
    "pyramid14": 3,
    "vertex": 0,
    "quad8": 2,
    "hexahedron20": 3,
    "triangle10": 2,
    "triangle15": 2,
    "triangle21": 2,
    "line4": 1,
    "line5": 1,
    "line6": 1,
    "tetra20": 3,
    "tetra35": 3,
    "tetra56": 3,
    "quad16": 2,
    "quad25": 2,
    "quad36": 2,
    "triangle28": 2,
    "triangle36": 2,
    "triangle45": 2,
    "triangle55": 2,
    "triangle66": 2,
    "quad49": 2,
    "quad64": 2,
    "quad81": 2,
    "quad100": 2,
    "quad121": 2,
    "line7": 1,
    "line8": 1,
    "line9": 1,
    "line10": 1,
    "line11": 1,
    "tetra84": 3,
    "tetra120": 3,
    "tetra165": 3,
    "tetra220": 3,
    "tetra286": 3,
    "wedge40": 3,
    "wedge75": 3,
    "hexahedron64": 3,
    "hexahedron125": 3,
    "hexahedron216": 3,
    "hexahedron343": 3,
    "hexahedron512": 3,
    "hexahedron729": 3,
    "hexahedron1000": 3,
    "wedge126": 3,
    "wedge196": 3,
    "wedge288": 3,
    "wedge405": 3,
    "wedge550": 3,
    "VTK_LAGRANGE_CURVE": 1,
    "VTK_LAGRANGE_TRIANGLE": 2,
    "VTK_LAGRANGE_QUADRILATERAL": 2,
    "VTK_LAGRANGE_TETRAHEDRON": 3,
    "VTK_LAGRANGE_HEXAHEDRON": 3,
    "VTK_LAGRANGE_WEDGE": 3,
    "VTK_LAGRANGE_PYRAMID": 3,
}


class polyMesh:

    def __init__(self, mesh, fileType):
        self.origin = fileType
        self.points = mesh.points
        self.boundFaces = self.getCellsFromMeshio(mesh, 2)
        self.cells = self.getCellsFromMeshio(mesh, 3)
        self.pointZones = self.getZonesFromMeshio(mesh, 1)
        self.faceZones = self.getZonesFromMeshio(mesh, 2)
        self.cellZones = self.getZonesFromMeshio(mesh, 3)

        self.faceCenter = {}
        self.cellCenter = {}

        self.getFacesCenter()
        self.getCellsCenters()

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
                dict = {}
                dict["type"] = cellI.type
                dict["nPts"] = cellI.data.shape[-1]
                dict["points"] = cellI.data

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

    def getCellsCenters(self):
        for listI in self.cells:
            x = np.mean(self.points[listI["points"],0], 1)
            y = np.mean(self.points[listI["points"],1], 1)
            z = np.mean(self.points[listI["points"],2], 1)

            self.cellCenter[listI["type"]] = np.array(np.vstack((x, y, z))).T

    def createInternalFaces(self):
        pass

    def checkFaceOrientations(self):
        pass