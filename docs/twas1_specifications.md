# TWAS-1 Cluster Architecture and Capabilities

## Overview

The **TWAS-1 Cluster** is a tightly controlled, high-performance computing (HPC) resource tailored for compute-intensive scientific research, data analytics, and numerical modeling. The system is deployed as part of the **QUEVEDO Cluster** configuration and is optimized to exploit modern Intel server-class processor features.

See [TWAS-1 Ganglia Dashboard] by `Grid` -> `--Choose a Source` (Click on `Choose a Source` and select `twas1`).

[TWAS-1 Ganglia Dashboard]: http://154.68.126.3/ganglia/?r=hour&cs=&ce=&m=load_one&s=by+name&c=twas1&tab=m&vn=&hide-hf=false
 

---
 ## Access and Resource Governance
 Access to the TWAS-1 Cluster is **highly restricted**, ensuring predictable performance and efficient allocation to approved research projects. Regular maintenance and data hygiene policies are enforced to preserve system integrity and long-term reliability. Unauthorized access will suggests a cybersecurity breach.

## Compute Architecture

The TWAS-1 Cluster consists of **three compute nodes**, each powered by **dual Intel® Xeon® Gold 5218R processors**, delivering the following capabilities:

- **80 logical CPUs per node**
  - 2 sockets × 20 cores per socket × 2 threads (Hyper-Threading)
- **NUMA-aware architecture**
  - Two NUMA nodes per system, enabling memory-locality–optimized parallel workloads
- **92 GB DDR4 RAM per node**
  - Well suited for memory-intensive simulations and in-memory analytics

---

## Advanced Instruction Set Support

The CPUs expose a comprehensive set of modern instruction extensions, enabling high efficiency across a wide range of scientific and data-driven workloads.

### Vectorization & Floating-Point Performance

- SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2
- AVX, AVX2, and full **AVX-512** support:
  - AVX-512F, DQ, CD, BW, VL
- **AVX-512 VNNI** for accelerated deep learning inference and mixed-precision workloads
- **FMA (Fused Multiply-Add)** and **F16C** for optimized numerical kernels

### Cryptography & Security Acceleration

- AES-NI, PCLMULQDQ, RDRAND, RDSEED, ADX
- Hardware-level mitigations for speculative execution vulnerabilities:
  - IBRS, STIBP, SSBD, MD_CLEAR
- NX (No-Execute) and SMEP/SMAP for robust memory protection

---

## Virtualization and Isolation

The cluster supports advanced virtualization and isolation features, enabling flexible and secure execution environments:

- Intel VT-x with EPT and VPID for efficient virtual machines and containerized workloads
- Flexible privilege management via PKU/OSPKE
- Hardware support for secure multi-tenant execution where required

---

## Cache and Memory Hierarchy

To sustain high throughput and reduce memory latency, the system provides:

- Per-core L1 instruction and data caches (32 KB each)
- 1 MB L2 cache per core
- ~28 MB shared L3 cache per socket
- Cache Allocation Technology (CAT) and Memory Bandwidth Allocation (MBA) for fine-grained resource control across workloads

---

## Performance Monitoring and Optimization

The TWAS-1 Cluster provides extensive observability and tuning capabilities:

- Architectural performance monitoring:
  - `arch_perfmon`, PEBS, Intel PT
- Constant and invariant TSC for precise timing
- NUMA topology awareness for scalable MPI and OpenMP applications

---

## Intended Use Cases

Thanks to its instruction-rich CPUs and balanced memory design, the TWAS-1 Cluster is particularly well suited for:

- Large-scale numerical simulations (climate, physics, engineering)
- Machine learning inference and vectorized analytics
- High-throughput data processing and statistical modeling
- Cryptography-aware and security-sensitive research workloads
- Virtualized or containerized scientific environments

---

