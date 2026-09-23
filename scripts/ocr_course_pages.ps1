param([string]$Manifest = "$PSScriptRoot\..\tmp\course_extract\ocr_manifest.json")
Add-Type -AssemblyName System.Runtime.WindowsRuntime
$null = [Windows.Storage.StorageFile, Windows.Storage, ContentType=WindowsRuntime]
$null = [Windows.Graphics.Imaging.BitmapDecoder, Windows.Graphics.Imaging, ContentType=WindowsRuntime]
$null = [Windows.Media.Ocr.OcrEngine, Windows.Foundation, ContentType=WindowsRuntime]
$null = [Windows.Globalization.Language, Windows.Globalization, ContentType=WindowsRuntime]
$asTask = ([System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object { $_.Name -eq 'AsTask' -and $_.IsGenericMethod -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' })[0]
function AwaitResult($Operation, $Type) {
    $task = $asTask.MakeGenericMethod($Type).Invoke($null, @($Operation))
    $task.Wait()
    return $task.Result
}
$engines = @{}
foreach ($tag in @('en-US','zh-Hans-CN')) {
    $engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage([Windows.Globalization.Language]::new($tag))
    if ($engine) { $engines[$tag] = $engine }
}
$rows = Get-Content -LiteralPath $Manifest -Raw -Encoding UTF8 | ConvertFrom-Json
$count = 0
foreach ($row in $rows) {
    $count++
    if (Test-Path -LiteralPath $row.output) { continue }
    try {
        $file = AwaitResult ([Windows.Storage.StorageFile]::GetFileFromPathAsync($row.image)) ([Windows.Storage.StorageFile])
        $stream = AwaitResult ($file.OpenAsync([Windows.Storage.FileAccessMode]::Read)) ([Windows.Storage.Streams.IRandomAccessStream])
        $decoder = AwaitResult ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)) ([Windows.Graphics.Imaging.BitmapDecoder])
        $bitmap = AwaitResult ($decoder.GetSoftwareBitmapAsync()) ([Windows.Graphics.Imaging.SoftwareBitmap])
        $languages = @('en-US')
        if ($row.chinese -and $engines.ContainsKey('zh-Hans-CN')) { $languages += 'zh-Hans-CN' }
        $results = @{}
        foreach ($tag in $languages) {
            $result = AwaitResult ($engines[$tag].RecognizeAsync($bitmap)) ([Windows.Media.Ocr.OcrResult])
            $lines = @($result.Lines | ForEach-Object { $_.Text })
            $results[$tag] = @{ text = ($lines -join "`n") }
        }
        $payload = @{ results = $results; error = $null } | ConvertTo-Json -Depth 5
        [System.IO.File]::WriteAllText($row.output, $payload, [System.Text.UTF8Encoding]::new($false))
        $bitmap.Dispose(); $stream.Dispose()
    } catch { Write-Output "ERROR $($row.image) $_"; exit 1 }
    if ($count % 50 -eq 0) { Write-Output "OCR $count/$($rows.Count)" }
}
Write-Output "OCR complete: $($rows.Count) pages"
