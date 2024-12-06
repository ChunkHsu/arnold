# Arnold

## Tips for Docker-based

- 关于原任务数据的使用：下载的数据可以放在`./workspace`下面
  
  ```sh
  workspace/
    ├── data/
    ├── Dockerfile
    ├── materials/
    ├── sample/
    └── Vagrantfile
  ```

- 项目的配置文件很重要： `./configs/default.yaml` 里面保护运行的环境、模型及任务等参数的指定路径

- 运行任务时需要先编译`./utils/compute_points.pyx` , 进入到 utils目录，`/isaac-sim/python.sh setup.py build_ext --inplace` 

## npz数据包含的属性
```json
"gt":[
  {
    "images": [ // 一个图像帧
      {
        "rgb": [[[0],[1]...[127]],],
        "depthLinear": [[],[],],  // 包含深度图像数据
        "camera": { // 包含相机相关的信息
          "pose": [[],[],], // 相机的位置和方向
          "fov": 1.3959954678, // 相机的视场角
          "focal_length": 12.4899959564, // 相机的焦距
          "horizontal_aperture":20.9549999237, // 相机的水平光圈大小
          "view_projection_matrix":[[,,,],[],], // 视图投影矩阵，用于将3D坐标转换为2D图像坐标
          "resolution":{ // 相机图像的分辨率
            "width": 128,
            "height": 128
          },
          "clipping_range": { // 定义了渲染时的裁剪范围
            "dimension": 2
          }
        },
        "semanticSegmentation": [[],],
        "state": {
          "rgb": true,
          "depthLinear": true,
          "semanticSegmentation": true
        }
      },...
    ],
    "semantic_id": {}, // 可能包含语义分割的标识符或标签
    "keyframe": false, // 指示当前帧是否是关键帧
    "instruction": "empty all water out of the cup", // 提供了机械臂执行任务的指令，例如“清空杯子里的所有水”
    "template_actions": null, // 可能包含预定义的动作模板
    "diff": 100.0, // 表示某种差异度量，可能是目标状态和当前状态之间的差异
    "robot_base": [[19.87,0.00,304.88],[-0.70,0.70,-0.00,0.00]], // 包含机械臂基座的位置和方向
    "position_rotation_world":[[65.95,38.83,304.32],[-0.25,0.29,-0.64,0.65]], // 包含机械臂末端执行器在世界坐标系中的位置和旋转
    "gripper_joint_positions":[4.0,3.99], // 包含夹持器关节的位置
    "joint_positions":[0.012,-0.57,-4.22,-2.80,0.0,3.09,0.74,4.0,3.99], // 包含机械臂所有关节的位置
    "joint_velocities":[0.0,2.90,0.0,-7.20,-0.0,-8.40,-0.0,-0.0,0.00], // 包含机械臂关节的速度
    "gripper_open":true, // 指示夹持器是否打开
    "target":[0,0] // 可能包含任务的目标位置或状态
  },...
]
'info':{
    "scene_parameters": {
        "usd_path": "/root/VRKitchen2.0/sample/house/0/layout.usd",
        "task_type": "pour_water",
        "traj_dir": "/root/VRKitchen2.0/translate/AWS/pour_water-0-0-2-0-0-0/trajectory",
        "floor_path": "floors",
        "wall_path": "roomStruct",
        "furniture_path": "furniture",
        "floor_material_url": "/root/VRKitchen2.0/materials/Wood/Ash.mdl",
        "wall_material_url": "/root/VRKitchen2.0/materials/Wall_Board/Cardboard.mdl"
    },
    "robot_parameters": {
        "usd_path": "/root/VRKitchen2.0/sample/robot/franka/franka.usd",
        "robot_position": [,,],
        "robot_orientation_quat": [,,,]
    },
    "objects_parameters": [
        {
            "usd_path": "/root/VRKitchen2.0/sample/custom/Cup/0/cup.usd",
            "scale": array([,,]),
            "object_position": [,,],
            "orientation_quat": [,,,],
            "object_type": "Cup",
            "args": {
                "annotator": "AWS",
                "task_type": "pour_water",
                "task_id": "0",
                "house_id": "0",
                "mission_id": "2",
                "robot_id": "0",
                "robot": {
                    "type": "franka",
                    "translate": [,,],
                    "orient": [,,,]
                },
                "objects": [
                    {
                        "asset_path": "./custom/Cup/0/cup.usd",
                        "obj_type": "Cup",
                        "obj_id": "0",
                        "materials": [],
                        "has_water": True,
                        "translate": [,,],
                        "orient": [,,,],
                        "scale": [,,]
                    }
                ],
                "state": (0, 0)
            },
            "object_physics_properties": {
                "collision": "convexDecomposition",
                "is_rigid_body": True
            },
            "part_physics_properties": {
                "cup_shape": {
                    "mass": 0.01,
                    "static_friction": 1.0,
                    "dynamic_friction": 1.0,
                    "restitution": 0.0,
                    "has_physics_material": True,
                    "collision": "convexDecomposition",
                    "is_rigid_body": False
                }
            },
            "fluid_properties": {
                "fluid_sphere_diameter": 0.72,
                "particle_system_schema_parameters": {
                    "contact_offset": 0.8999999999999999,
                    "particle_contact_offset": 0.75,
                    "rest_offset": 0.75,
                    "solid_rest_offset": 0,
                    "fluid_rest_offset": 0.44999999999999996,
                    "solver_position_iterations": 10,
                    "wind": Gf.Vec3f(0.0, 0.0, 0.0),
                    "max_velocity": 40
                },
                "particle_mass": 3e-07,
                "particle_color": array([,,])
            },
            "object_timeline_management": {
                "init_state": 0,
                "target_state": 0,
                "language_description": None,
                "target_joint": None
            }
        }
    ],
    "config": {
        "annotator": "AWS",
        "task_type": "pour_water",
        "task_id": "0",
        "house_id": "0",
        "mission_id": "2",
        "robot_id": "0",
        "robot": {
            "type": "franka",
            "translate": [,,],
            "orient": [,,,]
        },
        "objects": [
            {
                "asset_path": "./custom/Cup/0/cup.usd",
                "obj_type": "Cup",
                "obj_id": "0",
                "materials": [],
                "has_water": True,
                "translate": [,,],
                "orient": [,,,],
                "scale": [,,]
            }
        ],
        "state": (0, 0)
    },
    "robot_shift": [,,]
}
```

## 环境的配置

- 使用 wget 下载 Vagrant 软件包：
  
  ```sh
  curl -O https://releases.hashicorp.com/vagrant/2.2.9/vagrant_2.2.9_x86_64.deb
  sudo apt install ./vagrant_2.2.9_x86_64.deb
  vagrant --version
  ```

- nvidia docker的安装[nvidia docker install](https://blog.csdn.net/yiqiedouhao11/article/details/141392752)

## 进度

### 2024-12-05

1. 在`win10`中装了`wsl`、`docker desktop` ，在`wsl`中配置了`vagrant`环境，构建了 arnold 的 docker image

2. 在`wsl` 中运行的时候：
   
   - 解决了构建`Dockerfile`时不能拉取镜像的问题
   - 在使用`vagrant`构建虚拟机时，发现`wsl`缺少相关的挂载文件（与`vulkan`相关），尝试不挂载文件使用，能够正常构建虚拟机
   - 在虚拟机中运行`isaac sim`显示，不可用，显卡驱动问题（应该是与`vulkan`有关）

3. 在`win10`中装了`vagrant`，去构建环境所需的虚拟机，进入后显示缺少`vulkan`的文件
   
   - /etc/vulkan/implicit_layer.d/nvidia_layers.json
   - /etc/vulkan/icd.d/nvidia_icd.json  
     在网上没找到解决方案，遂放弃

4. 装双系统，先装了`ubuntu20.04`，但运行的时候与`cpu`有兼容性问题，屏幕显示扭曲、有雪花

5. 装`ubuntu22.04`，在系统中安装了`docker engine、 nvidia docker`、`vagrant`以及必备的软件，同时下载了`omniverse、Isaac Sim`，在宿主机上能够打开对应的`Isaac Sim`，尝试在`win10`中也装了`omniverse、Isaac Sim`但是不能用。于是就在`ubuntu22.04`中使用

6. 在`ubuntu22.04`使用`omniverse的Isaac Sim`构建了`WebUI`的页面，同时也测试了使用内网穿透来访问`Isaac Sim WebUI`服务，可以正常访问，至此、系统的一个重要的模块完成
   
   - http://127.0.0.1:8211/streaming/webrtc-client?server=127.0.0.1

7. 使用源码在`ubuntu22.04`中使用`Isaac Sim`的`python`运行，但是报错`导入模块错误`，但是源码中使用的是项目根目录下的`util`包，正常是不会报错...于是尝试在虚拟机中运行

8. 在`ubuntu22.04`中，使用`dockerfile`构建了`arnold`镜像，在`vagrant`使用此`arnold`镜像构建了虚拟机，在虚拟机中:
   
   - 部分官方样例可以运行
   
   - 运行源码的`task=pour_water model=eval use_gt=[1,1] visualize=1`验证数据集失败，显示`ERROR_OUT_OF_DEVICE_MEMORY`，内存/显存不足
     
     ```shell
     2024-12-03 16:28:27 [322,866ms] [Error] [carb.graphics-vulkan.plugin] VkResult: ERROR_OUT_OF_DEVICE_MEMORY
     2024-12-03 16:28:27 [322,866ms] [Error] [carb.graphics-vulkan.plugin] vkAllocateMemory failed for flags: 0.
     2024-12-03 16:28:27 [322,866ms] [Error] [gpu.foundation.plugin] Unable to allocate buffer
     2024-12-03 16:28:27 [322,866ms] [Error] [gpu.foundation.plugin] Buffer creation failed for the device: 0.
     2024-12-03 16:28:27 [322,866ms] [Error] [gpu.foundation.plugin] Failed to update params for RenderOp 572
     2024-12-03 16:28:27 [322,866ms] [Error] [gpu.foundation.plugin] Failed to update params for RenderOp Cached PT ClearAll. Will not execute this or subsequent RenderGraph operations. Aborting RenderGraph execution
     2024-12-03 16:28:27 [322,866ms] [Error] [carb.scenerenderer-rtx.plugin] Failed to execute RenderGraph on device 0. Error Code: 7 
     ```
   
   ```
   运行视频 `/home/chunk/Videos/录屏`
   ```

下一步打算看源码的运行框架结构



开题报告框架

- 算法端

- 数据部分

- 前端

- 后端

- 算法的意义相关工作（少）

- 方法相关工作意义（多）
