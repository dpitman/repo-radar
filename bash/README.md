# BASH version of repo-radar

> <details><summary>:warning: DISCLAIMER!</summary>USE AT OWN RISK!</details>

---

To use this script, save it to a file (`e.g. repo-radar.sh`) and make it executable with the following command:

```bash
chmod +x repo-radar.sh
```

#### Then you can run it with:

```bash
./repo-radar.sh
```
This will search for git repositories in the directory specified by dir and print the status of each repository.

## Sample Putput

```bash
Path                               Modified    Stashed   Name
~/Working/learning-mongodb                6          0   learning-mongodb
~/Working/learning-github-actions         1          0   learning-github-actions
~/Working/learning-eBPF                   3          2   learning-eBPF
```
> **_`NOTE`:_**  I shortened the `PATH` so it would be more readable here. The script displays the full path. 

:arrow_heading_up: [BACK](../README.md)