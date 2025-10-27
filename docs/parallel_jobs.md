# 7.0 Submitting a Parallel Job

This section provides step-by-step instructions for submitting a parallel job on an SGE-grid type cluster using a sample job script.

## 7.1 Prerequisites

- Access to an SGE-grid cluster.
- Necessary permissions to submit jobs.
- Required modules (e.g., OpenMPI) installed on the cluster.

## 7.2 Job Submission Script

Below is a sample job submission script. Save this script as `parallel_job.sh` or any name of your choice.

```c++
#!/bin/bash
#$ -N matmul
#$ -cwd
#$ -pe mpi 64
#$ -l h_rt=24:10:00
#$ -j y
#$ -o mpi_matmul.txt

module load openmpi

mpirun -mca btl_openib_allow_ib 1 -np 64 ./matmulmpi.x
```

## 7.3 Running the Sample Job Script

This section provides a detailed explanation of the job submission script and its components.

## 7.4 Script Breakdown

1. **Shebang Line**: 
    ```bash
    #!/bin/bash
    ```
    This line indicates that the script should be run in the Bash shell.

2. **Job Name**:
    ```bash
    #$ -N matmul
    ```
    This sets the name of the job to "matmul".

3. **Current Working Directory**:
    ```bash
    #$ -cwd
    ```
    This option tells the scheduler to run the job from the current working directory.

4. **Parallel Environment**:
    ```bash
    #$ -pe mpi 64
    ```
    This specifies that the job will use the MPI parallel environment with 64 slots.

5. **Runtime Limit**:
    ```bash
    #$ -l h_rt=24:10:00
    ```
    This sets a hard runtime limit of 24 hours and 10 minutes for the job.

6. **Job Output**:
    ```bash
    #$ -j y
    #$ -o mpi_matmul.txt
    ```
    These lines combine standard output and error into a single file named `mpi_matmul.txt`. You can separate them.

7. **Loading Modules**:
    ```bash
    module load openmpi
    ```
    This command loads the OpenMPI module, which is necessary for running MPI applications.

8. **Running the MPI Program**:
    ```bash
    mpirun -mca btl_openib_allow_ib 1 -np 64 ./matmulmpi.x
    ```
    This command executes the MPI program `matmulmpi.x` using 64 processes.

## 7.5 Summary

This job submission script is designed to run a parallel matrix multiplication program using MPI on an SGE-grid cluster. Ensure that all prerequisites are met before submitting the job.

## 7.6 Running the Job

To submit your parallel job, follow these steps:

1. **Open a terminal** on your local machine or connect to the SGE-grid cluster via SSH.

2. **Navigate to the directory** where your job submission script (`parallel_job.sh`) is located.

    ```bash
    cd /path/to/your/script
    ```

3. **Submit the job** using the `qsub` command:

    ```bash
    qsub parallel_job.sh
    ```

4. **Monitor your job** status with the following command:

    ```bash
    qstat -u $USER
    ```

5. **Check the output** of your job in the specified output file (`mpi_matmul.txt`) once it has completed.
## 7.7 Quantum Espresso 7.4.1 Users 
```c++
#!/bin/bash
#$ -N qe_scf
#$ -cwd
#$ -pe mpi 64
#$ -l h_rt=24:00:00
#$ -j y
#$ -o qe_job.txt

module load espresso/7.4.1

mpirun -mca btl_openib_allow_ib 1 -np 64 pw.x < scf.in > scf.out

```

## 7.8 Additional Notes For Compiling and Running in Parallel

- Ensure that your executable (`matmulmpi.x`) is compiled and available in the same directory as your job script.
- Adjust the number of processors (`-pe mpi 64`) and runtime (`-l h_rt=24:10:00`) according to your job requirements and cluster policies.
- Ensure that your Makefile is pointing to the correct set of library and include directories. 
- Use `module show module_name` to display the paths to the libraries for the modules loaded. (e.g. `module show fftw/3.3.10-gnu11`)
- For more information on job submission options, refer to the SGE documentation or contact your system administrator.
