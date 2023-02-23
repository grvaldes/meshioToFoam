import numpy as np

def writePointsFile(mesh, filename):
    with open(filename + "/constant/polyMesh/points","w") as writer:
        writer.write(writeBanner())
        writer.write(writeFoamFile("vectorField","constant/polyMesh","points"))
        writer.write(writeBreak(1))
        writer.write("\n\n")

        writer.write(f"{np.size(mesh.points,0)}\n(\n")

        for line in mesh.points:
            writer.write(f"({line[0]} {line[1]} {line[2]})\n")

        writer.write(")\n")
        writer.write("\n\n")
        writer.write(writeBreak(2))


def writeBoundaryFile(mesh, filename):
    with open(filename + "/constant/polyMesh/boundary","w") as writer:
        writer.write(writeBanner())
        writer.write(writeFoamFile("polyBoundaryMesh","constant/polyMesh","boundary"))
        writer.write(writeBreak(1))
        writer.write("\n\n")

        n_bound = 0
        n_keys = {}

        for key, value in mesh.field_data.items():
            if value[-1] == 2:
                n_bound += 1
                n_keys[key] = value[0]

        writer.write(f"{n_bound}\n(\n")

        for key, value in n_keys.items():
            writer.write(f"\t{key}\n".expandtabs(4))
            writer.write("\t{\n".expandtabs(4))
            writer.write("\t\ttype\t\t\tpatch;\n".expandtabs(4))
            writer.write("\t\tphysicalType\tpatch;\n".expandtabs(4))
            writer.write(f"\t\tnFaces\t\t\t{value};\n".expandtabs(4))
            writer.write(f"\t\tstartFace\t\t{value};\n".expandtabs(4))
            writer.write("\t}\n".expandtabs(4))

        writer.write(")\n")
        writer.write("\n\n")
        writer.write(writeBreak(2))


def writeBanner(OF_version = 8):
    banner = ("/*--------------------------------*- C++ -*----------------------------------*\ \n" + 
     "  =========                 | \n" +
     "  \\\\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox \n" +
     "   \\\\    /   O peration     | Website:  https://openfoam.org \n" +
    f"    \\\\  /    A nd           | Version:  {OF_version} \n" +
     "     \\\\/     M anipulation  | Generated with meshioToFoam\n" +
     "\*---------------------------------------------------------------------------*/\n")

    return banner


def writeBreak(i):
    if i == 1:
        brk = "// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n"
    elif i == 2:
        brk = "// ************************************************************************* //"

    return brk


def writeFoamFile(foamClass, location, object, version = 2.0, format = "ascii"):
    foamFile = ("FoamFile\n" +
        "{\n" +
        f"\tversion\t\t{version};\n".expandtabs(4) +
        f"\tformat\t\t{format};\n".expandtabs(4) +
        f"\tclass\t\t{foamClass};\n".expandtabs(4) +
        f"\tlocation\t\"{location}\";\n".expandtabs(4) +
        f"\tobject\t\t{object};\n".expandtabs(4) +
        "}\n")

    return foamFile