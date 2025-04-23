$projectRoot = $PSScriptRoot

. "$projectRoot\venv\Scripts\activate.ps1"

if ($env:VIRTUAL_ENV) {
    $scanPath = "D:\Eltex\logs"
    $logPath = "C:\Users\Admin\Logs\clean.log"

    python "$projectRoot\scripts\base_checker.py" $scanPath $logPath
} else {
    Write-Error "Не удалось активировать виртуальную среду. Проверьте директорию venv."
    exit 1
}
