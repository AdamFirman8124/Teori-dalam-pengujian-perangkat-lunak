param(
    [Parameter(Mandatory = $true)]
    [ValidateRange(0, 99)]
    [int]$Index,

    [Parameter(Mandatory = $true)]
    [ValidateRange(1, 100)]
    [int]$Count
)

$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
Set-Location $Root

if ($Index -ge $Count) {
    throw "Index harus 0..$($Count - 1), diberikan $Index"
}

$Python = Join-Path $Root '.venv\Scripts\python.exe'
if (-not (Test-Path $Python)) {
    throw 'Jalankan tools\setup_windows.ps1 terlebih dahulu.'
}

# Notebook loads config/.env with override=True, so write a temporary per-shard
# config, run from a private project copy, and keep the real API key local.
$ShardRoot = Join-Path $Root (".shards\shard-{0}-of-{1}" -f $Index, $Count)
$ResultRel = "experiment_results_shard_$Index"
$Log = Join-Path $Root ("shard-{0}.log" -f $Index)
$Err = Join-Path $Root ("shard-{0}.err.log" -f $Index)

# One repository cannot safely host simultaneous notebook runs: each modifies
# work/checkpoints. Robocopy a lightweight private copy, excluding generated and
# environment directories; reuse the root venv through an absolute interpreter.
New-Item -ItemType Directory -Force $ShardRoot | Out-Null
$null = robocopy $Root $ShardRoot /MIR /XD .git .venv .shards experiment_results /XF '*.log' '*.pid' /NFL /NDL /NJH /NJS /NP
if ($LASTEXITCODE -gt 7) { throw "robocopy gagal: $LASTEXITCODE" }

$EnvPath = Join-Path $ShardRoot 'config\.env'
$EnvText = Get-Content (Join-Path $Root 'config\.env') -Raw
function Set-EnvValue([string]$Text, [string]$Name, [string]$Value) {
    $pattern = '(?m)^' + [regex]::Escape($Name) + '=.*$'
    if ([regex]::IsMatch($Text, $pattern)) {
        return [regex]::Replace($Text, $pattern, "$Name=$Value")
    }
    return $Text.TrimEnd() + "`r`n$Name=$Value`r`n"
}
$EnvText = Set-EnvValue $EnvText 'TASK_SHARD_COUNT' "$Count"
$EnvText = Set-EnvValue $EnvText 'TASK_SHARD_INDEX' "$Index"
$EnvText = Set-EnvValue $EnvText 'RESULTS_DIR' $ResultRel
$EnvText = Set-EnvValue $EnvText 'RUN_LABEL' ("shard-{0}-of-{1}" -f $Index, $Count)
$EnvText = Set-EnvValue $EnvText 'RESUME' '0'
$EnvText = Set-EnvValue $EnvText 'FRESH' '1'
Set-Content $EnvPath $EnvText -Encoding utf8

Remove-Item $Log, $Err -Force -ErrorAction SilentlyContinue
$Args = @(
    'tools\run_notebook.py',
    'experiments_codamosa_coverup.ipynb',
    "$ResultRel\executed.ipynb"
)
$Process = Start-Process -FilePath $Python -ArgumentList $Args `
    -WorkingDirectory $ShardRoot -RedirectStandardOutput $Log `
    -RedirectStandardError $Err -PassThru
Set-Content (Join-Path $Root ("shard-{0}.pid" -f $Index)) $Process.Id
Write-Host "Shard $Index/$Count started: PID=$($Process.Id)"
Write-Host "Results: $ShardRoot\$ResultRel"
Write-Host "Logs: $Log / $Err"
