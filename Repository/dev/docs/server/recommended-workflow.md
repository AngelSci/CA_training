Recommended Workflow
====================

One of the most useful features of Anaconda Server is its ability to
help you manage package development and deployment in a seamless
fashion. Below you can find a write-up of the actual development process
and channel usage employed by one of our internal Wakari team.

Leveraging Channels for Workflow Separation
-------------------------------------------

Using multiple channels allows your team to maintain separate package
states and easily earmark and control the versions and states of
packages that users can install. For example, your team might create the
following channels:

-   master
-   staging
-   release

**Master** is created any time something is merged into our master
branch. It’s considered the development build of all of our components
that make up Wakari. Code that makes it to this should be stable and
have been confirmed independently, but a full QA test has not been run
on it yet.

Once we’re ready to start working on a release, we create a
**staging**:X.Y.Z branch. This contains all code that’s going to go into
a release. No new features should be introduced at this point, just any
last minute bug fixes to existing code.

The staging channel gets culled so only the latest package is maintained
in it — any alpha, beta, or dev packages are removed. After all testing
is complete, all issues are resolved, and the channel contains only one
version of each package, we copy that package into a **release**:X.Y.Z
channel, then lock that channel.

We’ve used this through 4 release cycles and so far its worked out well
for us.
