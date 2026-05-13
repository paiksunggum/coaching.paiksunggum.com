@echo off
REM pip.exe 가 깨졌을 때: conda/venv 활성화 후 이 파일 실행 (python -m pip 사용)
cd /d "%~dp0"
python -m ensurepip --upgrade 2>nul
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
if errorlevel 1 exit /b 1
echo Done.
