echo off
set tmp=%~dp0\tmp
set res=%localappdata%\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets
echo Store image Temporary directory %tmp%

for %%i in ( %tmp% ) do  if not exist %%i md %%i

for /f "delims=" %%b in ('dir /a-d /b /s %res%') do (
    if %%~zb GTR 409600 xcopy %%b %tmp%
)

ren %tmp%\* *.jpg
echo Select Picture
start /w %tmp%
exit