# Requirements
Valid Credentials and Jobs

# Checking the Status of an SGE-Grid Cluster and Jobs

To check the status of an SGE-Grid cluster and the jobs you have submitted, follow these steps:

1. **Check Cluster Status**
    Use the following command to get an overview of the cluster's status:
    ```bash
    qstat -g c
    ```

2. **Check Job Status**
    To view the status of your submitted jobs, use:
    ```bash
    qstat -u your_username
    ```
    Replace `your_username` with your actual username.

3. **Detailed Job Information**
    For detailed information about a specific job, use:
    ```bash
    qstat -f job_id
    ```
    Replace `job_id` with the ID of the job you want to inspect.

4. **Check Compute Nodes**
    To see the status of the compute nodes, use:
    ```bash
    qstat -f
    ```
    Otherwise use,
    ```bash
    qhost
    ```
5. **Monitor Resource Usage**
    To monitor resource usage of jobs, you can use:
    ```bash
    qacct -j job_id
    ```
    Again, replace `job_id` with the ID of the job you want to check.

 
- NB: DO NOT RUN JOBS ON YOUR LOGIN NODE!!! as this will make production slow accross the cluster. Use job submission scripts to request queues and resources.
In case of errors, Notify the administration (Check our Website for Who to Contact).