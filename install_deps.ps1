# pip.exe 오류(pip-script.py 없음) 시: venv/conda 활성화 후 이 스크립트 실행
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot
python -m ensurepip --upgrade 2>$null
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
Write-Host "Done."
