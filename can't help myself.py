frame1 = r"""
                   
        ___        
   [===/   \--__   
  []          (]   
  []          []   
   []         |/   
[===)              
[][][][]____ ____  
"""

frame2 = r"""
                   
                   
   [========--__   
  []          (]   
  []          []   
   []         []   
[===)         \|   
[][][][]_________  
"""

frame3 = r"""
                   
                   
   [========--__   
  []          (]   
  []          []   
   []          []  
[===)           ___
[][][][]_________  
"""

frame4 = r"""
                   
                   
   [========--__   
  []          (]   
  []          []   
   []          []  
[===)           [] 
[][][][]_________\ 
"""

frame5 = r"""
                   
                   
   [=======--__    
  []         (]    
  []         []    
   []         []   
[===)          []  
[][][][]_______+\  
"""

frame6 = r"""
                   
         __        
   [====/  \__     
  []        (]     
  []        []     
   []        []    
[===)         []   
[][][][]______+\   
"""

frame7 = r"""
                   
       ___         
   [==/   \_       
  []       (]      
  []       []      
   []       []     
[===)        []    
[][][][]_____+|    
"""

frame8 = r"""
                   
      _/\_         
   [=/    \        
  []      (]       
  []      []       
   []      []      
[===)       []     
[][][][]____+|     
"""

frame9 = r"""
                   
      _/\_         
   [=/    \        
  []      (]       
  []      []       
   []     []       
[===)      []      
[][][][]_++/       
"""

frame10 = r"""
       __          
      /  \         
   [=/    \        
  []      (]       
  []      []       
   []     []       
[===)     []       
[][][][]++/        
"""

frame11 = r"""
       /\          
      /  \         
   [=/    \        
  []      (]       
  []      []       
   []    []        
[===)  +[]         
[][][][]/          
"""

frame12 = r"""
       __          
      /  \         
   [=/    \        
  []      (]       
  []      []       
   []     []       
[===)  + []        
[][][][] /         
"""

frame13 = r"""
       ___         
      /   \        
   [=/     \       
  []       (]      
  []       []      
   []      []      
[===)   + []       
[][][][]  /        
"""

frame14 = r"""
         ___       
        /   \      
   [===/     \     
  []         (]    
  []         []    
   []        []    
[===)        /     
[][][][]+          
"""

frame15 = r"""
                   
        ___        
   [===/   \--__   
  []          (]   
  []          []   
   []         /    
[===)         *    
[][][][]+          
"""

frame16 = r"""
                   
      _____        
   [=/     \--__   
  []          (]   
  []          \|   
   []          *   
[===)              
[][][][]+_    *    
"""

frame17 = r"""
                   
      _____        
   [=/     \--__   
  []          (]   
  []          \|   
   []          *   
[===)              
[][][][]__   _+_   
"""

frame18 = r"""
                   
      _____        
   [=/     \--__   
  []          (]   
  []          \|   
   []              
[===)          *   
[][][][]__   ___  
"""

frame19 = r"""
                   
      _____        
   [=/     \--__   
  []          (]   
  []          \|   
   []              
[===)              
[][][][]__   __+_  
"""

frame20 = r"""
                   
      _____        
   [=/     \--__   
  []          (]   
  []          \|   
   []              
[===)              
[][][][]___  ____  
"""

frame21 = r"""
                   
      _____        
   [=/     \--__   
  []          (]   
  []          \|   
   []              
[===)              
[][][][]___  ____  
"""

frame22 = r"""
                   
      _____        
   [=/     \--__   
  []          (]   
  []          \|   
   []              
[===)              
[][][][]____ ____  
"""


import ctypes
import os
import sys
import time


ACCENT = "\033[38;2;220;70;110m"
RESET = "\033[0m"


frames = [
   frame1,
   frame2,
   frame3,
   frame4,
   frame5,
   frame6,
   frame7,
   frame8,
   frame9,
   frame10,
   frame11,
   frame12,
   frame13,
   frame14,
   frame15,
   frame16,
   frame17,
   frame18,
   frame19,
   frame20,
   frame21,
   frame22,
]


def enable_ansi_escape_sequences():
   if os.name != "nt":
      return

   kernel32 = ctypes.windll.kernel32
   handle = kernel32.GetStdHandle(-11)
   mode = ctypes.c_uint()

   if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
      kernel32.SetConsoleMode(handle, mode.value | 0x0004)


def render_frame(frame):
   lines = frame.splitlines()
   bottom_line_index = 0

   for index, line in enumerate(lines):
      if line.strip():
         bottom_line_index = index

   colored_lines = []

   for index, line in enumerate(lines):
      colored_line = line.replace("+", f"{ACCENT}+{RESET}")
      colored_line = colored_line.replace("*", f"{ACCENT}*{RESET}")

      if index == bottom_line_index:
         colored_line = colored_line.replace("_", f"{ACCENT}_{RESET}")

      colored_lines.append(colored_line)

   sys.stdout.write("\033[H")
   sys.stdout.write("\n".join(colored_lines))
   sys.stdout.write("\n\nCan't Help Myself\nAn ASCII Art Rendition\nby dk865")
   sys.stdout.write("\n")
   sys.stdout.flush()


enable_ansi_escape_sequences()


try:
   sys.stdout.write("\033[2J\033[H\033[?25l")
   sys.stdout.flush()

   while True:
      for frame in frames:
         render_frame(frame)
         time.sleep(0.25)
finally:
   sys.stdout.write("\033[?25h")
   sys.stdout.flush()