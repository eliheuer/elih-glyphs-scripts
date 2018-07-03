#MenuTitle: Add new anchors to selected glyphs
# -*- coding: utf-8 -*-
__doc__="""
Add new anchors to selected glyphs
"""

thisFont = Glyphs.font  # Active font
thisFontMaster = thisFont.selectedFontMaster  # Active master
listOfSelectedLayers = thisFont.selectedLayers  # Active layers of selected glyphs

def addAnchor( thisGlyph ):
    anchorsAdded = []
    thisWidth = thisLayer.width
    newAnchor = GSAnchor()
    newAnchor.name = "top"
    newAnchor.position = NSPoint(400, 600)
    thisLayer.addAnchor_( newAnchor )
    anchorsAdded.append( newAnchor.name )
    print anchorsAdded

# Do stuff
thisFont.disableUpdateInterface() # suppresses UI updates in Font View

for thisLayer in listOfSelectedLayers:
    thisGlyph = thisLayer.parent
    print thisGlyph.name,
    thisGlyph.beginUndo() # begin undo grouping
    addAnchor(thisGlyph)
    thisGlyph.endUndo()   # end undo grouping

thisFont.enableUpdateInterface() # re-enables UI updates in Font View
