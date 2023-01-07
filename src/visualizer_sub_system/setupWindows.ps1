$root = (pwd).Path

while (-not (Test-Path (Join-Path $root ".git")))
{
    $root = (Split-Path $root)
}

Write-Host "Root of repo found at $root"

$venvPath = "$root/venv/scripts/Activate.ps1"

Write-Host "Activating venv in $venvPath"

& $venvPath

Write-Host "Updating pip"

python.exe -m pip install --upgrade pip

$version = python --version
$versionString = (((python --version) -split "\.")[0..1] -join "" -replace "Python", "").Trim()

Write-Host "Using python version $version and seraching for version string of $versionString"

$filesToInstall = Get-ChildItem "$root/src/visualizer/Installers" | Where-Object { $_.Name -like "*$versionString*" }

foreach ($file in $filesToInstall)
{
    python -m pip install $($file.FullName)
}

python -m pip install -r "$root/src/visualizer/Installers/required.txt"