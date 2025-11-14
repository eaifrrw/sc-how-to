# 10.0 Requesting an Interactive Node 

## 10.1 Introduction
This guide provides step-by-step instructions on how to request an interactive node on the Sun Grid Engine (SGE) cluster.

## 10.1.1 Prerequisites
- Access to the SGE cluster.
- A valid user account on the cluster.

## 10.1.2 Steps to Request an Interactive Node

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
      qlogin -pe mpi 64 -l mem_free -l h=hostname
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

## 10.2 Graphic Based Applications

1. **Open a Terminal**
    - Access your terminal application on your local machine.

2. **Connect to the Cluster with X11 Forwarding**
    - Use the `ssh` command with the `-X` option to enable X11 forwarding. Replace `username` and `cluster_address` with your actual username and the address of the cluster (e.g. quevedo.eaifr.org):
      ```bash
      ssh -X username@quevedo.eaifr.org
      ```

3. **Load the Required Modules (if necessary)**
    - If VMD is not installed by default, load the necessary module:
      ```bash
      module load vmd
      ```

4. **Launch VMD**
    - Start VMD by typing the following command:
      ```bash
      vmd
      ```

5. **Use VMD for Visualization**
    - Once VMD is open, you can load your molecular structures and begin your visualization tasks.

6. **End the VMD Session**
    - To exit VMD, simply close the application window or type:
      ```bash
      exit
      ```



## 10.3 Further Information
Login to CINECA's HPC Infrastructure can be configured to ease access. See` :doc:`Section 11 <cineca_access>`

For further assistance, please refer to the cluster documentation or contact the ICTP-EAIFR  research support team.
