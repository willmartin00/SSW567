import requests
import json

def get_commits():
    x = 'willmartin00'
    r = get_repos(x)
    if isinstance(r, str):
        repos = json.loads(r)
    else:
        repos = json.loads(r.text)
    repo_lookup = []
    commits_list = []

    for k in repos:
        try:
            z = k['name']
        except:
            print("Out of api calls")
            quit()
        repo_lookup.append(z)
        commits_list.append(0)

    commit_counter = [0] * len(commits_list)
    u = 0

    for k in repo_lookup:
        r = get_commits_sub(x,k)
        if isinstance(r, str):
            commits = json.loads(r)
        else:
            commits = json.loads(r.text)
        for v in commits:
            commit_counter[u] = commit_counter[u] + 1
        u = u + 1

    u = 0

    for k in repo_lookup:
        print('Repo: ' + k + ' Number of commits: ' + str(commit_counter[u]))
        u = u + 1

def get_commits_sub(x, k):
    return requests.get('https://api.github.com/repos/' + x + '/' + k + '/commits')

def get_repos(x):
    return requests.get('https://api.github.com/users/' + x + '/repos')

if __name__ == "__main__":
    get_commits()