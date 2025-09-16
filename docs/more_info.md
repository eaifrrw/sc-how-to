# Requesting an Interactive Node on the SGE Cluster

# Introduction
This guide provides step-by-step instructions on how to request an interactive node on the Sun Grid Engine (SGE) cluster.

# Prerequisites
- Access to the SGE cluster.
- A valid user account on the cluster.

# Steps to Request an Interactive Node

1. **Open a Terminal**
    - Access your terminal application on your local machine or connect to the cluster via SSH.

2. **Load the Required Modules (if necessary)**
    - Depending on your environment, you may need to load specific modules. Use the following command:
      ```bash
      module load <module_name>
      ```

3. **Request an Interactive Session**
    - Use the `qlogin` command with the `-pe` option to request an interactive session. You can specify the resources you need (e.g., number of slots, time limit) as follows:
      ```bash
      qsub -pe mpi 64 -l mem_free -l h=hostname
      ```
    - Replace `4G` with the desired memory and `hostname` with the specific node you want to use (example compute-0-0).

4. **Specify Additional Options (Optional)**
    - You can add more options to customize your request, such as:
      - `-q queue_name`: Specify the queue.
      - `-l h_rt=01:00:00`: Set the maximum run time (1 hour in this example).

5. **Connect to the Interactive Node**
    - Once your request is accepted, you will be connected to the interactive node, and you can start executing your commands.

6. **End the Interactive Session**
    - To exit the interactive session, simply type:
      ```bash
      exit
      ```

# Further Information
For further assistance, please refer to the cluster documentation or contact the ICTP-EAIFR  research support team.