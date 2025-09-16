# User Guide: Submitting a Serial Job on the SGE Grid Cluster

This guide provides step-by-step instructions on how to submit a serial job to the SGE (Sun Grid Engine) grid cluster.

## Prerequisites

- Access to the QUEVEDO cluster.
- A valid user account on the cluster.
- The job script ready for submission.

## Step 1: Create Your Job Script

Create a shell script that contains the commands you want to run. For example, create a file named `my_serial_job.sh`:
```c++
#!/bin/bash
#$ -N serial_pw
#$ -cwd
#$ -l h_rt=24:10:00
#$ -j y
#$ -o qe_pw_test_output_file.txt

module load espresso/6.4.1 
pw.x < input.scf.in > output.scf.out
``` 


## Step 2: Understanding the Job Script

The job script you created, `my_serial_job.sh`, is a shell script designed to run a job on a cluster using a job scheduler (like Sun Grid Engine). Let's break down the components of the script:

1. **Shebang (`#!/bin/bash`)**:
   - This line indicates that the script should be executed using the Bash shell. It tells the system which interpreter to use.

2. **Job Scheduler Directives**:
   - Lines starting with `#$` are directives for the job scheduler. They provide information about how to manage the job:
     - `#$ -N serial_pw`: Sets the name of the job to "serial_pw".
     - `#$ -cwd`: Specifies that the job should run in the current working directory.
     - `#$ -l h_rt=24:10:00`: Requests a maximum run time of 24 hours and 10 minutes.
     - `#$ -j y`: Merges standard error and standard output into a single output file.
     - `#$ -o qe_pw_test_output_file.txt`: Specifies the name of the output file where the job's output will be written.

3. **Loading Modules**:
   - `module load espresso/6.4.1`: This command loads the specified software module (in this case, version 6.4.1 of "espresso"). This is often necessary to ensure that the correct environment and dependencies are available for your job.

4. **Running the Program**:
   - `pw.x < input.scf.in > output.scf.out`: This line executes the program `pw.x`, redirecting input from `input.scf.in` and output to `output.scf.out`. The `<` operator takes the contents of `input.scf.in` as input for the program, while the `>` operator directs the program's output to `output.scf.out`.

### Summary

This job script is a crucial component for automating tasks on a computing cluster. By understanding each part of the script, you can customize it to suit your specific computational needs, manage resources effectively, and ensure that your jobs run smoothly. 


## Step 2: Submit Your Job Script

Once you have created your job script, you can submit it to the SGE grid cluster using the `qsub` command. Run the following command in your terminal:
```c++
qsub my_serial_job.sh
```

- Follow the steps on how to check job/cluster status.