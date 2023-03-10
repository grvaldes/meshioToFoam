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

abaqus_tet = {
    "face1": np.array([0, 1, 2]),
    "face2": np.array([0, 3, 1]),
    "face3": np.array([1, 3, 2]),
    "face4": np.array([2, 3, 0])
}
abaqus_hex = {
    "face1": np.array([0, 1, 2, 3]),
    "face2": np.array([4, 7, 6, 5]),
    "face3": np.array([0, 4, 5, 1]),
    "face4": np.array([1, 5, 6, 2]),
    "face5": np.array([2, 6, 7, 3]),
    "face6": np.array([3, 7, 4, 0])
}
abaqus_psm = {
    "face1": np.array([0, 1, 2]),
    "face2": np.array([3, 5, 4]),
    "face3": np.array([0, 3, 4, 1]),
    "face4": np.array([1, 4, 5, 2]),
    "face5": np.array([2, 5, 4, 1])
}

of_tet = {
    "face1": np.array([1, 2, 3]),
    "face2": np.array([2, 0, 3]),
    "face3": np.array([0, 1, 3]),
    "face4": np.array([1, 0, 2])
}
of_hex = {
    "face1": np.array([0, 4, 7, 3]),
    "face2": np.array([1, 2, 6, 5]),
    "face3": np.array([0, 1, 5, 4]),
    "face4": np.array([2, 3, 7, 6]),
    "face5": np.array([0, 3, 2, 1]),
    "face6": np.array([4 ,5 ,6 ,7])
}
of_psm = {
    "face1": np.array([0, 2, 1]),
    "face2": np.array([3 ,4, 5]),
    "face3": np.array([0, 3, 5, 2]),
    "face4": np.array([1, 2, 5 ,4]),
    "face5": np.array([0, 1, 4, 3])
}
of_pyr = {
    "face1": np.array([0, 3, 2, 1]),
    "face2": np.array([0, 4, 3]),
    "face3": np.array([2, 3, 4]),
    "face4": np.array([1, 2, 4]),
    "face5": np.array([0, 1, 4])
}
of_wdg = {
    "face1": np.array([0, 2, 1]),
    "face2": np.array([3, 4, 5, 6]),
    "face3": np.array([0, 3, 6]),
    "face4": np.array([1, 2, 5, 4]),
    "face5": np.array([0, 1, 4, 3]),
    "face6": np.array([0, 6, 5, 2])
}
of_twg = {
    "face1": np.array([0, 2, 1]),
    "face2": np.array([0, 1, 3]),
    "face3": np.array([0, 3, 4, 2]),
    "face4": np.array([1, 3, 4, 3])
}