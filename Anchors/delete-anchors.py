#MenuTitle: Delete Anchors
# -*- coding: utf-8 -*-
__doc__=
"""
Delete anchors in selected glyphs.
"""

myFont = Glyphs.font
selectedLayers = myFont.selectedLayers

for myLayer in selectedLayers:
    myGlyph = myLayer.parent
    print("-- %s" % myGlyph.name)
    myGlyph.beginUndo()
    myLayer.setAnchors_( None )
    myGlyph.endUndo()
    print("Done! :-)")
