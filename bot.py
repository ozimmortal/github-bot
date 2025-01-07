from github import Github
import requests,time

def get_quote()->str:
    try:
        res =  requests.get("https://api.kanye.rest").json()
        return res["quote"]
    except:
        return "Not found One."
def github_app(token:str,repo:str)->None:
    github = Github(token)
    quote = get_quote()
    try:
        repo = github.get_repo(repo)
        
        readme_file = None
        contents = repo.get_contents("")
        for file in contents:
            if file.name.lower() == "readme.md":
                readme_file = file
                break

        if not readme_file:
            print("README.md file not found in the repository.")
            return
        new_content = readme_file.decoded_content.decode("utf-8") + f"\n \n -- {quote}  {time.ctime()}"
        commit_message = "added new quote"
        repo.update_file(
            path=readme_file.path ,
            message=commit_message,
            content=new_content,
            sha=readme_file.sha  
        )
        print(f"File '{readme_file.path}' updated successfully!")
    except:
        print("Not Success")

if __name__ == "__main__":
    token = ""
    repo = ""
    github_app(token,repo)