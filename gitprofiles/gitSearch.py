from github3 import login
from decouple import config
import time

class GitObj():

    g = login(config("USERNAME"), config("PASSWORD"))

    def gitSearchUser(self, location: str, language: str, repos: int=5, followers: int=10, verbose=True):
        q_ = "followers:>={} repos:>{}".format(followers, repos)
        if location:
            q_ += " location:{}".format(location)
        if language:
            q_ += " language:{}".format(language)

        if verbose: print(q_)

        return [a.user for a in self.g.search_users(q_)]

    def gitHireables(self, searchList):
        return [self.g.user(user.login) for user in searchList
                    if self.g.user(user.login).hireable and self.g.user(user.login).email]

    def top3Languages(self, user):
        repos = [a for a in self.g.repositories_by(user.login)]
        word_list = [x.language for x in repos if x.language is not None]
        word_list = ['Python' if x=='Jupyter Notebook' else x for x in word_list]

        word_counter = {}
        for word in word_list:
            if word in word_counter:
                word_counter[word] += 1
            else:
                word_counter[word] = 1

        popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
        user.type = popular_words[:3] #top 3
        return user

    def gitSearchProsForHire(self, location, language, repos, followers):
        start_time = time.time()
        ret = [self.top3Languages(user) for user in self.gitHireables(self.gitSearchUser(location, language, repos, followers))]
        elapsed_time = time.time() - start_time
        print("elapsed time searching:", elapsed_time)
        return ret
