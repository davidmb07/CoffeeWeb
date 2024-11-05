# Script para activar el entorno virtual
$venvPath = ".\venv\Scripts\Activate.ps1"
if (Test-Path $venvPath) {
    & $venvPath
}