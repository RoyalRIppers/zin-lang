param(
    [string]$Version = "4.13.1"
)
$dist = "antlr-$Version-complete.jar"
$toolDir = "tools/antlr"
$outDir = "compiler/gen/python"

New-Item -ItemType Directory -Force -Path $toolDir | Out-Null
New-Item -ItemType Directory -Force -Path $outDir | Out-Null

if (-not (Test-Path "$toolDir/$dist")) {
    Write-Host "[+] Downloading ANTLR $Version..."
    Invoke-WebRequest -UseBasicParsing -Uri "https://www.antlr.org/download/$dist" -OutFile "$toolDir/$dist"
}

Write-Host "[+] Generating Python3 parser..."
java -jar "$toolDir/$dist" -Dlanguage=Python3 -visitor -o "$outDir" "docs/spec/grammar/Zin.g4"
Write-Host "[+] Done. Generated in $outDir"
