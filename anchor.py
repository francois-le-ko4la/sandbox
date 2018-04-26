import re

anchor = "ExtractPythonModule.__extract__(self, my_pythonobj, inspectmembers, level=0, decorator=None)"
anchor = re.sub(r"__([a-zA-Z_]*)__\(", r"\1(", anchor)
anchor = re.sub(r"[^\w\- ]+", "", (anchor.replace(' ','-')).lower())
print(anchor)

