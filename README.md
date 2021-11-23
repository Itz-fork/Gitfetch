# Gitfetch :octocat:

<p align="center">
  <a href="#"><img src="https://user-images.githubusercontent.com/77770753/142969033-2f653aa9-4a81-4784-902f-581eff402211.png" alt="Gitfetch Cli"></a></br>
  <b>Just a (cli?) tool to get github user details 🙂</b>
</p>


## Installation 📂

Install [Gitfetch](https://github.com/Itz-fork/Gitfetch) via pypi

```
pip install gitfetch
```

or

```
pip install git+https://github.com/Itz-fork/Gitfetch.git
```


## Usage 👀

- **CLI Usage 👇,**
  - ```
    gitfetch [your github username]
    ```
  - Ex:
    ```gitfetch Itz-fork```

- **Use it as a python module 👇,**
  - ```python
    from gitfetch_tools import GitFetch

    git = GitFetch("Your-Github-Username")
    print(git.fetch_user_data())
    ```

## FAQ 😕

#### Q: Can I customize it?
**A:** Yeah, check [fetch.py](https://github.com/Itz-fork/Gitfetch/blob/master/gitfetch_tools/fetch.py) and [display](https://github.com/Itz-fork/Gitfetch/blob/master/gitfetch_tools/display) files.
