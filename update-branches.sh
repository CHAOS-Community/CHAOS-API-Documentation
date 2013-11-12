# http://stackoverflow.com/questions/4532063/commit-to-multiple-branches-at-the-same-time-with-git

CURRENT_BRANCH="$(git rev-parse --abbrev-ref HEAD)"

git checkout v5 && \
  git rebase master

git checkout v6 && \
  git rebase v5

# Go back to original branch
git checkout $CURRENT_BRANCH


## Cherry-picking solution:
# http://stackoverflow.com/questions/7259135/git-commit-to-multiple-branches-at-the-same-time/18529576#18529576

