def github_call(user):
    x_repos = []
    y_repo_size = []
    import requests
    receive = requests.get(f'https://api.github.com/users/{user}/repos',headers={"Authorization": "Token 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"})
    print(type(receive.json()))
    for x in receive.json():
        print(type(x))
        x_repos.append(x["name"])
        y_repo_size.append(x["size"])

    import matplotlib.pyplot as plt
    plt.bar(x_repos,y_repo_size)
    plt.xlabel('Repo Name')
    plt.ylabel('Repo Size')
    plt.title(f'Active Repos for {user}')
    plt.show()


def main():
    user = input("Input a GitHub user:")
    github_call(user)

if __name__ == "__main__":
    main()