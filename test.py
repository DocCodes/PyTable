import table

r = [
   ["Game", "Developer", "Year"],
   ["Terraria", "Re-Logic", 2011],
   ["Minecraft", "Mojang", 2011],
   ["Skyrim", "Bethesda", 2011],
   ["Fallout 4", "Bethesda", 2015]
]
t = table.table(r)

t.display()