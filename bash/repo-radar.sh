#!/usr/bin/env bash

# Set the directory to the current working directory
dir=$(pwd)
home=$HOME

# Find all of the git repositories in the given directory
repos=$(find "$dir" -type d -name ".git")

# Print the report headings
printf "%-50s %-10s %-10s %s\n" "Path" "Modified" "Stashed" "Name"

# Loop through each repository and check the status
for repo in $repos
do
    # Get the path and repository name
    path=$(dirname "$repo")
    name=$(basename "$path")
    trunc_path="~${path#$home}"

    # Change to the repository directory
    cd "$path"

    # Count the number of modified and untracked files
    modified=$(git diff --name-only | wc -l)
    untracked=$(git ls-files --others --exclude-standard | wc -l)

    # Count the number of stashed changes
    stashed=$(git stash list | wc -l)

    # Print the repository report
    printf "%-50s %-10s %-10s %s\n" "$trunc_path" "$untracked" "$stashed" "$name"
done
