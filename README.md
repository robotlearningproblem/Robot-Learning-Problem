# Survey on Physics Engines, Simulation Frameworks, and Benchmarks for Robot Learning
This is the accompanying repository from the paper "Survey on Physics Engines, Simulation Frameworks, and Benchmarks for Robot Learning." This repository tracks updates in the field following our definition of Physics Engines, Simulation Frameworks, and Benchmarks in the robot learning domain.


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
| Locomotion Support | ✅ | ✅ | ~ | ~ | ~ | ❌ | ❌ | ❌ | ❌ | ~ | ✅ | ✅ |
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


## Changelog

This section will track all major updates to the engines, frameworks, and benchmarks covered in this survey. Whenever a new major version is released, capabilities are added or changed, or entirely new entries appear, record the date, the tool affected, and a short description of what’s new.

| Date | Tool | Change Description | Notes / Links |
| ---- | ---- | ------------------ | ------------- |
| –    | –    | –                  | –             |

*Entries will be added here as releases are announced or new tools are included.*
