@echo off
SET rootdir=PalworldAdminTool

mkdir %rootdir%
mkdir %rootdir%\frontend
mkdir %rootdir%\frontend\templates
mkdir %rootdir%\frontend\templates\auth
mkdir %rootdir%\frontend\templates\pages
mkdir %rootdir%\frontend\static

echo.> %rootdir%\frontend\templates\base.html
echo.> %rootdir%\frontend\templates\auth\login.html
echo.> %rootdir%\frontend\templates\auth\register.html
echo.> %rootdir%\frontend\templates\pages\templatepage.html
echo.> %rootdir%\frontend\static\style.css

mkdir %rootdir%\backend
mkdir %rootdir%\config

echo Directory structure and placeholder files created.
