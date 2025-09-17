# 9.0 Transferring Data

## 9.1 Introduction
This guide provides instructions for transferring data to and from the Quevedo cluster (quevedo.eaifr.org). It covers both uploading and downloading files using secure methods.

## 9.2 Prerequisites
- Access to the Quevedo cluster.
- SSH client installed on your local machine.
- Basic knowledge of command line operations.

## 9.3 Transferring Data to the Quevedo Cluster

## 9.3.1 Using SCP (Secure Copy Protocol)

1. **Open your terminal.**
2. **Use the following command to upload files:**

    ```bash
    scp /path/to/local/file username@quevedo.eaifr.org:/path/to/remote/directory
    ```

    Replace `/path/to/local/file` with the path of the file you want to upload, `username` with your Quevedo username, and `/path/to/remote/directory` with the destination directory on the cluster.

3. **Example:**

    ```bash
    scp ~/Documents/myfile.txt user@quevedo.eaifr.org:/home/user/data/
    ```

## 9.3.2 Using SFTP (Secure File Transfer Protocol)

1. **Open your terminal.**
2. **Connect to the cluster using SFTP:**

    ```bash
    sftp username@quevedo.eaifr.org
    ```

3. **Use the following commands to upload files:**

    - Navigate to the desired remote directory:

      ```bash
      cd /path/to/remote/directory
      ```

    - Upload the file:

      ```bash
      put /path/to/local/file
      ```

4. **Example:**

    ```bash
    sftp user@quevedo.eaifr.org
    cd /home/user/data/
    put ~/Documents/myfile.txt
    ```

## 9.4 Transferring Data from the Quevedo Cluster

## 9.4.1 Using SCP

1. **Open your local terminal.**
2. **Use the following command to download files:**

    ```bash
    scp username@quevedo.eaifr.org:/path/to/remote/file /path/to/local/directory
    ```

3. **Example:**

    ```bash
    scp user@quevedo.eaifr.org:/home/user/data/myfile.txt ~/Downloads/
    ```

## 9.4.2 Using SFTP

1. **Open your terminal.**
2. **Connect to the cluster using SFTP:**

    ```bash
    sftp username@quevedo.eaifr.org
    ```

3. **Use the following commands to download files:**

    - Navigate to the desired remote directory:

      ```bash
      cd /path/to/remote/directory
      ```

    - Download the file:

      ```bash
      get filename
      ```

4. **Example:**

    ```bash
    sftp user@quevedo.eaifr.org
    cd /home/user/data/
    get myfile.txt
    ```

## 9.5 Conclusion
This guide provides the basic commands needed to transfer files to and from the Quevedo cluster. For more advanced usage, refer to the `man` pages of `scp` and `sftp` for additional options and features.