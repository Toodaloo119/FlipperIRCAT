:loop
    for /d %%D in (%1\*) do (move "%%D\*" %1\ && rmdir "%%D")
    SHIFT
    set PARAMS=%1
if not %PARAMS%!==! goto loop