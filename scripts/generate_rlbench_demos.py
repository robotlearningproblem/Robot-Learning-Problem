import numpy as np
from PIL import Image
from rlbench.action_modes.action_mode import MoveArmThenGripper
from rlbench.action_modes.arm_action_modes import EndEffectorPoseViaPlanning, RelativeFrame
from rlbench.action_modes.gripper_action_modes import Discrete
from rlbench.environment import Environment
from rlbench.observation_config import ObservationConfig, CameraConfig
from rlbench.tasks import FS10_V1

cam_cfg = CameraConfig(image_size=(512,512))
obs_config = ObservationConfig()
obs_config.front_camera = cam_cfg

arm_mode = EndEffectorPoseViaPlanning(
    absolute_mode=False,
    frame=RelativeFrame.WORLD,
    collision_checking=False
)
action_mode = MoveArmThenGripper(
    arm_action_mode=arm_mode,
    gripper_action_mode=Discrete()
)

env = Environment(action_mode, obs_config=obs_config, headless=False)
env.launch()

np.random.seed(0)
train_tasks = FS10_V1['train']
tasks = list(np.random.choice(train_tasks, size=10, replace=False))

# Here we move down 0.02 m (= 2 cm) per step for 10 steps = 0.2 m total
# This was done so that we can see the gripper in the previews
delta_xyz = [0.0, 0.0, -0.02]
identity_quat = [0.0, 0.0, 0.0, 1.0]
gripper_noop   = [0]
down_action = np.array(delta_xyz + identity_quat + gripper_noop,
                       dtype=np.float32)

for i, TaskClass in enumerate(tasks):
    task = env.get_task(TaskClass)
    task.sample_variation()
    descriptions, obs = task.reset()

    for _ in range(10):
        obs, reward, terminate = task.step(down_action)

    img = Image.fromarray(obs.front_rgb)
    img.save(f"rlbench_{TaskClass.__name__}_{i:02d}.png")
    print(f"Saved rlbench_{TaskClass.__name__}_{i:02d}.png")

env.shutdown()
