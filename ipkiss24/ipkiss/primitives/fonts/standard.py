# IPKISS - Parametric Design Framework
# Copyright (C) 2002-2012  Ghent University - imec
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
# 
# i-depot BBIE 7396, 7556, 7748
# 
# Contact: ipkiss@intec.ugent.be

from .. import font as _font


#----------------------------------------------------------------------------
#Standard Path Alphabet
#----------------------------------------------------------------------------

TEXT_FONT_STANDARD = _font.PathFont()
TEXT_FONT_STANDARD.ID = 0
TEXT_FONT_STANDARD.cell_size = (0.6, 1.0)
TEXT_FONT_STANDARD.spacing = 0.2
TEXT_FONT_STANDARD.line_width = 0.1
TEXT_FONT_STANDARD.default_char = [(0.0,0.2), (0.0,0.8), (0.6,0.8), (0.6,0.2), (0.0,0.2), (0.0,0.8)]
TEXT_FONT_STANDARD.coords = {
    'A' : [[(0.0,0.0), (0.0,0.8), (0.2,1.0), (0.4,1.0), (0.6,0.8), (0.6,0.0)], [(0.6,0.5), (0.0,0.5)], [(-0.1,0.0),(0.1,0.0)], [(0.5,0.0),(0.7,0.0)]],
    'B' : [[(0.0,0.0), (0.0,1.0)],[(-0.1,1.0), (0.5,1.0), (0.5,0.5), (0.6,0.5), (0.6, 0.0), (-0.1,0.0)], [(0.0,0.5), (0.6,0.5)]],
    'C' : [[(0.6,0.1), (0.6,0.0), (0.1,0.0), (0.0,0.1), (0.0,0.9), (0.1,1.0), (0.6, 1.0), (0.6,0.9)]],
    'D' : [[(0.0,0.0), (0.0,1.0)], [(-0.1,1.0),(0.4,1.0), (0.6,0.8), (0.6,0.2), (0.4,0.0), (-0.1,0.0)]],
    'E' : [[(0.6,0.1), (0.6,0.0), (0.0,0.0), (0.0,1.0), (0.6,1.0), (0.6,0.9)], [(0.0,0.5), (0.4,0.5)], [(0.4,0.4),(0.4,0.6)]],
    'F' : [[(0.0,0.0), (0.0,1.0), (0.6,1.0), (0.6, 0.9)], [(0.0,0.5), (0.4,0.5)], [(-0.1,0.0),(0.1,0.0)], [(0.4,0.4),(0.4,0.6)]],
    'G' : [[(0.3,0.4), (0.3,0.5), (0.6,0.5), (0.6,0.1), (0.5,0.0), (0.1,0.0), (0.0,0.1), (0.0,0.9), (0.1,1.0), (0.6,1.0), (0.6,0.9)]],
    'H' : [[(0.0,0.0), (0.0,1.0)], [(0.0,0.5), (0.6,0.5)], [(0.6,1.0), (0.6,0.0)], [(-0.1,0.0),(0.1,0.0)], [(0.5,0.0),(0.7,0.0)], [(-0.1,1.0),(0.1,1.0)], [(0.5,1.0),(0.7,1.0)]],
    'I' : [[(0.1,0.0), (0.5,0.0)], [(0.3,0.0), (0.3,1.0)], [(0.1,1.0), (0.5,1.0)]],
    'J' : [[(0.0,0.1), (0.1,0.0), (0.3,0.0), (0.4,0.1), (0.4,1.0)], [(0.2,1.0), (0.6,1.0)]],
    'K' : [[(0.0,0.0), (0.0,1.0)], [(0.0,0.5), (0.1,0.5), (0.6,1.0)], [(0.1,0.5), (0.6,0.0)], [(-0.1,0.0),(0.1,0.0)], [(0.5,0.0),(0.7,0.0)], [(-0.1,1.0),(0.1,1.0)], [(0.5,1.0),(0.7,1.0)]],
    'L' : [[(0.6,0.1), (0.6,0.0), (0.0,0.0), (0.0,1.0)], [(-0.1,1.0), (0.1,1.0)]],
    'M' : [[(0.0,0.0), (0.0,1.0)],[(-0.1,1.0), (0.1, 1.0), (0.3,0.8), (0.5, 1.0), (0.7,1.0)], [(0.6,1.0), (0.6,0.0)], [(-0.1,0.0),(0.1,0.0)], [(0.5,0.0),(0.7,0.0)]],
    'N' : [[(0.0,0.0), (0.0,1.0)],[(-0.1,1.0), (0.1, 1.0), (0.5,0.6), (0.6,0.6)], [(0.6,1.0), (0.6,0.0)], [(-0.1,0.0),(0.1,0.0)], [(0.5,0.0),(0.7,0.0)], [(0.5,1.0),(0.7,1.0)]],
    'O' : [[(0.0,0.2), (0.0,0.8), (0.2,1.0), (0.4,1.0), (0.6,0.8), (0.6,0.4)], [(0.6,0.5), (0.6,0.2), (0.4,0.0), (0.2,0.0), (0.0, 0.2), (0.0,0.8)]],
    'P' : [[(0.0,0.0), (0.0,1.0)],[ (-0.1, 1.0), (0.5,1.0), (0.6,0.9), (0.6,0.5), (0.5,0.4), (0.0,0.4)], [(-0.1,0.0),(0.1,0.0)]],
    'Q' : [[(0.0,0.2), (0.0,0.8), (0.2,1.0), (0.4,1.0), (0.6,0.8), (0.6,0.2), (0.4,0.0), (0.2,0.0), (0.0, 0.2)], [(0.4,0.2), (0.6,0.0)]],
    'R' : [[(0.0,0.0), (0.0,1.0)],[ (-0.1, 1.0), (0.5,1.0), (0.6,0.9), (0.6,0.5), (0.5,0.4), (0.0,0.4)], [(0.4,0.4), (0.4,0.3), (0.6, 0.1), (0.6,0.0)], [(-0.1,0.0),(0.1,0.0)], [(0.5,0.0),(0.7,0.0)]],
    'S' : [[(0.0,0.1), (0.0,0.0), (0.5,0.0), (0.6,0.1), (0.6,0.4), (0.5,0.5), (0.1,0.5), (0.0,0.6), (0.0,0.9), (0.1,1.0), (0.6,1.0), (0.6,0.9)]],
    'T' : [[(0.3,0.0), (0.3,1.0)], [(0.0,0.9), (0.0,1.0), (0.6,1.0), (0.6,0.9)],[(0.2,0.0), (0.4,0.0)]],
    'U' : [[(0.0,1.0), (0.0,0.1), (0.1,0.0), (0.5,0.0), (0.6,0.1), (0.6,1.0)], [(-0.1,1.0),(0.1,1.0)], [(0.5,1.0),(0.7,1.0)]],
    'V' : [[(0.0,1.0), (0.0,0.3), (0.3,0.0), (0.6,0.3), (0.6,1.0)], [(-0.1,1.0),(0.1,1.0)], [(0.5,1.0),(0.7,1.0)]],
    'W' : [[(0.0,1.0), (0.0,0.1), (0.1,0.0), (0.3,0.2), (0.5,0.0), (0.6,0.1), (0.6,1.0)], [(-0.1,1.0),(0.1,1.0)], [(0.5,1.0),(0.7,1.0)]],
    'X' : [[(0.0,0.0), (0.0,0.2), (0.6,0.8), (0.6,1.0)], [(0.0,1.0), (0.0,0.8), (0.6,0.2), (0.6,0.0)], [(-0.1,0.0),(0.1,0.0)], [(0.5,0.0),(0.7,0.0)], [(-0.1,1.0),(0.1,1.0)], [(0.5,1.0),(0.7,1.0)]],
    'Y' : [[(0.3,0.0), (0.3,0.5), (0.0,0.8), (0.0,1.0)], [(0.3,0.5), (0.6,0.8), (0.6,1.0)], [(0.2,0.0), (0.4,0.0)], [(-0.1,1.0),(0.1,1.0)], [(0.5,1.0),(0.7,1.0)]],
    'Z' : [[(0.0,0.9), (0.0,1.0), (0.6,1.0), (0.6,0.8), (0.0,0.2), (0.0,0.0), (0.6,0.0), (0.6,0.1)]],
    '0' : [[(0.3,0.0), (0.2,0.0), (0.0,0.2), (0.0,0.8), (0.2,1.0), (0.4,1.0), (0.6,0.8), (0.6,0.4)], [(0.6,0.5), (0.6,0.2), (0.4,0.0), (0.2,0.0), (0.0,0.2), (0.0, 0.5)], [(0.1, 0.1), (0.3, 0.3), (0.3, 0.7), (0.5,0.9)]],
    '1' : [[(0.1,0.7), (0.4,1.0), (0.5,1.0), (0.5,0.0)],[(0.4,0.0), (0.6,0.0)]],
    '2' : [[(0.0,0.9), (0.1,1.0), (0.5,1.0), (0.6,0.9), (0.6,0.7), (0.0,0.1), (0.0,0.0), (0.6,0.0), (0.6,0.1)]],
    '3' : [[(0.0,0.9), (0.1,1.0), (0.5,1.0), (0.6,0.9), (0.6,0.6), (0.5,0.5), (0.3,0.5)], [(0.5,0.5), (0.6,0.4), (0.6,0.1), (0.5,0.0), (0.1,0.0), (0.0,0.1)]],
    '4' : [[(0.1,1.0), (0.0,1.0), (0.0,0.4), (0.6,0.4)], [(0.4,0.6), (0.4,0.0)], [(0.3,0.0),(0.5,0.0)]],
    '5' : [[(0.6,0.9), (0.6,1.0), (0.0,1.0), (0.0,0.6), (0.4,0.6), (0.6,0.4), (0.6,0.1), (0.5,0.0), (0.1,0.0), (0.0,0.1)]],
    '6' : [[(0.0,0.5), (0.5,0.5), (0.6,0.4), (0.6,0.1), (0.5,0.0), (0.2,0.0)], [(0.3,0.0), (0.1, 0.0), (0.0,0.1), (0.0,0.8), (0.2,1.0), (0.4,1.0), (0.6,0.8)]],
    '7' : [[(0.0,0.9), (0.0,1.0), (0.6,1.0), (0.6,0.8), (0.3,0.5), (0.3,0.0)],[(0.2,0.0), (0.4,0.0)]],
    '8' : [[(0.1,0.5), (0.0,0.6), (0.0,0.8), (0.2,1.0), (0.4,1.0), (0.6,0.8), (0.6,0.6), (0.5,0.5),(0.2,0.5)], [(0.4,0.5), (0.1,0.5), (0.0,0.4), (0.0,0.1), (0.1,0.0), (0.3,0.0)], [(0.2,0.0), (0.5,0.0), (0.6,0.1), (0.6,0.4), (0.5,0.5)]],
    '9' : [[(0.6,0.4), (0.1,0.4), (0.0,0.5), (0.0,0.9), (0.1,1.0), (0.3,1.0)], [(0.2,1.0), (0.5,1.0), (0.6,0.9), (0.6,0.1), (0.5,0.0), (0.1,0.0), (0.0,0.1), (0.0,0.2)]],				   '.' : [[(0.25,0.0), (0.35,0.0)]],
    ',' : [[(0.15,-0.2),(0.35,0.0)]],
    '(' : [[(0.4,1.0), (0.2,0.8), (0.2,0.2), (0.4,0.0)]],
    ')' : [[(0.2,1.0), (0.4,0.8), (0.4,0.2), (0.2,0.0)]],
    '[' : [[(0.4,1.0), (0.2,1.0), (0.2,0.0), (0.4,0.0)]],
    ']' : [[(0.2,1.0), (0.4,1.0), (0.4,0.0), (0.2,0.0)]],
    '#' : [[(0.0,0.6), (0.6,0.6)], [(0.6,0.3), (0.0,0.3)], [(0.15,0.1), (0.15,0.8)],  [(0.45,0.8), (0.45,0.1)]],
    '%' : [[(0.0,1.0), (0.2,1.0), (0.2,0.8), (0.0,0.8), (0.0,1.0), (0.2,1.0)], [(0.0,0.2), (0.6,0.8)], [(0.4,0.2), (0.6,0.2), (0.6,0.0), (0.4,0.0), (0.4,0.2), (0.6,0.2)]],
    '$' : [[(0.0,0.2), (0.1,0.1), (0.5,0.1), (0.6,0.2), (0.6,0.4), (0.5,0.5), (0.1,0.5), (0.0,0.6), (0.0,0.8), (0.1,0.9), (0.5,0.9), (0.6,0.8)], [(0.3, -0.1), (0.3,1.1)]],
    '*' : [[(0.0,0.5), (0.6,0.5)], [(0.1,0.8), (0.3, 0.6), (0.3,0.4), (0.5, 0.2)], [(0.1,0.2), (0.3, 0.4)], [(0.3,0.6), (0.5, 0.8)]],
    ':' : [[(0.25,0.0), (0.35,0.0)], [(0.25,0.4), (0.35,0.4)]],
    ';' : [[(0.15,-0.2), (0.35,0.0)], [(0.25,0.4), (0.35,0.4)]],
    '!' : [[(0.25,0.0), (0.35,0.0)], [(0.3,1.0), (0.3,0.3)]],
    '?' : [[(0.25,0.0), (0.35,0.0)], [(0.0,0.8),(0.0,0.9), (0.1,1.0), (0.4,1.0), (0.5,0.9), (0.5,0.7), (0.3,0.5), (0.3,0.3)]],
    '/' : [[(0.0,0.0), (0.0,0.2), (0.6,0.8), (0.6,1.0)]],
    '\\': [[(0.0,1.0), (0.0,0.8), (0.6,0.2), (0.6,0.0)]],
    '-' : [[(0.1,0.5), (0.5,0.5)]],
    '_' : [[(0.0,0.0), (0.6,0.0)]],
    '+' : [[(0.1,0.5), (0.5,0.5)], [(0.3,0.3), (0.3, 0.7)]],
    '=' : [[(0.1,0.4), (0.5,0.4)], [(0.1,0.6), (0.5,0.6)]],
    '{' : [[(0.4,1.0), (0.3,0.9), (0.3,0.6), (0.2,0.5), (0.3,0.4), (0.3, 0.1), (0.4,0.0)]],
    '}' : [[(0.2,1.0), (0.3,0.9), (0.3,0.6), (0.4,0.5), (0.3,0.4), (0.3, 0.1), (0.2,0.0)]],
    '<' : [[(0.5,0.0), (0.1,0.4), (0.5,0.8)]],
    '>' : [[(0.1,0.0), (0.5,0.4), (0.1,0.8)]],
    '`' : [[(0.3,1.2), (0.3,0.7)]],
    '\"': [[(0.1,1.2),(0.2,0.8)],[(0.3,1.2),(0.4,0.8)]],
    '^' : [[(0.05, 0.8), (0.25, 1.0), (0.35, 1.0), (0.55,0.8)]],
    ' ' : []
}
