#MenuTitle: Get info from selected
# -*- coding: utf-8 -*-
__doc__="""
Get info from selected
"""

thisFont = Glyphs.font  # Active font
thisFontMaster = thisFont.selectedFontMaster  # Active master
listOfSelectedLayers = thisFont.selectedLayers  # Active layers of selected glyphs

def allAnchorsOfThisGlyph( thisGlyph ):
    anchorDict = {}
    for thisLayer in thisGlyph.layers:
        thisWidth = thisLayer.width 
        allAnchors = [a for a in thisLayer.anchors]
        if thisWidth == 0:
            thisWidth = 1
        for thisAnchor in allAnchors:
            thisAnchorInfo = ( thisAnchor.name, thisAnchor.x, thisAnchor.y )
        if not thisAnchor.name in anchorDict.keys():
            anchorDict[thisAnchor.name] = [ thisAnchorInfo ]
        else:
            anchorDict[thisAnchor.name].append( thisAnchorInfo )
    return anchorDict

def addAnchor( thisGlyph )
    anchorsAdded = []
    thisWidth = thisLayer.width
    newAnchorPosition = averagePosition( allAnchorDict[newAnchorName], thisWidth )
    newAnchor = GSAnchor()
    newAnchor.name = top
    newAnchor.position = NSPoint(400, 600)
    thisLayer.addAnchor_( newAnchor )
    anchorsAdded.append( newAnchorName )
    reportString += "  %s: %s\n" % ( thisLayer.name, ", ".join(anchorsAdded) )
    print reportString

# Do stuff
print(" ")
print("Getting anchor info from selected glyphs ###############")
print(" ")
thisFont.disableUpdateInterface() # suppresses UI updates in Font View

for thisLayer in listOfSelectedLayers:
    thisGlyph = thisLayer.parent
    print thisGlyph.name,

    allAnchorDict = allAnchorsOfThisGlyph( thisGlyph )
    print(allAnchorDict)

    thisGlyph.beginUndo() # begin undo grouping
    addAnchor(thisGlyph)
    thisGlyph.endUndo()   # end undo grouping

print(" ")
print("Done ###################################################")
print(" ")

thisFont.enableUpdateInterface() # re-enables UI updates in Font View
