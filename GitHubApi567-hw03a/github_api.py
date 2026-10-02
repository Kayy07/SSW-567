import requests
import json

def list_repositories(user_id):
    if not user_id:
        return []
    
    url = f"https://api.github.com/users/{user_id}/repos"
    payload = requests.get(url)
    repositories = json.loads(payload.text)

    response = []

    for repo in repositories:
        repo_name = repo["name"]

        commit_url = (
            f"https://api.github.com/repos/"
            f"{user_id}/{repo_name}/commits"
        )
        commit_payload = requests.get(commit_url)
        commits = json.loads(commit_payload.text)

        # Count the commits
        commit_count = len(commits)

        # Store the repository name and commit count
        response.append({
            "name": repo_name,
            "commits": commit_count
        })

        print(
            f"Repo: {repo_name} "
            f"Number of commits: {commit_count}"
        )

    return response


# Main program
if __name__ == "__main__":
    user_id = input("Enter a GitHub user ID: ")
    list_repositories(user_id)