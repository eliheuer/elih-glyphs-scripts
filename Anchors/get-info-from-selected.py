#MenuTitle: Get info from selected
# -*- coding: utf-8 -*-
__doc__="""
Get anchor info from selected
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

# Do stuff
print("Getting anchor info from selected glyphs:")
thisFont.disableUpdateInterface() # suppresses UI updates in Font View

for thisLayer in listOfSelectedLayers:
    thisGlyph = thisLayer.parent
    print thisGlyph.name,

    allAnchorDict = allAnchorsOfThisGlyph( thisGlyph )
    print(allAnchorDict)

print("Done")

thisFont.enableUpdateInterface() # re-enables UI updates in Font View
