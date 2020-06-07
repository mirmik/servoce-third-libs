// Created on: 1995-12-06
// Created by: Jacques GOUSSARD
// Copyright (c) 1995-1999 Matra Datavision
// Copyright (c) 1999-2014 OPEN CASCADE SAS
//
// This file is part of Open CASCADE Technology software library.
//
// This library is free software; you can redistribute it and/or modify it under
// the terms of the GNU Lesser General Public License version 2.1 as published
// by the Free Software Foundation, with special exception defined in the file
// OCCT_LGPL_EXCEPTION.txt. Consult the file LICENSE_LGPL_21.txt included in OCCT
// distribution for complete text of the license and disclaimer of any warranty.
//
// Alternatively, this file may be used under the terms of Open CASCADE
// commercial license or contractual agreement.

#ifndef BRepCheck_DataMapOfShapeListOfStatus_HeaderFile
#define BRepCheck_DataMapOfShapeListOfStatus_HeaderFile

#include <TopoDS_Shape.hxx>
#include <BRepCheck_ListOfStatus.hxx>
#include <TopTools_ShapeMapHasher.hxx>
#include <NCollection_DataMap.hxx>

typedef NCollection_DataMap<TopoDS_Shape,BRepCheck_ListOfStatus,TopTools_ShapeMapHasher> BRepCheck_DataMapOfShapeListOfStatus;
typedef NCollection_DataMap<TopoDS_Shape,BRepCheck_ListOfStatus,TopTools_ShapeMapHasher>::Iterator BRepCheck_DataMapIteratorOfDataMapOfShapeListOfStatus;


#endif
