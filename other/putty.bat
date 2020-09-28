@echo off
set var=%1
set extract=%var:~6,-1%
"C:\Program Files\putty\putty.exe" %extract%