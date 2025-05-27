# Survey on Physics Engines, Simulation Frameworks, and Benchmarks for Robot Learning
This is the accompanying repository from the paper "Survey on Physics Engines, Simulation Frameworks, and Benchmarks for Robot Learning." This repository tracks updates in the field following our definition of Physics Engines, Simulation Frameworks, and Benchmarks in the robot learning domain.


## Comparison of features across physics engines typically used in Robot Learning 
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
