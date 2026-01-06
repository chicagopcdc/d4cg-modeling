# DSM Git Workflow: Feature Branches + Rebase + Squash Merge

This repository uses a feature-branch workflow with rebasing and squash merges to keep `main` clean and avoid overwriting each other’s work.

Principles
- No direct pushes to `main`
- All work happens on short-lived feature branches
- Feature branches are rebased onto `main`
- Pull requests are merged using "Squash and merge"
- One PR = one commit on `main`


## 0) Start from a clean `main`

Always begin from an up-to-date `main`.

<pre>
git switch main
git fetch origin  
git pull --ff-only  
git status
</pre>  

git pull --ff-only is safe: it will refuse to run if your local `main` has diverged.


## 1) Create a feature branch

Use a short-lived, descriptive branch name that follows the pattern of `[user initials]/[topic]`. For example:

<pre>git switch -c MW/genetic-analysis-edits</pre>


## 2) Make edits and commit (repeat as needed)

### Stage everything using patch control

<pre>git add -p [filename]</pre>  


- **About patch control:**
  
  When staging with patch control, Git presents each changed code hunk and prompts:
  
  <pre>Stage this hunk [y,n,q,a,d,s,e,?]?</pre>
  
  | Key | Name | What it does |
  |-----|------|--------------|
  | `y` | yes | Stage this hunk |
  | `n` | no | Do not stage this hunk (leave it unstaged) |
  | `q` | quit | Quit patch mode immediately; already staged hunks remain staged |
  | `a` | all | Stage this hunk and all remaining hunks in the file |
  | `d` | do not stage | Skip this hunk and all remaining hunks in the file |
  | `s` | split | Split the current hunk into smaller hunks (often down to individual lines) |
  | `e` | edit | Manually edit the hunk before staging; remove `+` lines to exclude them |
  | `?` | help | Show the full help message |
  

- **Commmon patch options:**
  
  | Key | When to use it |
  |-----|----------------|
  | `y` | This hunk belongs in the commit |
  | `n` | This hunk does not belong in the commit |
  | `s` | The hunk mixes multiple logical changes |
  | `e` | You need line-level control inside the hunk |



### Commit the changes:
<pre>git commit -m "Describe the change"</pre> 


### Check your state:
<pre>
git status  
git log --oneline
</pre>


## 3) Rebase your branch onto latest origin/main

<pre>
git fetch origin  
git rebase origin/main  
</pre>

If conflicts occur:
<pre>
git status  
(resolve conflicts in files)  
git add [filename]
git rebase --continue  
</pre>

To abandon the rebase:
<pre>git rebase --abort</pre>

---

## 4) Push your branch

First push:

<pre>git push -u origin [feature-branch]</pre>

If you rebased after already pushing (step 6):

<pre>git push --force-with-lease origin [feature-branch]</pre>

Never use git push --force.



## 5) Open a Pull Request (GitHub UI)

**Base:** main  
**Compare:** [feature-branch]

High-level description of changes



## 6) Keep the PR up to date (if required)

If GitHub says the branch is out of date:
<pre>
git fetch origin  
git rebase origin/main  
git push --force-with-lease origin [feature-branch]  
</pre>



## 7) Merge using Squash and merge (GitHub UI)

On the PR page:
<pre>
- Choose Squash and merge
- Use PR title as the commit title
- Merge
- Delete the branch on GitHub
</pre>
Main will receive one clean commit per PR.



## 8) After merge: update local main and clean up

<pre>
git switch main  
git pull --ff-only  
git branch -d [feature-branch] 
git fetch -p  
</pre>

