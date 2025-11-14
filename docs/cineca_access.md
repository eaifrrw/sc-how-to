# 11.0 Tutorial Guide: Accessing the Leonardo Supercomputer (CINECA)

This guide walks you through the process of setting up secure SSH authentication and file transfer between your local machine and the Leonardo HPC system at CINECA.

---

## 11.1 Prerequisites

Before starting, make sure:
- You have an active **CINECA UserDB account**.
- You’ve installed the required tools:
  - `step` (for SSH certificate authentication)
  - `google-authenticator` (for one-time passwords)
- You’re working in a Linux or macOS terminal.

---

## 11.2 Generate Your SSH Key

Create a new SSH key pair named after your CINECA username:

```bash
ssh-keygen -t ecdsa
```

When prompted for a file name, use:
```
~/.ssh/<username>
```

---

## 11.3 Start the SSH Agent Automatically

Add this line to your `~/.bashrc` to start the SSH agent automatically:

```bash
eval "$(ssh-agent -s)"
```

Then reload it:

```bash
source ~/.bashrc
```

---

## 11.4 Create an Authentication Alias

Add an alias to your `~/.bashrc` or `~/.bash_aliases` file (replace `<username>` with your actual username):

```bash
alias authleonardo="rm -f ~/.ssh/*<username>* && step ssh certificate '<username>' --provisioner cineca-hpc ~/.ssh/<username>"
```

Reload the shell:

```bash
source ~/.bashrc
```

---

## 11.5 Authenticate with Leonardo

Run:

```bash
authleonardo
```

You’ll be redirected to the **CINECA login portal**.  
Enter your username, password, and OTP.  
When you see “Success,” your SSH certificate has been generated.

---

## 11.6 Configure SSH Access

Edit your SSH configuration file:

```bash
nano ~/.ssh/config
```

Add:

```
Host leonardo
    StrictHostKeyChecking=no
    UserKnownHostsFile=/dev/null
    LogLevel ERROR
    User <username>
    Hostname login.leonardo.cineca.it
    IdentityFile ~/.ssh/<username>

Host leonardodata
    StrictHostKeyChecking=no
    UserKnownHostsFile=/dev/null
    LogLevel ERROR
    User <username>
    Hostname data.leonardo.cineca.it
    IdentityFile ~/.ssh/<username>
```

---

## 11.7 Transferring Files

Authenticate first:

```bash
authleonardo
```

### Upload (Local → Remote)
```bash
scp -r /path/to/local/dir leonardo:/leonardo_scratch/large/userexternal/<username>/Project/
```

### Download (Remote → Local)
```bash
scp -r leonardo:/leonardo_scratch/large/userexternal/<username>/Project/ /path/to/local/dir
```

### Use `rsync` (Recommended)
```bash
rsync -PravzHS leonardodata:/leonardo_scratch/large/userexternal/<username>/Project/ /path/to/local
```

---

## 11.8 Summary Checklist

| Step | Task | Command |
|------|------|----------|
| 1 | Generate SSH key | `ssh-keygen -t ecdsa` |
| 2 | Start SSH agent | `eval "$(ssh-agent -s)"` |
| 3 | Add alias | `alias authleonardo="..."` |
| 4 | Authenticate | `authleonardo` |
| 5 | Configure SSH | `~/.ssh/config` |
| 6 | Transfer files | `scp` or `rsync` |

---

## 11.9 Troubleshooting Tips

| Problem | Cause | Solution |
|----------|--------|----------|
| Permission denied | Not authenticated | Run `authleonardo` again |
| Host key verification failed | Old cached host keys | `ssh-keygen -R login.leonardo.cineca.it` |
| No such file or directory | Wrong path | Verify directory paths |

---

---
## 11.10 Addtional Information

### To Regenerate the certs:
```bash
$ step ssh login '<user-email>' --provisioner cineca-hpc
```

It is possible to check for the presence of a valid certificate either via ssh-agent 
or via step with one of the following commands:
```bash
$ ssh-add -L
```
```bash
ecdsa-sha2-nistp256-cert-v01@openssh.com AAAAKGVjZHNhLXNoYTItbmlzdHAyNTYtY2VydC12MDFAb3BlbnNzaC5jb20AAAAgYjJfSnpeTTNrMHB4Lm9yX3YjZWNxXyRxcHM9blRzU1gAAAAIbmlzdHAyNTYAAABBBAJRZ11/PIo0VJknlFMDa5BIaJp/w0OWd95ueZbWlQ4uG92aSZ+K8aKgkyDiOGla3x7l+saVT/pIR+x3zBgvwgkLrbmYufPPVAAAAA
EAAAAUbS5tb3Jnb3R0aUBjaW5lY2EuaXQAAAAMAAAACG1tb3Jnb3R0AAAAAGILhpwAAAAAYgv3HAAAAAAAAACCAAAAFXBlcm1pdC1YMTEtZm9yd2FyZGluZwAAAAAAAAAXcGVybWl0LWFnZW50LWZvcndhcmRpbmcAAAAAAAAAFnBlcm1pdC1wb3J0LWZvcndhcmRpbmcAAAAAAAAACnBlcm1pdC1wdHkAAAAAAAAADnBlcm1pdC11c2VyLXJjAAAAAAAAAAAAAABoA
AAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBAE3K7f5piMLWXDm9c6kd+VAJmBClKXkQ9i/8E1UA9DcBFofX+r9JyBOULZSDkGtr84oqpNX0fa5DMCar3AQp1YAAABkAAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAABJAAAAIDg33ohPQ6BgzV1ATGsSVSbRwrbYa8LprV2EEHk4mMgWAAAAIQCkd8QKYS+zbeyD1nXeuRAXVWJXJeoxMScgDVx2
qqu2Mg== <user-email>
```
```bash
$ step ssh list
```
```bash
256 SHA256:x+QEW8xmDBtRjVRtAukc7v7zKEHef/9joyFP9n/gZtk <user_email> (ECDSA-CERT)
```

### To Check if certificates are valid:
To check if the certificates are still valid

```bash
$ step ssh list --raw  '<user_email>' | step ssh inspect
```
```bash
-:
 Type: ecdsa-sha2-nistp256-cert-v01@openssh.com user certificate
 Public key: ECDSA-CERT SHA256:TdhIpD5KFZD37roGYcDstS7180TruOnNgNJeS8eJJPk
 Signing CA: ECDSA SHA256:e0ZF6AnnUzi0g7Db9nOaXxkEjRq9D6Ka4tV04XqiIgM
 Key ID: "<user_email>"
 Serial: 841532770994081620
 Valid: from 2025-05-12T11:55:24 to 2025-05-12T19:55:24
 Principals:
          <username>
 Critical Options: (none)
 Extensions:
          permit-X11-forwarding
          permit-port-forwarding
          permit-pty 
```

### To avoid using ssh-agent, do the following:

Download your certificate launching the following command in any path 
of your local PC (we suggest using the ~/.ssh folder)
```bash
$ step ssh certificate 'user-email' --provisioner cineca-hpc my_key
```
---
