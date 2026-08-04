$ErrorActionPreference = 'Stop'
$script = $MyInvocation.MyCommand.Name

Write-Host "${script}: Creating virtual environment..."
py -3 -m venv .env

Write-Host "${script}: Entering virtual env..."
. .\.env\Scripts\Activate.ps1

Write-Host "${script}: Installing wiki dependencies..."
pip install -r requirements.txt

Write-Host "${script}: Setup complete`n"
Write-Host "${script}: To start the wiki server, run:"
Write-Host "${script}:   '.\.env\Scripts\Activate.ps1'"
Write-Host "${script}:   'zensical serve'"

