@echo off
cls
echo [GFL MISSION CONTROL] Initiating Triple-Redundancy Sync...
echo.

:: Step 1: Pull any changes made on the web (like the bio/fact sheet)
echo [1/3] Pulling latest updates from GitHub...
git pull origin main

:: Step 2: Commit all local changes (simulations, logs, charts)
echo [2/3] Packaging local R&D assets...
git add .
git commit -m "Auto-sync: %date% %time%"

:: Step 3: Push to both destinations
echo [3/3] Syncing Public and Private vaults...
git push origin main
git push vps main

echo.
echo [SUCCESS] All systems synced. 40-year legacy secured.
pause