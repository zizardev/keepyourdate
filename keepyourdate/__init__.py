"""
KeepYourDate@ 2024 ZizaR
"""
from .check import Check
from .edit import Edit

check = Check()
edit = Edit()

add = edit.add
delete = edit.delete

today = check.today
now = check.now
history = check.history
archive = check.archive