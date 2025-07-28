# EDUCATIONAL PURPOSES !!

# iptracker

To run this IP tracker, start the Flask server with `python app.py`, then expose it publicly using `./cloudflared.exe tunnel --url http://localhost:5000`.
add cloudflare file to that folder


phxsxng link that knows others ip


other:

@echo off
title IP Logger - Flask + LocalXpose

echo Starting Flask server...
start cmd /k "python app.py"

timeout /t 3 >nul

echo Starting LocalXpose tunnel...
start cmd /k "loclx tunnel http --to 5000"

echo Done!
