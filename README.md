# Survey on Physics Engines, Simulation Frameworks, and Benchmarks for Robot Learning
This is the accompanying repository from the paper "Survey on Physics Engines, Simulation Frameworks, and Benchmarks for Robot Learning." This repository tracks updates in the field following our definition of Physics Engines, Simulation Frameworks, and Benchmarks in the robot learning domain. We include a curated list of tools for each type of software, but more exhaustive lists can be found in other repositories (see the [best-of-robot-simulators](https://github.com/knmcguire/best-of-robot-simulators) for example). 


## Comparison of features across physics engines typically used in Robot Learning 

This table provides a side-by-side overview of the core capabilities and trade-offs offered by the most popular physics engines in robot learning. Each column highlights a key dimension—accuracy, GPU acceleration, joint configurability, soft-body support, contact solver behavior, documentation quality, open-source status, sensor modalities, multi-agent scalability, and ease of physics parameter tuning for domain randomization. Use it to quickly spot which engines are best suited for high-precision manipulation tasks (e.g., MuJoCo, Chrono), GPU-parallelized large-scale training (e.g., PhysX, MJX), or rich soft-body interaction (e.g., Bullet, Chrono).

| Physics Engine | Accuracy | GPU | 6-DoF Configurable Joint | Soft Body Support | Contact Solver Characteristics | Docs | Open Source | Sensor Support | Multi-agent Scalability | Physics Params Support |
|---|---|---|---|---|---|---|---|---|---|---|
| Mujoco | High | ❌ | ❌ | ❌ | No internal forces, Robust, Convergence guarantees | Comprehensive | ✅ | Limited (Camera, no LiDAR) | Limited | High |
| MJX | Medium | ✅ | ❌ | ❌ | No internal forces, Robust, Convergence guarantees | Comprehensive | ✅ | Limited (inherits MuJoCo's model) | Support with JAX | Medium |
| Bullet | Medium | ~ | ✅ | ✅ | Hard contacts | Well-documented | ✅ | Moderate | CPU bottlenecks | Medium |
| Havok | Low | ❌ | ✅ | ✅ | Not strict convergence | Limited documentation | ❌ | Very limited | Limited | Low |
| ODE | Low | ❌ | ❌ | ❌ | Hard contacts | Partially documented | ✅ | Very limited | Limited | Medium |
| PhysX | Medium | ✅ | ✅ | ✅ | Hard contacts | Well-documented | ✅ | Moderate | High | Medium |
| Dart | High | ❌ | ❌ | ❌ | Hard contacts | Well-documented | ✅ | Good | Good | High |
| Genesis | Medium | ✅ | ❌ | ✅ | ~ | Partially documented | ✅ | Limited | Moderate | Medium |
| Chrono | High | ✅ | ✅ | ✅ | Hard contacts | Well-documented | ✅ | Comprehensive | Moderate | High |

## Comparison of Simulation Frameworks for Robot Learning

Simulation frameworks wrap a physics engine in high-level tooling for robot modeling, environment construction, sensor emulation, and experiment management. This table compares their native interoperability with learning libraries, support for curriculum and domain randomization (both physical and visual), rendering fidelity, proven sim-to-real workflows, and out-of-the-box support for locomotion, manipulation, and navigation tasks. “✅” means full built-in support, “~” indicates partial or emerging capabilities, and “❌” means none. Choose a framework that matches your workflow needs—whether that’s top-tier rendering for vision-based manipulation (e.g., Unity, IsaacSim), flexible randomization APIs for robust policy training (e.g., MuJoCo Playground, SAPIEN), or strong multi-agent and navigation features (e.g., Habitat, CARLA).

| Frameworks | IsaacSim | SAPIEN | Unity | CoppeliaSim | Gazebo | CARLA | Habitat | AI2Thor | Robosuite | iGibson | MuJoCo Playground | PyBullet |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Interoperability with Learning Frameworks | ✅ | ✅ | ✅ | ~ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ~ |
| Domain Randomization Curriculum | ~ | ~ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| Visual Domain Randomization | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ~ | ❌ | ❌ | ~ |
| High Fidelity Rendering Support | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ~ | ✅ | ✅ | ❌ | ❌ |
| Sim-to-Real Track Record | ✅ | ✅ | ❌ | ~ | ~ | ❌ | ~ | ~ | ~ | ❌ | ❌ | ✅ |
| Locomotion Support | ✅ | ~ | ~ | ~ | ~ | ❌ | ❌ | ❌ | ❌ | ~ | ✅ | ✅ |
| Manipulation Support | ✅ | ✅ | ~ | ✅ | ~ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| Navigation Support | ~ | ~ | ✅ | ~ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ~ |

## Comparison of Benchmarks for Robot Learning

Benchmarks offer standardized tasks and evaluation protocols so that algorithms can be rigorously compared. In this table you’ll find each benchmark’s target domains (manipulation, locomotion, navigation), whether it offers diverse reward structures, environment complexity, built-in sim-to-real evaluations, visual robustness tests, and the overall breadth of tasks included. Use this to pick a benchmark aligned with your research focus—whether that’s long-horizon compositional manipulation (e.g., CALVIN, ManiSkill), multi-domain challenges (e.g., RoboHive, HumanoidBench), or navigation-specific suites (e.g., Habitat Challenge).

| Benchmark | Domains Supported | Reward Diversity | Environment Complexity | Sim2Real | Visual Robustness | Diversity of Tasks |
|---|---|---|---|---|---|---|
| Mujoco Playground | Manipulation, Locomotion | ~ | ❌ | ~ | ~ | ~ |
| DeepMind Control | Locomotion | ❌ | ❌ | ❌ | ❌ | ❌ |
| OGBench | Manipulation | ~ | ❌ | ❌ | ~ | ✅ |
| RoboHive | Manipulation, Locomotion | ✅ | ✅ | ✅ | ~ | ✅ |
| Meta-World | Manipulation | ✅ | ~ | ~ | ~ | ✅ |
| RlBench | Manipulation | ✅ | ✅ | ✅ | ✅ | ✅ |
| ManiSkill | Manipulation | ✅ | ✅ | ~ | ✅ | ✅ |
| DMC-VB | Manipulation | ~ | ❌ | ❌ | ~ | ~ |
| DMC-GB2 | Manipulation, Locomotion | ~ | ❌ | ❌ | ~ | ~ |
| VD4RL | Manipulation | ~ | ~ | ❌ | ✅ | ~ |
| RL-ViGen | Manipulation | ~ | ~ | ❌ | ✅ | ✅ |
| CALVIN | Manipulation | ✅ | ✅ | ✅ | ✅ | ✅ |
| Colosseum | Manipulation | ~ | ~ | ~ | ~ | ~ |
| HumanoidBench | Manipulation, Locomotion | ❌ | ✅ | ❌ | ✅ | ✅ |
| LocoMuJoCo | Locomotion | ✅ | ❌ | ~ | ❌ | ✅ |
| Habitat Challenge | Navigation | ✅ | ✅ | ✅ | ✅ | ~ |

### Task-Specific Resources for Robot Learning
Beyond general simulation comparisons, it's often helpful to look at task-specific research and implementations. This section curates representative works and public repositories categorized by robotic capabilities such as locomotion, manipulation, and navigation. Each table includes references to learning-based approaches, real-world deployments, and sim-to-real workflows for specific robot platforms.
#### Locomotion Resources for Legged Robots
|  | **A1** | **Go1** | **H1** | **Anymal** | **spot** | **cassie** | **solo12** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **MuJoCo** | [A Walk in the Park: Learning to Walk in 20 Minutes With Model-Free Reinforcement Learning](https://arxiv.org/pdf/2208.07860) <br> <br> [Reinforcement Learning with Evolutionary Trajectory Generator: A General Approach for Quadrupedal Locomotion](https://arxiv.org/pdf/2109.06409) | [SLIM: Sim-to-Real Legged Instructive Manipulation via Long-Horizon Visuomotor Learning](https://arxiv.org/pdf/2501.09905) | [unitree_rl_gym](https://github.com/unitreerobotics/unitree_rl_gym) |  |  | [Reinforcement Learning for Versatile, Dynamic, and Robust Bipedal Locomotion Control](https://arxiv.org/pdf/2401.16889) [Sim-to-Real Learning for Bipedal Locomotion Under Unsensed Dynamic Loads](https://arxiv.org/pdf/2204.04340) <br> <br> [Learning Locomotion Skills for Cassie: Iterative Design and Sim-to-Real](https://proceedings.mlr.press/v100/xie20a/xie20a.pdf) | | 
| **IsaacGym/IsaacSim** | [Unified Locomotion Transformer with Simultaneous Sim-to-Real Transfer for Quadrupeds](https://arxiv.org/html/2503.08997v1) <br> <br> [CPG-RL: Learning Central Pattern Generators for Quadruped Locomotion](https://arxiv.org/pdf/2211.00458) <br> <br>  [HYBRID INTERNAL MODEL: LEARNING AGILE LEGGED LOCOMOTION WITH SIMULATED ROBOT RESPONSE](https://arxiv.org/pdf/2312.11460) <br> <br>  [Robot Parkour Learning](https://robot-parkour.github.io/resources/Robot_Parkour_Learning.pdf) <br> <br>  [Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning](https://arxiv.org/pdf/2109.11978) | [Robot Parkour Learning](https://robot-parkour.github.io/resources/Robot_Parkour_Learning.pdf) | [unitree_rl_gym](https://github.com/unitreerobotics/unitree_rl_gym) <br> <br> [Humanoid Parkour Learning](https://humanoid4parkour.github.io/resources/humanoid-parkour-learning-paper.pdf) <br> <br>  [A Unified and General Humanoid Whole-Body Controller for Fine-Grained Locomotion](https://arxiv.org/html/2502.03206v2) | [Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning](https://arxiv.org/pdf/2109.11978) |  | [Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning](https://arxiv.org/pdf/2109.11978) | [CaT: Constraints as Terminations for Legged Locomotion Reinforcement Learning](https://arxiv.org/pdf/2403.18765) | 
| **PyBullet** | [Robust High-Speed Running for Quadruped Robots via Deep Reinforcement Learning](https://arxiv.org/pdf/2103.06484) <br> <br> [LEARNING VISION-GUIDED QUADRUPEDAL LOCOMOTION END-TO-END WITH CROSS-MODAL TRANSFORMERS](https://openreview.net/pdf?id=nhnJ3oo6AB) <br> <br> [GenLoco: Generalized Locomotion Controllers for Quadrupedal Robots](https://arxiv.org/pdf/2209.05309) | [GenLoco: Generalized Locomotion Controllers for Quadrupedal Robots](https://arxiv.org/pdf/2209.05309) |  | [GenLoco: Generalized Locomotion Controllers for Quadrupedal Robots](https://arxiv.org/pdf/2209.05309) |  |  | [Model-free reinforcement learning for robust locomotion using demonstrations from trajectory optimization](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.854212/full) |
| **RaiSIM** |  |  |  | [Learning Agile and Dynamic Motor Skills for Legged Robots](https://arxiv.org/pdf/1901.08652) <br> <br> [Learning Quadrupedal Locomotion over Challenging Terrain](https://arxiv.org/pdf/2010.11251) <br> <br> [RLOC: Terrain-Aware Legged Locomotion using Reinforcement Learning and Optimal Control](https://arxiv.org/pdf/2012.03094) |  |  | [Controlling the Solo12 Quadruped Robot with Deep Reinforcement Learning](https://laas.hal.science/hal-03761331v2/file/Scientific_Reports.pdf) | 
| **Gazebo** | [Robust High-Speed Running for Quadruped Robots via Deep Reinforcement Learning](https://arxiv.org/pdf/2103.06484) | [Robust Localization, Mapping, and Navigation for Quadruped Robots](https://arxiv.org/html/2505.02272v1) |  |  | [Spot_simulation](https://github.com/SoftServeSAG/spot_simulation/tree/spot_control) |  |  |

Note: We only list the latest commercially available or open‐source versions of legged robots that multiple research labs have used. Contributions are welcome via pull request.

# Learning-Based Manipulation Resources for Dexterous Robots

| Simulator | Franka | Humanoid robot Digit | ANYmal + arm | ANYmal (using feet for manipulation) | Unitree Go2 + arm | Unitree Go1 + arm | Unitree B1 + arm | Xbot | UR5e Robot | Berkeley BLUE Robot arm | Shadow Dexterous Hand | Fourier GR-1 Humanoid Robot | A2Single | DEX-EE Hand | ALOHA | Unitree H1 | Unitree G1 | Franka Emika | Toyota HSR robot | Unitree Aliengo + Z1 arm | Aliengo (Using feet for manipulation) |
|-----------|--------|---------------------|--------------|-------------------------------------|-------------------|-------------------|------------------|------|------------|-------------------------|----------------------|------------------------------|----------|-------------|--------|------------|------------|--------------|-------------------|----------------------|---------------------------------------|
| **MuJoCo** | [Curriculum Design and Sim2Real Transfer for Reinforcement Learning in Robotic Dual-Arm Assembly](https://www.mdpi.com/2075-1702/12/10/682)<br><br>[Learning to Manipulate Anywhere: A Visual Generalizable Framework For Reinforcement Learning](https://arxiv.org/pdf/2407.15815) | [Sim-to-Real Learning for Humanoid Box Loco-Manipulation](https://arxiv.org/pdf/2310.03191) | | | | | | | | [DoorGym: A Scalable Door Opening Environment and Baseline Agent](https://arxiv.org/pdf/1908.01887) | [Solving Rubik's Cube with a Robot Hand](https://arxiv.org/abs/1910.07113)<br><br>[Learning Dexterous In-Hand Manipulation](https://arxiv.org/pdf/1808.00177)<br><br>[Learning to Solve a Rubik's Cube with a Dexterous Hand](https://arxiv.org/pdf/1907.11388) | | | [DemoStart: Demonstration-led auto-curriculum applied to sim-to-real with multi-fingered robots](https://arxiv.org/pdf/2409.06613) | [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](https://arxiv.org/abs/2304.13705) | | [FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation](https://arxiv.org/abs/2505.06776) | | | | |
| **IsaacGym/IsaacSim** | | | [Learning to Open and Traverse Doors with a Legged Manipulator](https://arxiv.org/pdf/2409.04882)<br><br>[Guided Reinforcement Learning for Robust Multi-Contact Loco-Manipulation](https://arxiv.org/pdf/2410.13817) | [Pedipulate: Enabling Manipulation Skills using a Quadruped Robot's Leg](https://arxiv.org/pdf/2402.10837) | [UMI on Legs: Making Manipulation Policies Mobile with Manipulation-Centric Whole-body Controllers](https://umi-on-legs.github.io/static/umi-on-legs.pdf) | [Deep Whole-Body Control: Learning a Unified Policy for Manipulation and Locomotion](https://www.notion.so/Learning-Based-Manipulation-Resources-for-Dexterous-Robots-21069d26f6e3809b9227c24930149f72?pvs=21) | [Learning Force Control for Legged Manipulation](https://arxiv.org/html/2405.01402v2)<br><br>[Visual Whole-Body Control for Legged Loco-Manipulation](https://arxiv.org/pdf/2403.16967) | [HYPERmotion: Learning Hybrid Behavior Planning for Autonomous Loco-manipulation](https://openreview.net/pdf?id=ma7McOiCZY) | | | | [Sim-to-Real Reinforcement Learning for Vision-Based Dexterous Manipulation on Humanoids](https://arxiv.org/pdf/2502.20396) | | | | [Unleashing Humanoid Reaching Potential via Real-world-Ready Skill Space](https://arxiv.org/abs/2505.10918) | [AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control](http://arxiv.org/pdf/2505.03738) | | | | [Learning Visual Quadrupedal Loco-Manipulation from Demonstrations](https://arxiv.org/pdf/2403.20328) |
| **PyBullet** | | | | | | | | | | [Transporter Networks: Rearranging the Visual World for Robotic Manipulation](https://arxiv.org/pdf/2010.14406) | | | | | | | | | | | |
| **RaiSIM** | | | | | | | | | | | | | | | | | | | | | |
| **Gazebo** | | | | | | | | | | | | | | | | | | | | | |
| **SAPIEN / ManiSkill** | | | | | | | | | | | | | [Learning Generalizable Manipulation Policy with Adapter-Based Parameter Fine-Tuning](https://ieeexplore.ieee.org/abstract/document/10801544?casa_token=-VomzwGsfToAAAAA:iF6L4PWbRuBZedrKjWYWfBNZCS4FC6tB_VXcOcjKEubQJCYPvDnUWuKfOpSZI7grVqmy-wSW8A) | | | | | | [Ag2Manip: Learning Novel Manipulation Skills with Agent-Agnostic Visual and Action Representations](https://ieeexplore.ieee.org/abstract/document/10801835?casa_token=jSN8ymJUTxYAAAAA:f0LL_tY02mcP1tWMV4Mw8p9Cq-TVG8PyXE6wDA2g6hkzkLzzGYqFS2ebs1TUMAaabE0HHsVIww) | [Learning Generalizable Manipulation Policy with Adapter-Based Parameter Fine-Tuning](https://ieeexplore.ieee.org/abstract/document/10801544?casa_token=-VomzwGsfToAAAAA:iF6L4PWbRuBZedrKjWYWfBNZCS4FC6tB_VXcOcjKEubQJCYPvDnUWuKfOpSZI7grVqmy-wSW8A) | [Learning Generalizable Manipulation Policy with Adapter-Based Parameter Fine-Tuning](https://ieeexplore.ieee.org/abstract/document/10801544?casa_token=-VomzwGsfToAAAAA:iF6L4PWbRuBZedrKjWYWfBNZCS4FC6tB_VXcOcjKEubQJCYPvDnUWuKfOpSZI7grVqmy-wSW8A) | |
| **Unity** | | | | | | | | | | [DoorGym: A Scalable Door Opening Environment and Baseline Agent](https://arxiv.org/pdf/1908.01887) | | | | | | | | | | | |
| **CoppeliaSim** | | | | | | | | | | | | | | | | | | | | | |
| **iGibson** | | | | | | | | | | | | | | | | | | | | | |
| **Robosuite** | [Curriculum Design and Sim2Real Transfer for Reinforcement Learning in Robotic Dual-Arm Assembly](https://www.mdpi.com/2075-1702/12/10/682) | | | | | | | | | | | | | | | | | | | | |

**Note:** We only list the latest commercially available or open-source versions of legged robots that have been used by multiple research labs. If you know of any additional papers or repositories that are not shown here, feel free to open a pull request.

## Changelog

This section will track all major updates to the engines, frameworks, and benchmarks covered in this survey. Whenever a new major version is released, capabilities are added or changed, or entirely new entries appear, record the date, the tool affected, and a short description of what’s new.

| Date | Tool | Change Description | Notes / Links |
| ---- | ---- | ------------------ | ------------- |
| June 2025  | NA   | Initial Commit of Resources after paper submission                  | –             |

*Entries will be added here as releases are announced or new tools are included.*
