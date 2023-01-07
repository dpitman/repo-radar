import os
import subprocess


def main():
    # Get the current working directory
    cwd = os.getcwd()

    # Find all of the git repositories in the given directory
    repos = find_repos(cwd)

    # Print the report headings
    print("{:<50} {:>10} {:>10} {}".format(
        "Path", "Untracked", "Stashed", "Name"))

    # Loop through each repository and check the status
    for repo in repos:
        # Get the path and repository name
        path = os.path.dirname(repo)
        name = os.path.basename(path)

        # Change to the repository directory
        os.chdir(path)

        # Count the number of modified and untracked files
        modified = count_lines(["git", "diff", "--name-status"])
        untracked = count_lines(
            ["git", "ls-files", "--others", "--exclude-standard"])

        # Count the number of stashed changes
        stashed = count_lines(["git", "stash", "list"])

        # Print the repository report
        print("{:<50} {:>10} {:>10} {}".format(path, untracked, stashed, name))


def find_repos(dir):
    """Find all of the git repositories in the given directory"""
    repos = []
    for root, dirs, files in os.walk(dir):
        if ".git" in dirs:
            repos.append(os.path.join(root, ".git"))
    return repos


def count_lines(cmd):
    """Run a command and return the number of lines in its output"""
    output = subprocess.run(cmd, capture_output=True, text=True)
    return len(output.stdout.split("\n")) - 1


if __name__ == "__main__":
    main()
