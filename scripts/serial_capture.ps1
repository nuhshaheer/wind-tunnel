<#
serial_capture.ps1: record every line an Arduino sends over USB serial into a CSV file, stamped with the PC's clock.

Why: the Arduino IDE's Serial Monitor copies only the lines on screen, so minutes of data are lost. This keeps all of
them, byte for byte apart from the time stamp added in front.

Usage (from the repository root; the Arduino IDE's Serial Monitor and Serial Plotter must be CLOSED, because only one
program can open the port at a time):

  powershell -NoProfile -ExecutionPolicy Bypass -File scripts\serial_capture.ps1 -Port COM3 -OutFile data\raw\<folder>\run01.csv

  Stop it with Ctrl+C, or give -Seconds N to stop after N seconds, or give -StopFile <path> and create that file to stop
  it cleanly (useful when it runs in the background).

Input: text lines from the board at -Baud (default 115200), ending in CR LF (Arduino println).
Output (-OutFile, UTF-8 without BOM; refuses to overwrite an existing file):
  pc_time,<the line exactly as the board sent it>
  pc_time : the PC's local time when the line was read, ISO 8601 with milliseconds and UTC offset,
            for example 2026-11-26T14:03:05.123-05:00. It lines the data up with notes of what was done when.
  The board's own CSV header (a line starting with a letter, e.g. "time_ms,counts") is written as "pc_time,time_ms,counts".
  Lines starting with '#' are the sketch's messages; they are kept, with the time in front.
  Units are whatever the sketch states in its header and comments (e.g. hx711_raw_counts: time_ms in ms, counts in ADC
  counts).
Opening the port resets the Mega (the DTR line), so the sketch starts again and prints its header first.

Needs only Windows PowerShell 5.1 and .NET's System.IO.Ports.SerialPort, both part of Windows: nothing to install.
#>
param(
  [string]$Port = 'COM3',
  [int]$Baud = 115200,
  [Parameter(Mandatory = $true)][string]$OutFile,
  [int]$Seconds = 0,
  [string]$StopFile = ''
)
$ErrorActionPreference = 'Stop'

# Resolve against PowerShell's current folder (.NET's current folder can differ).
$outPath = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($OutFile)
if (Test-Path -LiteralPath $outPath) { throw "Refusing to overwrite an existing file: $outPath" }
$outDir = Split-Path -Parent $outPath
if (-not (Test-Path -LiteralPath $outDir)) { New-Item -ItemType Directory -Path $outDir | Out-Null }
$stopPath = ''
if ($StopFile) { $stopPath = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($StopFile) }

$sp = New-Object System.IO.Ports.SerialPort $Port, $Baud, ([System.IO.Ports.Parity]::None), 8, ([System.IO.Ports.StopBits]::One)
$sp.NewLine = "`n"
$sp.ReadTimeout = 500
$sp.DtrEnable = $true

# Open the port before creating the file, so a busy port (e.g. the IDE's Serial Monitor still open) leaves no empty file.
$sp.Open()
$writer = New-Object System.IO.StreamWriter($outPath, $false, (New-Object System.Text.UTF8Encoding($false)))
$writer.AutoFlush = $true   # every line reaches the disk at once, so a crash or a killed process loses nothing

$lines = 0
$start = Get-Date
Write-Output ("Recording {0} at {1} baud into {2} (started {3})" -f $Port, $Baud, $outPath, $start.ToString('yyyy-MM-ddTHH:mm:ss.fffzzz'))
try {
  while ($true) {
    if ($Seconds -gt 0 -and ((Get-Date) - $start).TotalSeconds -ge $Seconds) { break }
    if ($stopPath -and (Test-Path -LiteralPath $stopPath)) { break }
    try {
      $line = $sp.ReadLine()
    } catch {
      $e = $_.Exception
      if ($e -is [System.TimeoutException] -or $e.InnerException -is [System.TimeoutException]) { continue }
      throw
    }
    $line = $line.TrimEnd("`r")
    if ($line -match '^[A-Za-z_]') {
      $writer.WriteLine('pc_time,' + $line)
    } else {
      $writer.WriteLine((Get-Date).ToString('yyyy-MM-ddTHH:mm:ss.fffzzz') + ',' + $line)
    }
    $lines++
  }
} finally {
  if ($sp.IsOpen) { $sp.Close() }
  $writer.Close()
  Write-Output ("Stopped {0}: {1} lines written to {2}" -f (Get-Date).ToString('yyyy-MM-ddTHH:mm:ss.fffzzz'), $lines, $outPath)
}
