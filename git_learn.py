""""
This file contains the basic commands usage methods for git version control

"""

##############################
# BASIC GIT WORKFLOW
##############################

git init "initializes a git project"

git status "check the status of changes made within a project"

git add filename(s) "adds file(s) to the staging area"

git diff filename "checks for differences between the working copy and
                   copy in the staging area"

q "exits the diff command interface"

git commit -m "message": "commits a change to the local repository. Should
                         be in present tense and < 50 characters"

git log "shows the log of changes to the local repository, it consist of a
        40 character SHA, the commit author, the commit time and the msg"

##############################
# BACKTRACKING
##############################

git show HEAD "The head commit is the commit that you are currently on. 
              This command shows all the output of git log *plus* all the
              file changes that were commited"

git checkout HEAD filename "restores the working directory filename to
                            look exactly the same as it did on your last
                            commit (the head commit)"

git reset HEAD filename "unstages filename from the staging area: it
                        resets the file in the staging area to be the same
                        as the head commit. *It does not change the file
                        in the working directory* it just removes them 
                        from staging area"
git reset SHA "resets the project to the specific SHA, SHA should be 
               entered as the first 7 charachters of the SHA. Any commit
               fter this commit will be gone. It rewinds your project"

##############################
# GIT BRANCHING
##############################

git branch "identify what branch you are on by *"

git branch new_branch "creates a new branch, name can not contain spaces"

git checkout branch_name "switch to branch_name branch"

git merge branch_name "updates the master branch with changes from
                      branch_name branch. Here we say branch_name is the 
                      giver branch and master is the reciever branch"

""" 
CONFLICT IN MERGING: if a conflict occurs in merging the bracnh to the master, the automatic merge will fail and you will need to fix the conflicting file manually. In that file you will see the following at each merge conflict point: 
<<<<<<< HEAD
master version of line
============
branch version of line
>>>>>>> BRANCH
To correct decide which version of the line to keep, delete all of gits special markings (>>, <<, HEAD, BRANCH), add the file to the staging area and in the commit msg write "Resolve merge conflict"
"""
git branch -d branch_name "deletes a branch"

#############################
# GIT TEAMWORK
##############################

git clone remote_location clone_name "replicates a remote repository at
                                      remote location and names it 
                                      clone_name. It also gives the 
                                      remote_loc the name origin"
git remote -v "list a git projects remotes"

git fetch "fetches changes made to remote and brings those changes to a
           remote branch. This command does not merge remote changes into
           your local repository"

git merge origin/master "merges the cahnges from the remote branch into 
                        your local repository, it fast forwards your local
                        master up to date with remote"

""" The workflow for Git collaborations typically follows this order:

1. Fetch and merge changes from the remote
2. Create a branch to work on a new project feature
3. Develop the feature on your branch and commit your work
4. Fetch and merge from the remote again (in case new commits were made   while you were working)
5. Push your branch up to the remote for review

Steps 1 and 4 are a safeguard against merge conflicts, which occur when two branches contain file changes that cannot be merged with the git merge command.

"""

git push origin branch_name "pushes the changes in branch name to the
                            remote origin where they can then be merged to
                            the remote master branch"








