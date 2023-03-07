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


class polyBlock:
    def __init__(self ,cell_type, data):
        self.type = cell_type
        self.data = np.asarray(data)
        self.dim = topological_dimension[cell_type]

        if topological_dimension[cell_type] == 1:
            self.elem = "lines"
        if topological_dimension[cell_type] == 2:
            self.elem = "faces"
        if topological_dimension[cell_type] == 3:
            self.elem = "cells"

    def __repr__(self):
        items = [
            "OpenFOAM polyBlock",
            f"type: {self.type}",
            f"num {self.elem}: {len(self.data)}"
        ]
        return "<" + ", ".join(items) + ">"

    def __len__(self):
        return len(self.data)


class polyMesh:

    def __init__(self, mesh, fileType):
        self.origin = fileType
        self.points = mesh.points
        self.cells = self.getCellsFromMeshio(mesh, 3)
        self.faces = self.getCellsFromMeshio(mesh, 2)
        self.pointZones = self.getZonesFromMeshio(mesh, 1)
        self.faceZones = self.getZonesFromMeshio(mesh, 2)
        self.cellZones = self.getZonesFromMeshio(mesh, 3)

        self.createInternalFaces()

        self.neighbour = 0
        self.owner = 0
        self.boundary = 0

        self.faceArea = 0
        self.faceCenter = 0
        self.cellVolume = 0
        self.cellCenter = 0

    
    def getCellsFromMeshio(mesh, ndim):
        cells = []

        for cellI in mesh.cells:
            if ndim == topological_dimension[cellI.type]:
                cells.append(mesh.data) 

        return cells

    
    def getZonesFromMeshio(mesh, ndim):
        zones = {}

        if ndim == 1:
            if mesh.point_data == {}:
                for key, zoneI in mesh.point_sets:
                    zones[key] = zoneI
            elif mesh.point_sets == {}:
                for key, zoneI in mesh.point_data:
                    zones[key] = zoneI
        elif ndim == 2:
            if mesh.cell_data == {}:
                for key, zoneI in mesh.cell_sets:
                    zones[key] = zoneI
            elif mesh.cell_sets == {}:
                for key, zoneI in mesh.cell_data:
                    zones[key] = zoneI

        return zones
        
    def createInternalFaces():
        pass

    def checkFaceOrientations():
        pass
