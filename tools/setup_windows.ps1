$ErrorActionPreference = 'Stop'

$Root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
Set-Location $Root

$Python = Join-Path $Root '.venv\Scripts\python.exe'
$Cfg = Join-Path $Root '.venv\pyvenv.cfg'

function Test-SupportedPython {
    param([string]$Exe, [string[]]$Arguments = @())
    try {
        $out = & $Exe @Arguments --version 2>&1
    } catch { return $false }
    $m = [regex]::Match(($out -join ' '), 'Python (\d+)\.(\d+)')
    if (-not $m.Success) { return $false }
    $major = [int]$m.Groups[1].Value
    $minor = [int]$m.Groups[2].Value
    Write-Host ("{0} {1} -> Python {2}.{3}" -f $Exe, ($Arguments -join ' '), $major, $minor)
    return ($major -eq 3 -and $minor -ge 12 -and $minor -le 14)
}

# A virtualenv is machine-local. Delete copied/stale Linux or another-PC envs.
if (Test-Path $Cfg) {
    $cfgText = Get-Content $Cfg -Raw
    if ($cfgText -match '/usr/bin|/home/' -or -not (Test-Path $Python)) {
        Write-Host 'Removing stale/non-Windows .venv ...'
        Remove-Item (Join-Path $Root '.venv') -Recurse -Force
    }
}

# Python 3.15 has no slipcover/litellm wheels: rebuild with a supported version.
if (Test-Path $Python) {
    $existing = & $Python --version 2>&1
    if (($existing -join ' ') -match 'Python 3\.15') {
        Write-Host 'Existing .venv uses Python 3.15 (unsupported); rebuilding ...'
        Remove-Item (Join-Path $Root '.venv') -Recurse -Force
    }
}

if (-not (Test-Path $Python)) {
    Write-Host 'Creating Windows .venv (Python 3.12-3.14) ...'
    $created = $false
    foreach ($spec in @(
        @('py', '-3.14'), @('py', '-3.13'), @('py', '-3.12'), @('py', '-3'),
        @('python3.14'), @('python3.13'), @('python3.12'), @('python')
    )) {
        $exe = $spec[0]
        if (-not (Get-Command $exe -ErrorAction SilentlyContinue)) { continue }
        $launcherArgs = @()
        if ($spec.Count -gt 1) { $launcherArgs += $spec[1] }
        if (-not (Test-SupportedPython -Exe $exe -Arguments $launcherArgs)) { continue }
        & $exe @launcherArgs -m venv .venv
        if ($LASTEXITCODE -eq 0 -and (Test-Path $Python)) { $created = $true; break }
    }
    if (-not $created) {
        throw 'Tidak ada Python 3.12-3.14. Install dari python.org (3.12/3.13/3.14, 64-bit). Python 3.15 belum didukung slipcover/litellm.'
    }
}

if (-not (Test-Path $Python)) {
    throw 'Gagal membuat .venv.'
}

& $Python --version

Write-Host 'Installing project dependencies (this can take several minutes) ...'
& $Python -m pip install --upgrade pip
if ($LASTEXITCODE -ne 0) { throw 'pip upgrade gagal.' }
& $Python -m pip install -r config\requirements.txt
if ($LASTEXITCODE -ne 0) { throw 'pip install requirements gagal; lihat error di atas.' }
& $Python -m pip install -e .\coverup
if ($LASTEXITCODE -ne 0) { throw 'pip install -e coverup gagal; lihat error di atas.' }

Write-Host 'Registering Jupyter kernel ...'
& $Python -m ipykernel install --user --name prpl-venv --display-name 'Python-PRPL-venv'
if ($LASTEXITCODE -ne 0) { throw 'Kernel registration gagal.' }

Write-Host 'Verifying imports ...'
& $Python -c "import litellm,requests,dotenv,nbclient,aiolimiter,numpy,pandas,matplotlib,scipy,mcp,pytest,slipcover; print('DEPENDENCIES OK')"
if ($LASTEXITCODE -ne 0) { throw 'Verifikasi gagal: dependency masih hilang.' }

Write-Host ''
Write-Host 'SETUP COMPLETE'
Write-Host 'VS Code: Ctrl+Shift+P -> Developer: Reload Window'
Write-Host 'Notebook: Select Kernel -> Python-PRPL-venv -> Restart -> Run All'
