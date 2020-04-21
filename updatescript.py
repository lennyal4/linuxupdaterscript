from bash import bash
from consolemenu import *

whats_gonna_be_updated=input("put what you want installed on your system:")
x=bash('sudo dnf install -y '+whats_gonna_be_updated)
print(x)