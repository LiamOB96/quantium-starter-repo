# run_tests.ps1
# Activate virtual environment
& "$PSScriptRoot\venv\Scripts\Activate.ps1"

# Run pytest
pytest
$exit_code = $LASTEXITCODE

# Exit with 0 if tests passed, 1 if they failed
if ($exit_code -eq 0) {
    Write-Host "All tests passed!"
    exit 0
} else {
    Write-Host "Some tests failed."
    exit 1
}