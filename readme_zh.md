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
