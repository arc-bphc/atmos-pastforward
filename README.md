# Atmos-Pastforward

Pastforward is a competition hosted by ARC (Automation and Robotics Club) during Atmos, BITS Pilani Hyderabad Campus' Tech Fest.

[Event link](https://bits-atmos.org/events/PastForward)


## Milestones:

* To be decided
* Once decided we will work on them sequentially.



## Contributing

We love contributions. That out of the way, an average
contribution would involve the following:

1. Fork this repository in your account.
2. Clone it on your local machine.
3. Add a new remote using `git remote add upstream https://github.com/arc-bphc/atmos-pastforward.git`.
4. Create a new feature branch with `git checkout -b my-feature`.
5. Make your changes.
6. Lint your files and run all tests locally using `grunt` and `grunt test`.
7. Commit your changes.
8. Rebase your commits with `upstream/master`:
  - `git checkout master`
  - `git fetch upstream master`
  - `git reset --hard FETCH_HEAD`
  - `git checkout my-feature`
  - `git rebase master`
9. Resolve any merge conflicts, and then push the branch with `git push origin my-feature`.
10. Create a Pull Request detailing the changes you made and wait for review/merge.

It might seem a little complicated at a glance, but the fundamental concept is simple: we
want to ensure that your changes are always made on top of the latest changes to the
project and thus, we can easily merge your code. If you are facing any troubles, create a
PR as you usually would and we would merge it manually. :)

### Commit Message Guidelines

The commit message:

- is written in the imperative (e.g., "Fix ...", "Add ...")
- is kept short, while concisely explaining what the commit does.
- is clear about what part of the code is affected -- often by prefixing with the name of the subsystem and a colon, like "express: ..." or "docs: ...".
- is a complete sentence, ending with a period.

Good summaries:

- `scripts: Fix running stream_data and node tests individually.`
- `gather_subscriptions: Fix exception handling bad input.`
- `Add GitLab integration.`

Compare `gather_subscriptions: Fix exception handling bad input.` with:

- `gather_subscriptions was broken`, which doesn't explain how it was broken (and isn't in the imperative)
- `Fix exception when given bad input`, in which it's impossible to tell from the summary what part of the code is affected
- `gather_subscriptions: Fixing exception when given bad input.`, not in the imperative
- `gather_subscriptions: Fixed exception when given bad input.`, not in the imperative


<img src="https://avatars3.githubusercontent.com/u/30314930?s=200&v=4" width="150">