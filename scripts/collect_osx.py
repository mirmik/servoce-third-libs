import io
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

def darwin_collect(name,tgt):
	import subprocess 

	otool_l = subprocess.Popen(f'otool -L {tgt}', shell=True, stdout=subprocess.PIPE)
	otool_l = io.TextIOWrapper(otool_l.stdout).read()
		
	strs = otool_l.split("\n")
	print(otool_l)

	fstrs = []
	for s in strs:
		if "libTK" in s or "libfreetype" in s:
			fstrs.append(s.strip().split(" ")[0])

	for f in fstrs:
		#filter parasite dirs addition, f.e. last @rpath addition 
		libname = [ l for l in f.split("/") if "dylib" in l ][0]
		cmd = f"install_name_tool -change {f} @rpath/{libname} {tgt}"
		print(cmd)
		os.system(cmd)

ltgt = []
for l in listlibs:
	src = "/usr/local/lib/" + "lib" + l + ".dylib"
	tgt = "./osx/" + "lib" + l + ".dylib"
	os.system(f"cp {src} {tgt}")
	ltgt.append((l,tgt))

	src = "/usr/local/lib/" + "lib" + l + ".7.dylib"
	tgt = "./osx/" + "lib" + l + ".7.dylib"
	os.system(f"cp {src} {tgt}")
	ltgt.append((l,tgt))


for l in ltgt:
	darwin_collect(*l)