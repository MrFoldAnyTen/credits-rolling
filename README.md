# credits-rolling
git clone https://github.com/MrFoldAnyTen/credits-rolling.git
git add -A
git push

import os, sys; sys.path.append(os.path.dirname(bpy.data.filepath)); import texture_painter
import importlib; importlib.reload(texture_painter); texture_painter.go()
