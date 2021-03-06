import git
import os
import junos

def collect_and_push(dev):
    cwd = os.getcwd()
    repo = git.Repo(cwd)
    repo.git.pull('origin', 'master')
    junos.collect_junos_commands(dev)
    print repo.git.add("data_collected/" + dev + "/.")
    repo.git.commit(m = "from Gitpython")
    repo.git.push('origin', 'master')
    return "done"
