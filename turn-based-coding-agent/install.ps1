[CmdletBinding()]
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$Destination,

    [switch]$Force
)

$ErrorActionPreference = 'Stop'
$Source = $PSScriptRoot
$Target = Join-Path $Destination 'turn-based-coding-agent'

New-Item -ItemType Directory -Path $Destination -Force | Out-Null

if (Test-Path -LiteralPath $Target) {
    if (-not $Force) {
        throw "Target already exists: $Target. Use -Force to replace it."
    }

    Remove-Item -LiteralPath $Target -Recurse -Force
}

New-Item -ItemType Directory -Path $Target -Force | Out-Null
Copy-Item -Path (Join-Path $Source '*') -Destination $Target -Recurse -Force

Write-Output "Installed turn-based-coding-agent to: $Target"
