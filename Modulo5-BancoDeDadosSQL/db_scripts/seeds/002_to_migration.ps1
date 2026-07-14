# pegar o diretório atual
$scriptDirectory = Split-Path $MyInvocation.MyCommand.Definition -Parent

# arquivo de saída com todos os sql
$OutputFile = Join-Path -Path $scriptDirectory -ChildPath "migration.sql"

# verifica se o arquivo já existe, se existir deleta
if (Test-Path $OutputFile){
    Remove-Item $OutputFile
}

# pega os conteúdos dos arquivos
$sqlFiles = Get-ChildItem $scriptDirectory -Filter *.sql -File | Sort-Object Name

# concatena arquivos
foreach($file in $sqlFiles){
    Get-Content $file.FullName | Out-File -Append -FilePath $OutputFile
    "GO" | Out-File -Append -FilePath $OutputFile
}

Write-Host "Todos os arquivos foram combinados $outputFile"