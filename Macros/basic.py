print(Glyphs.font)
#print Glyphs.font.glyphs

print(" ")
print(Glyphs.font.glyphs["a"]),
print Glyphs.font.glyphs["a"].name,
print Glyphs.font.glyphs["a"].category,
print Glyphs.font.glyphs["a"].subCategory,
print Glyphs.font.glyphs["a"].unicode

print(" ")
glyphname = "b"
print Glyphs.font.glyphs[glyphname].name,
print Glyphs.font.glyphs[glyphname].category,
print Glyphs.font.glyphs[glyphname].subCategory,
print Glyphs.font.glyphs[glyphname].unicode

print(" ")
glyphname = "c"
myGlyph = Glyphs.font.glyphs[glyphname]
print(myGlyph.name),
print(myGlyph.category),
print(myGlyph.subCategory),
print(myGlyph.unicode)

for myGlyph in Glyphs.font.glyphs:
    print myGlyph.name,
    print myGlyph.category,
    print myGlyph.subCategory,
    print myGlyph.unicode
