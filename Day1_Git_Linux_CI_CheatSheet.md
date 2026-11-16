# Day 1 Quick Reference

| Task | Command |
|---|---|
| Git status | `git status` |
| Stage | `git add .` |
| Commit | `git commit -m "message"` |
| New branch | `git switch -c feature/x` |
| Switch branch | `git switch main` |
| Merge | `git merge feature/x` |
| Push | `git push -u origin feature/x` |
| History | `git log --oneline --decorate` |
| Add tag | `git tag -a v1.0.0 -m "Release"` |
| Show folder | `pwd; ls -la` |
| Search logs | `grep ERROR logs/app.log` |
| Processes | `ps aux` |
| HTTP check | `curl --fail http://127.0.0.1:8000/health` |
| Exit status | `echo $?` |
| Test Python | `python -m pytest -q` |
| Lint | `ruff check .` |
| Run API | `python -m uvicorn app.main:app --reload` |

## Common CI terms
- Trigger: push / pull_request
- Job: isolated run on a runner
- Step: a command or reusable action
- Artifact: output retained for later inspection
- Cache: accelerates repeated work
- Gate: a required success check before merge/release
