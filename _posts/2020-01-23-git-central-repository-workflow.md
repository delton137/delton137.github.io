---
id: 10011
title: Basic workflow for creating and using a remote git repository for backup and collaboration
disquscomments: true
author: Dan Elton
layout: post
permalink: /2020/01/23/git-central-repository-workflow.html
categories:
  - coding
  - git
tags:
  - coding
  - git
  - linux
---


These are some notes on how to move beyond just using git locally for version control. Let's assume you want to create a remote repository on a (linux) server named `remoteserver` to archive your code or so that multiple people can push/pull to a central repository on that server.

## (optional) setting up a hostname and an SSH key on your local machine

It is useful to associate the `remoteserver` hostname with its IP address on your local machine, so you don’t have to keep looking it up. Do this by editing `/etc/hosts` and enter this line:

`128.231.191.101 remoteserver`

It is also useful to set up an SSH key. This will prevent you from having to enter your username and password each time you clone/push/pull to the repository. This is done by entering:

`ssh-keygen`

After issuing this command, you will be asked to enter a password to encrypt your SSH key. While you can go with no encryption by simply entering nothing and hitting enter this is not recommended for security reasons. After you set up your password will only need to enter this password once, the first time it is needed after you log into your machine. Finally, enter:

`ssh-copy-id delton@bezier2`

## Creating a new code repo on the remote server

Instead of all projects being stored in a single repository it is recommended to create separate repositories for each project. That way all history and branches are specific to the project of interest and they are not all combined together. Lets assume that all git projects on `remoteserver` will be stored in `/home/git/`.  

To create a git repository called `myrepo.git` on `remoteserver` first create a new directory for it:

`cd /home/gitrepos/`\\
`mkdir myrepo.git`

Set the permissions on the directory:

`chgrp git myrepo.git`\\
`chmod 775 myrepo.git`

Move to that directory and create an empty git repository.

`git --bare init --shared`

**Notes**: The “.git” extension on the folder name is a useful convention. The `--bare` option creates a “bare” folder which is equivalent to the .git folder you may be familiar with. In such a repository, the source files are in a compressed form and not directly visible. You should never try to put source files directly into such a folder. The `--shared` option lets git know that all files in this directory should be shared among the “git" group. If the git group doesn't yet exist, you can create it with `sudo groupadd git`. If you are not in the git group you can add your username with `sudo usermod -a -G git <myusername>`. 

## Cloning a repo from the remote server

To clone an existing repository from `remoteserver` onto your local machine
run:

`git clone ssh://remoteserver/home/gitrepos/myrepo.git`

## Creating a new local git repository

From your source code folder, enter:

`git init`

To associate your name and email with your commits, use the following:

`git config --global user.name "John D. Smith"`\\
`git config --global user.email john.smith@gmail.com`

## Committing code to your local git repository

`git add *`\\
`git commit`

Make sure to add a comment on what the changes are for\! By default git
will drop to an editor for you to do this. You can add a comment in the
command line with `git commit -c "here is my comment"`.  

**Notes**: The first command (`git add *`) recursively “stages” all
files and folders for committing. It is often useful to create a
`.gitignore` file. This is simply a text file with a list of files and
folders you want git to exclude when you run `git add *`. You should
commit often and always comment your commits.

## Pushing your changes to the remote server

Run  

`git push ssh://remoteserver/home/gitrepos/myrepo.git master`

## Pulling changes from the remote server

Similarly you can pull any changes via:

`git pull ssh://remoteserver/home/gitrepos/myrepo.git master`

**Notes** you can use the shortcut commands `git push` and `git pull` by
formally linking your master branch to the remote repository and
telling git you want to merge changes into your master branch. This can
be done by entering:

`remote add origin ssh://remoteserver/home/gitrepos/myrepo.git`\\
`git config branch.master.remote origin`\\
`git config branch.master.merge refs/heads/master`

You can view your git remote configuration in the file `.git/config` and
if you want you can change it by modifying that file directly.

## What to do if your work falls behind others

It’s possible that when you use `git push` it will return an error
because others have made changes to the remote repository, so your
version is behind. You can fix this by running

`git pull --rebase origin master`

This pulls all of the changes and then adds your latest commit on top.
This is the same as saying “I want to add my changes to what everyone
else has already done.” The `--rebase` option “rebases” everything -
ie. it combines both the new stuff from the pull and the new changes
from your local commit(s) that you are trying to push into your last
commit. You could also just run `  git pull `, however this will create
an additional “merge commit” which is inelegant to have in your log
file.  

It’s possible that when you try to run `git pull --rebase` you will run
into merge conflicts. You now need to fix each merge conflict locally.
For each file with a merge conflict, edit the file as you see fit, and
then run

`git add filename`\\
`git rebase --continue`

If you want to remove a file you can run `git rm` instead of `git add`. At any time you can see a list of merge conflicts by running `git status`. If you make a mistake during this process or decide you don’t want to try to fix the conflicts, enter `git rebase --abort`.

## Viewing history and checking out previous versions

To view the history of changes enter:

`git log`

If you wish to go back and “checkout” a previous version of the code,
commit (or stash) your latest changes, and then enter something like:

`git checkout <commit-identifier>`

Here `<commit-identifier>` is a long string of numbers and letters
specific to the commit of interest, which you can find in the output of
`git log` (it will look something like
`181518141330729fa1809702ac28be02393bd14f`). Using this command will
replace all files in your source directory with the versions from that
commit. If you would like you can create a branch for performing
experiments and modifications, via `git checkout -b <new-branch-name>`
(however branching and merging will not be covered here). To return to
the latest version enter:

`git checkout master`

## Further reading

* [Parts of this workflow were taken from Atlassian. Much more information can be found in their tutorials](https://www.atlassian.com/git)
