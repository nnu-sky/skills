# 参数与优化决策

来源核对：2026-09-12。以下是查阅入口与判断方法，不是通用 INCAR 模板。访问具体页面后核对其版本与目标 VASP 的适用性。

## 哪些文件决定计算

| 项目 | 需要判断的内容 |
|---|---|
| POSCAR | 晶胞、坐标、元素顺序、真空与约束是否表达目标体系 |
| POTCAR | 泛函配套的势、价电子选择、版本与元素顺序 |
| KPOINTS / KSPACING | 实际积分网格、偏移、任务所需采样；不能按原子数单独确定 |
| INCAR | 单点/弛豫/MD、能量与力精度、自旋、展宽、算法、应力及输出 |

官方入口：[POTCAR 准备](https://vasp.at/wiki/Preparing_a_POTCAR)、[电子基态计算](https://vasp.at/wiki/Computing_the_electronic_groundstate)。用现有参考结果或小范围收敛证据确认精度；能量/原子接近不保证逐原子力接近。

## 加速候选

| 候选 | 何时考虑 | 不可直接推广的原因 |
|---|---|---|
| vasp_gam | 实际 Γ-only 且所需功能支持 | 单点计算本身不代表只需 Γ 点；非共线/SOC等需核对程序变体 |
| OpenMP、CPU绑定、SMT | CPU参与阶段明显或绑核不正确 | 物理核与逻辑线程不等价；整机并发会争用核心 |
| MKL / FFTW / fftlib | 已识别 CPU FFT/矩阵热点或线程库配套问题 | MKL是数学库，不能保证替换后快；核对实际加载库和线程运行时 |
| NSIM | GPU能带分块效率不足 | 最优值随算法、规模、硬件变化，也可能增加内存 |
| KPAR | 多k点、多GPU且工作可均衡划分 | Γ-only没有多k点可分；单GPU任务不能靠它制造并行 |
| 多任务并发、MPS | 每个独立任务不能充分占用GPU | CPU、显存与执行单元会互相竞争，收益按成功完成量确认 |
| 本地临时盘、减少不需要的输出 | 日志证明I/O或传输占比高 | WAVECAR/CHGCAR可能用于恢复或后处理，不能一律禁写 |
| LREAL、ALGO等 | 有明确精度/收敛和性能权衡 | 可能改变结果或收敛路径，应单列而非宣称纯执行加速 |

官方：[并行优化](https://vasp.at/wiki/Optimizing_the_parallelization)、[GPU实现](https://vasp.at/wiki/GPU_ports_of_VASP)、[OpenMP与MPI](https://vasp.at/wiki/Combining_MPI_and_OpenMP)、[MKL/OpenMP编译模板](https://vasp.at/wiki/Makefile.include.nvhpc_ompi_mkl_omp_acc)、[LREAL](https://vasp.at/wiki/LREAL)。GPU路径不照搬CPU NCORE调参；严格以所用版本为准。

MPS允许不同进程的GPU工作重叠，改善小任务共享效率：[NVIDIA说明](https://docs.nvidia.com/deploy/mps/latest/index.html)。查阅[适用条件与限制](https://docs.nvidia.com/deploy/mps/when-to-use-mps.html)时特别核对驱动版本、客户端归属、错误影响范围和安全退出。active-thread percentage 是资源使用上限，不能当成独占预留；不要直接把宿主机所有其他用户任务纳入同一服务。

## 发现新优化的方法

按已有证据定位计算、CPU、传输、同步、初始化或排队损失。官方文档用于功能与支持条件，维护者代码、HPC教程和论文用于提出候选，本项目短对照决定是否保留。结论记录输入规模、算法、程序/库版本、并发负载、计时范围、显存及能量/力差异。换体系时复核受影响部分，不重跑整套优化。

[ENCCS VASP实践](https://github.com/ENCCS/vasp-best-practices)可用于寻找常见配置问题，但教学示例不是任意体系的生产配方。

## 复用组件

- [Custodian](https://github.com/materialsproject/custodian)：VASP错误识别与恢复。只接入选定处理器；部分恢复会更改INCAR，需保留尝试历史。
- [atomate2](https://github.com/materialsproject/atomate2)：参考结构化输入、标准任务和结果组织；已有DP-GEN2项目不为单次优化整体迁移。
- [quacc](https://github.com/Quantum-Accelerators/quacc)：参考ASE计算器与工作流适配边界；不是自动硬件调参保证。
- [AiiDA-VASP](https://aiida-vasp-plugin.readthedocs.io/en/latest/)：参考可追溯流程；采用完整框架前评估部署和迁移成本。
