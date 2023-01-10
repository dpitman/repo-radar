# git repo-radar

This script checks the status of git repositories and prints a report with repository details.

---

> <details><summary>:warning: DISCLAIMER!</summary>:boom: USE AT OWN RISK :exclamation:</details>
> If there is an easier way, please let me know.

---

## Problem Statement

---

Pushing changes to a remote repository at the end of the day is a good idea for several reasons. I don't like leaving changes dangling, which is a terrible practice. So I created this script to check at the end of the day. Why you say, well here are some reasons I can think of:

- It helps to ensure that your work is backed up and safe in case of unexpected issues, such as a power outage or hardware failure.
- It allows other team members to access your changes and collaborate on the project more effectively.
- It allows you to switch to a different task or work on a separate branch without worrying about losing your work.
- It helps you to stay organized and keep track of your progress.

Pushing changes to a remote repository at the end of the day is also a good practice to establish as part of your workflow. It helps to ensure that you are regularly committing and pushing your changes, which helps avoid conflicts and makes it easier to collaborate with others on the project.

---

### Sample Output

```bash
Path                              Untracked    Stashed   Name
~/Working/learning-mongodb                6          0   learning-mongodb
~/Working/learning-github-actions         1          0   learning-github-actions
~/Working/learning-eBPF                   3          2   learning-eBPF
```

> **_`NOTE`:_** I shortened the `PATH` so it would be more readable here. The script displays the full path.

---

| Version                      | Comments                                                                                   |
| ---------------------------- | ------------------------------------------------------------------------------------------ |
| [BASH](./bash/README.md)     | My original script will probably mostly stay the same.                                     |
| [PYTHON](./python/README.md) | Decided to create a python version and add some extra features... `coming soon`! :mailbox: |

---

## ToDo:
- thinking of adding all checks. Something like:
```bash
modified=$(git diff --name-status)
staged=$(git diff --cached --name-only)
stashed=$(git stash list)
local_head=$(git rev-parse HEAD)
remote_head=$(git ls-remote origin HEAD)
```
- 