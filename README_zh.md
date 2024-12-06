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
