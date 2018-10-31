Font.parent.windowController().setMasterIndex_(Font.masterIndex - 1)

for master in range(len(Glyphs.font.masters)):
	layer = Glyphs.font.selectedLayers[0] # current layer

	# access all anchors:
	for a in layer.anchors:
        	print a
	
	# add a new anchor
	layer.anchors['top'] = GSAnchor()



	# delete anchor
	# del(layer.anchors['top'])

	# copy anchors from another layer
	#import copy
	#layer.anchors = copy.copy(anotherlayer.anchors)




#MenuTitle: Delete All Components
# -*- coding: utf-8 -*-
__doc__="""
Deletes all components in selected glyphs.
"""

thisFont = Glyphs.font
selectedLayers = thisFont.selectedLayers

def process( thisLayer ):
	if len( thisLayer.components ) > 0:
		listOfComponentNames = ", ".join( [c.componentName for c in thisLayer.components] )
		print "-- Deleted components: %s" % listOfComponentNames
		thisLayer.components = []

for thisLayer in selectedLayers:
	thisGlyph = thisLayer.parent
	print "Processing", thisGlyph.name
	thisGlyph.beginUndo()
	process( thisLayer )
	thisGlyph.endUndo()
