import requests
import json

def get_commits():
    x = input('Enter GitHub Username: ')
    r = requests.get('https://api.github.com/users/' + x + '/repos')
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
        r = requests.get('https://api.github.com/repos/' + x + '/' + k + '/commits')
        commits = json.loads(r.text)
        for v in commits:
            commit_counter[u] = commit_counter[u] + 1
        u = u + 1

    u = 0

    for k in repo_lookup:
        print('Repo: ' + k + ' Number of commits: ' + str(commit_counter[u]))
        u = u + 1

if __name__ == "__main__":
    get_commits()