Software Environments
# Listing available software environments

# Steps
```bash
module avail                   # list environments
module load {name[/version]}   # load environment
module list                    # show active
module unload {name}           # unload one
module purge                   # unload all
module help {name}             # get help
```
- Example: `module load gnu/11` loads GNU-11 compilers.

```c
IMPORTANT NOTE:
It is important to always activate the right software  environments by using the module load
directive within your job script before submission.
```

