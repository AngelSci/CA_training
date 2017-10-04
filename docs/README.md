# README

* This repository in under development and should not be used yet for courses. 
* Trainers wishing to build course materials should continue to use [the original Training repository](https://github.com/ContinuumIO/Training) until informed otherwise.


## Contribute

* Current steward and maintainer of this repository is dhavide.aruliah@continuum.io
* Please coordinate with maintainer if you wish to contribute.
* Development guidelines are here: [./README_DEV.md](./README_DEV.md)


## Goals

* create better curriculum for course "Introduction to Python Programming using Anaconda"
* stand-alone repo of curriculum materials, no external dependencies
* a plan that can be developed over time, not all at once
* course files that require minimal to zero preparation to deliver
* static content that can be delivered as-is, no build process
* course customization done by content exclusion, not inclusion 
* single notebooks that can be skipped without breaking the narrative
* tested notebooks, tests performed only with the environment files provided
* notebooks that can be updated during training on a "deployment branch"
* deployed content that if modified, allows fast-forward merge into master.
* No automated injection of styling or stitching (unless automated undo)

## Development Plan

* Design a course content outline that fits the target audience
* Migrate a subset of the materials from the original Training repo
     * use content outline to guide which material may be reused 
     * still need to migrate `/data` and `/img` files
* create a working static course from that material, similar to output from old build script
    * review past `spec.yml` files used to build previous courses
* Reorganize the notebooks to match the topic ordering
* test all notebooks
    * create issues in GitHub for broken notebooks
    * build the queue of issues before fixing, then get others to help in spare time
* fill in content where gaps exist
    * new exercise notebooks
    * new lesson notebooks

 