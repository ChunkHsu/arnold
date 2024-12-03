# Arnold
## Tips for Docker-based
- 关于原任务数据的使用：下载的数据可以放在`./workspace`下面
  ```sh
  workspace/
    ├── tasks/
    ├── Dockerfile
    ├── materials/
    ├── sample/
    └── Vagrantfile
  ```
- 项目的配置文件很重要： `./configs/default.yaml` 里面保护运行的环境、模型及任务等参数的指定路径

- 使用 wget 下载 Vagrant 软件包：
  ```sh
  curl -O https://releases.hashicorp.com/vagrant/2.2.9/vagrant_2.2.9_x86_64.deb
  sudo apt install ./vagrant_2.2.9_x86_64.deb
  vagrant --version
  ````
- [nvidia docker install](https://blog.csdn.net/yiqiedouhao11/article/details/141392752)