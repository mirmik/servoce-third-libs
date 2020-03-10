import sys
import os

listlibs = [
	"TKernel",
	"TKMath",
	"TKG2d",
	"TKG3d",
	"TKBRep",
	"TKGeomBase",
	"TKGeomAlgo",
	"TKTopAlgo",
	"TKPrim",
	"TKBO",
	"TKBool",
	"TKOffset",
	"TKService",
	"TKV3d",
	"TKOpenGl",
	"TKFillet",
	"TKSTL",
	"TKBin",
	"TKShHealing",
	"TKMesh",
	"TKHLR",

	#darwin
	"TKCAF",
	"TKLCAF",
	"TKCDF",
	"TKBinL",
]

for l in listlibs:
	src = "/usr/local/lib/" + "lib" + l + ".dylib"
	tgt = "./osx/" + "lib" + l + ".dylib"
	os.system(f"cp {src} {tgt}")

	src = "/usr/local/lib/" + "lib" + l + ".7.dylib"
	tgt = "./osx/" + "lib" + l + ".7.dylib"
	os.system(f"cp {src} {tgt}")