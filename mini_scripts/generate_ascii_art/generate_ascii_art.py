"""
Generate ASCII art with art package
"""

# import packages
from art import *

# print codex in 3d fonts 
result = text2art("CODEX", font="3-d")
print("\n",result,"\n")

# print claude in random font
result = text2art("CLAUDE", font="rnd")
print(result,"\n")

# print gemini in random font
result = text2art("GEMINI", font="rnd")
print(result,"\n")

