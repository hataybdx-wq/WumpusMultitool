@echo off
title Wumpus Multitool - Installation

echo.
echo ================================================
echo        Wumpus Multitool - Installation
echo ================================================
echo.

echo Installation des dépendances...
pip install pystyle colorama requests selenium undetected-chromedriver Pillow aiohttp psutil websockets

echo.
echo Installation terminée !
echo.
pause
