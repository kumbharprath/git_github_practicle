# Shell script usage

In Git Bash, WSL, or a Linux/macOS terminal:

1. Start API in another terminal: `python -m uvicorn app.main:app --reload`
2. Health check: `bash scripts/check_service.sh http://127.0.0.1:8000/health`
3. Failure test: `bash scripts/check_service.sh http://127.0.0.1:9999/health`
4. Create demo log: `mkdir -p logs && echo 'INFO started' > logs/app.log`
5. Archive: `bash scripts/archive_logs.sh`

Windows PowerShell without Git Bash/WSL cannot execute Bash scripts directly.
