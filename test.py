import table

r = [
   ["Game", "Developer", "Year"],
   ["Terraria", "Re-Logic", 2011],
   ["Minecraft", "Mojang", 2011],
   ["Skyrim", "Bethesda", 2011],
   ["Fallout 4", "Bethesda", 2015]
]

"""Tables

0  --  Default formatting
1  --  No column borders
2  --  No row borders
3  --  More horizontal padding
4  --  Different alignments
5  --  Shorthand alignment (same alignment for all cells in a column)
6  --  New feature, title!
7  --  More vertical padding
"""
tbls = [
   table.table(r),
   table.table(r, colbd=""),
   table.table(r, rowbd=""),
   table.table(r, hpad=5),
   table.table(r, align=[["^", "^", "^"], ["<", "^", ">"], ["<", "^", ">"], ["<", "^", ">"], ["<", "^", ">"]]),
   table.table(r, align=[table.alignment.LEFT, table.alignment.CENTER, table.alignment.RIGHT]),
   table.table(r, title="Favourite Games", talign=table.alignment.RIGHT),
   table.table(r, vpad=3)
]

tbls[0].display()