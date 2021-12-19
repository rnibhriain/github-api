import requests
import mpld3
from mpld3 import plugins
import matplotlib.pyplot as plt

def github_call(user):
    x_repos = []
    y_repo_size = []
    receive = requests.get(f'https://api.github.com/users/{user}/repos',headers={"Authorization": "Token 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"})
    print(type(receive.json()))
    for x in receive.json():
        print(type(x))
        x_repos.append(x["name"])
        y_repo_size.append(x["size"])
    plt.bar(x_repos,y_repo_size)
    plt.xlabel('Repo Name')
    plt.ylabel('Repo Size')
    plt.title(f'Active Repos for {user}')
    plt.show()

def average_lines (lang) :
    # Create an API request 
    url = f'https://api.github.com/search/repositories?q=language:{lang}&sort=stars'
    response = requests.get(url)

    print("Status code: ", response.status_code)
    # In a variable, save the API response.
    response_dict = response.json()
    # Evaluate the results.
    print(response_dict.keys())
    print("Total repos:", response_dict['total_count'])
    # find total number of repositories
    repos_dicts = response_dict['items']
    
    print("Repositories found:", len(repos_dicts))
    sizes = 0

    for repos_dict in repos_dicts:
        sizes += repos_dict['size']
    avg = sizes/len(repos_dicts)
    print('Average size: ', avg)
    return avg



def main():
    user = input("Input a GitHub user:")
    github_call(user)
    lang = 'python'
    y1 = average_lines(lang)
    lang = 'javascript'
    y2 = average_lines(lang)
    lang = 'java'
    y3 = average_lines(lang)
    lang = 'c++'
    y4 = average_lines(lang)
    lang = 'typescript'
    y5 = average_lines(lang)
    lang = 'go'
    y6 = average_lines(lang)
    lang = 'ruby'
    y7 = average_lines(lang)
    plt.clf()
    x = ['python', 'javascript', 'java', 'c++', 'typescript', 'go', 'ruby']
    y = [y1, y2, y3, y4, y5, y6, y7]
    plt.bar(x,y, color='pink')
    plt.xlabel('Repo Type')
    plt.ylabel('Repo Size')
    plt.title('Avg Repo size for diff langauges')
    plt.display()

if __name__ == "__main__":
    main()