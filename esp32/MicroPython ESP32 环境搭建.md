# MicroPython ESP32 环境搭建

如果你之前已经熟练掌握 Python 或已经使用 Python 开发，那么可以直接使用你原来习惯的开发软件来编程。

如果你是初学者或者喜欢简单而快速应用，那么推荐使用 `Thonny`。`Thonny` 是一款开源软件，以极简方式设计，对 MicroPython 的兼容性非常友善。而且支持 Windows、Mac OS、Linux、树莓派。由于开源，所以软件迭代速度非常快，功能日趋成熟。使用 `Thonny` 还有两个方便之处，可直接在该软件中实现给 ESP32 单片机刷 MicroPython 固件，可以实时预览 ESP32 的文件系统。

`Thonny` 也不是没有缺陷的，由于其过于轻量化的设计，Thonny 不具备代码提示功能等很多开发者常用工具，但是对于初学者而言，依然是一款十分方便的 IDE。如果你觉得 PyCharm 更适合你的话，本节课也会教给你如何使用 PyCharm 开发 Micropython。

## 安装 Thonny

要在电脑上成功安装 `Thonny`，首先必须要有安装包，我们可以在 Thonny 官网下载：[https://thonny.org/open in new window](https://thonny.org/)，打开界面如下:

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202303011612792.png)

页面右上角有下载提示，根据电脑的系统选择不同的版本，然后下载即可。

如果感觉下载太慢，在我们的资料包中有 `thonny-4.0.1.exe`，可以直接使用。

下载好之后，鼠标右键点击 `Thonny` 安装程序，选择以管理员模式运行，之后就无脑点击 Next，选择好存放路径即可。

注意

注意：存放路径不能出现中文或特殊字符

如果能正常打开，说明安装成功。

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202303012108674.png)

之所以在下面的 shell 交互环境中有红色报错，是因为我们的 ESP32 中不存在 MicroPython 固件，因此，不用担心，咱们下一步就是烧录 ESP32 MicroPython 固件了。

## [#](#配置-micropython-开发环境) 配置 MicroPython 开发环境

首先，在 Thonny 中显示本地与开发板中的实时文件浏览窗口。

打开 Thonny 软件，点击`视图`选择`文件`，如下：

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202303012119268.png)

这时候，我们就看到了左侧出现本地和开发板的实时文件浏览窗口：

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202303012124807.png)

这时，我们看到在单片机中不存在任何文件，这也是为什么交互环境中报错的原因 - 没有 MicroPython 固件。

接下来，我们需要配置解释器并烧录固件到单片机中。

点击右下角，选择配置解释器。

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202303012127285.png)

在解释器页面，选择 `MicroPython(ESP32)` 和当前单片机占用的端口。

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202303012132771.png)

在点击 OK 之前，我们还需要把 MicroPython 固件烧录到 ESP32 单片机中。点击 `install or update MicroPython`

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202303012133068.png)

选择对应的端口以及固件，端口与之前配置解释器时的端口一致。

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202303012154357.png)

固件需要在 [MicroPython的官网open in new window](https://micropython.org/download/esp32/) 下载，也可以在资料包中的`开发工具`中的`ESP32 MicroPython 固件`中找到。

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202303012139121.png)

点击安装，等待安装完毕即可。

如果安装失败，出现以下报错不用担心，只需要安装时，按住 `BOOT 键`即可。

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202303012200933.png)

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202303012201044.png)

出现以下信息即可松手。

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202303012203634.png)

安装完成后，我们可以看到在单片机设备中出现了 `boot.py` 文件，shell 环境也可以正常使用了。

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202303012205095.png)

## [#](#运行程序) 运行程序

前面我们已经安装好了 Thonny IDE 和配置，接下来我们使用最简单的方式来做一个点亮 LED 的实验测试一下是否 MicroPython 环境是否搭建成功。

大家暂时先不用理解代码意思，后面章节会有讲解。这里主要是为了让大家了解一下 MicroPython 编程软件Thonny 的使用方法和原理。

在本地创建一个文件 `main.py`，

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202303012301780.png)

并将以下代码复制到 `main.py` 文件中。

```python
import time
from machine import Pin

pin2 = Pin(2, Pin.OUT)

while True:
    pin2.value(not pin2.value())
    time.sleep(1)
```

点击左上角`运行当前脚本`，或者按 F5 运行。

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202303012306670.png)

然后我们就可以看到单片机上的一个 LED 开始闪烁，说明我们固件烧录成功了。

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202303012331795.jpg)

## [#](#常见问题) 常见问题

### [#](#_1-配置解释器没有发现端口) 1. 配置解释器没有发现端口

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202303012322054.png)

这里有两种解决方法：

1. 检查esp32连接电脑的数据线，如果是单纯的供电线是不可以的，需要更换为能传输数据的数据线。
2. 安装对应的 `ESP32 USB 驱动`，可以将资料包中的`开发工具`中的`ESP32 驱动 CP210X`下的压缩包解压安装即可。

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202303012326543.png)

### [#](#_2-检测到端口-但是有警告图标-端口无法使用) 2. 检测到端口，但是有警告图标，端口无法使用

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202304231024735.png)

这种情况很有可能是设备驱动有问题。串口显示黄色的，需要更新设备驱动，如下图，右键设备，点击更新设备驱动。

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202304231025151.png)

手动查找驱动程序，

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202304231025989.png)

从计算机上的可用驱动程序列表中选取，

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202304231026376.png)

选择 `端口（COM 和 LPT）`，

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202304231027526.png)

安装两个驱动，第一个是 `USB 串行设备`，

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202304231027797.png)

重复上图的操作,安装另一个驱动 `USB 串行调制解调器设备`，

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202304231028437.png)

这样就 OK 了。

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202304231028393.png)

## [#](#在-pycharm-中使用-micropython) 在 PyCharm 中使用 MicroPython

首先，在 `PyCharm > File > Settings > Plugins` 中找到 MicroPython 插件，

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202303171618527.png)

安装并重启 IDE

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202303171620650.png)

继续打开 Settings，并在 Languages & Frameworks 中找到 MicroPython

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202303171625884.png)

打开 MicroPython 支持，选择设备类型为 `Pyboard`，设备路径输入你电脑检测到的端口，比如我检测到的是 COM6，输入 COM6 即可。

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202303171628272.png)

接着，你会看到在代码块出现警告，缺少支持 Pyboard 的包

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202303171632379.png)

我们直接在终端命令行中输入以下命令，等待安装完成即可：

```bash
pip install pyserial==3.5 docopt==0.6.2 adafruit-ampy==1.0.7 -i https://pypi.
douban.com/simple/
```

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202303171635292.png)

我们还需要加入以下测试代码，来检测是否安装成功，该代码的作用是让 ESP32 单片机上的 LED 闪烁：

```python
# 导入time模块
import time
# 导入Pin模块
from machine import Pin

pin_2 = Pin(2, Pin.OUT)  # 构建led1对象，GPIO15输出

# 永真循环
while True:
    # 使IO15输出高电平，点亮LED
    pin_2.on()
    # 延时0.5秒
    time.sleep(0.5)
    # 使IO15输出低电平，熄灭LED
    pin_2.off()
    time.sleep(0.5)
```

最后，需要添加运行配置，将代码上传到单片机中并运行。点击右上角的 Add Configuration

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202303171652005.png)

 点击右上角的运行，我们可以看到 MicroPython REPL 已经自动打开，但是灯泡并没有闪烁， 

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202303171649881.png)

我们先停止该程序，打开 Thonny，可以看到在单片机中已经多了一个 [led.pyopen in new window](http://led.py) 文件

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202303171655893.png)

::: waring 如果你没有关闭 PyCharm 中的 MicroPython REPL， Thonny 则会显示没有权限访问该端口 :::

重新在 PyCharm 中运行，并在 REPL 中输入 `import led` 或者 `import led.py`，单片机上的 LED 就开始闪烁了。

注意

文件名如果是 [main.pyopen in new window](http://main.py) 的话，会自动启动，但是需要重置一下，点击单片机上的重置开关或者在 REPL 中使用 ctrl + D

总而言之，在敲代码的时候，PyCharm 肯定比 Thonny 好用，但是如果在配置环境还有查看 MicroPython 实时文件系统上，还是离不开 Thonny，因此，本套教程依然采用 Thonny 进行开发。

------

著作权归极客侠 GeeksMan所有 基于GPL 3.0协议 原文链接：https://docs.geeksman.com/esp32/MicroPython/02.esp32-micropython-install.html