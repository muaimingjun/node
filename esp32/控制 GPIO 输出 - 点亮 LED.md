# 控制 GPIO 输出 - 点亮 LED

------
不论学习什么单片机，最简单的外设莫过于 IO 口的高低电平控制 LED，本节课将向大家介绍如何使用 MicroPython 控制 ESP32 的 GPIO 输出。通过本节课的学习，让大家对 MicroPython 的程序架构有一定的认识，为以后大型项目程序学习打下基础，增强信心。

##  实验原理

###  1. GPIO 引脚

引脚又叫管脚，英文叫 Pin, 就是从集成电路（芯片以及一些电子元件）内部电路引出与外围电路的接线的接口。

在我们的 ESP32 开发板上, 我们可以把这些称为引脚, 这些引脚其实是从 ESP32 芯片内部引出来的, 我们可以看到每个引脚都标了自己独特的名字。

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202303261657888.png)

其中有一类引脚叫 GPIO 引脚, 负责输入/输出电压。开发板上 D 开头的引脚都是这种引脚, 比如 D2、D4、D15 等等

输入我们暂时不讲，这里我们先讲一下输出，简单来说，每个 GPIO 都可以输出高低电平。

什么是电平？

电路上某点的电压（对公共参考点）或电位是高还是低。比如在逻辑电路中，高于某个数值的电位称其为高电位，或高电平，低于某个数值的，为低电位或低电平。比如 ESP32 中，高电平的数值大于2.5V，低电平的数值小于0.5V，具体的数值最好通过测试研究来确定。

### [#](#_2-led) 2. LED

LED（light-emitting diode） 即发光二极管。它具有单向导电性，通过 5mA 左右电流即可发光，电流越大，其亮度越强，但若电流过大，会烧毁二极管，一般我们控制在 3mA-20mA 之间，通常我们会在 LED 管脚上串联一个电阻，目的就是为了限制通过发光二极管的电流不要太大，因此这些电阻又可以称为`限流电阻`。当发光二极管发光时，测量它两端电压约为 1.7V，这个电压又叫做发光二极管的`导通压降`。

发光二极管正极又称阳极，负极又称阴极，电流只能从阳极流向阴极。直插式发光二极管长脚为阳极，短脚为阴极。

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202303021153821.png)

## [#](#硬件电路设计) 硬件电路设计

物料清单（BOM 表）：

|   材料名称   | 数量 |
| :----------: | :--: |
|  直插式 LED  |  1   |
|   1kΩ 电阻   |  1   |
| 杜邦线(跳线) | 若干 |
|    面包板    |  1   |

LED 的正极接开发板的 D12 引脚，并串联一个电阻，负极接 GND，如下图：

![img](https://gcore.jsdelivr.net/gh/bigrich-luo/typora-picgo-images-1@master/images/202310291459817.png)

注意

一定要接电阻，不然会由于电流过大，烧坏 LED。

## [#](#软件设计) 软件设计

### [#](#pin-引脚类) Pin 引脚类

MicroPython 中可使用 machine 模块中的 Pin 模块对 GPIO 输出控制。其构造方法如下：

构造函数 `Pin(id, mode=-1, pull=-1, value, drive, alt)`：访问与给定 `id 引脚`. 如果在构造函数中给出了额外的参数，那么它们将用于初始化引脚。任何未指定的设置将保持其先前状态。

- `id` 是必填项，用于指定引脚，注意：可用的引脚范围是：0-19，21-23，25-27，32-39。
- `mode` 指定引脚模式，可以是 `Pin.IN` 输入引脚，`Pin.OUT`。
- `pull` 指定引脚是否连接了（弱）上拉电阻，并且可以是 `None` 没有上拉或下拉电阻，`Pin.PULL_UP` 上拉电阻，`Pin.PULL_DOWN` 下拉电阻。

其他参数在初级阶段涉及相对较少，更多内容可以参考[官网文档open in new window](https://docs.micropython.org/en/latest/esp32/quickref.html#pins-and-gpio)。

```python
from machine import Pin

# 创建一个输出引脚在 0 引脚
p0 = Pin(0, Pin.OUT)

# 给 P0 引脚先输出低电平，再输出高电平
p0.value(0)
p0.value(1)

# 给 P0 引脚先输出低电平，再输出高电平，等同于 p0.value(0)，p0.value(1)
p0.on()
p0.off()

# 在 P2 创建一个输入引脚，并设置上拉电阻
p2 = Pin(2, Pin.IN, Pin.PULL_UP)

# 打印 P2 的值
print(p2.value())
```

通过上面的文档我们知道，想要让一个引脚输出高电平，只需要找到对应的 GPIO 然后通过 `on()` 或者 `value(1)` 操作就可以，同理如果想要输出低电平让 `LED` 灯灭，只需要调用 `off()` 或者 `value(0)` 就行。

### [#](#_1-点亮一颗-led) 1. 点亮一颗 LED

因此，如果我们想要点亮这颗 LED 的话，只需要先构建引脚对象，然后给这个引脚赋值一个高电平即可。

```python
from machine import Pin

# 构建 pin_12 引脚对象，GPIO12输出
pin_12 = Pin(12, Pin.OUT)

# 使 Pin2 输出高电平，点亮LED
pin_12.value(1)
```

通过 Thonny 编写上述代码，然后运行，此时会看到电路中的 LED 灯被点亮了。

### [#](#_2-闪烁的-led-灯) 2. 闪烁的 LED 灯

我们已经成功点亮一颗 LED 了，接下来，可以尝试一下稍微复杂一点的逻辑，比如让这颗 LED 闪烁。

实现 LED 闪烁的原理很简单，就是在`循环语句`中使用`延时模块`。先设置高电平，延时 X 秒，再设置低电平，延时 X 秒，之后就不断循环该语句即可。

在之前的 [Python 入门教程]() 中，我们学习了 `for` 和 `while` 两种循环语句，如果我们想要让灯泡一直闪烁，则需要设置无限循环，因此使用 `while` 更合适。

```python
# 如果 while 的条件为 True，一直为真，就可以实现无限循环了。
while True:
    pass
```

Python 中用到延时，可使用 time 模块，time 模块中常用的几个延时函数使用如下：

```python
# 导入 time 模块
import time

# 延时 0.5 秒
time.sleep(0.5)
# 延时 100 毫秒
time.sleep_ms(100)
# 延时 100 微秒
time.sleep_us(100)
# 获取毫秒计时器当前值
time_1 = time.ticks_ms()
```

注意

这里的 time 模块是 MicroPython 中的 time 模块，与 Python 中的不同，更多使用方法可以参考官方文档 [MicroPython Time 模块open in new window](https://docs.micropython.org/en/latest/library/time.html?highlight=time#module-time)

所以，我们的程序可以这么写：

```python
# 导入time模块
import time
# 导入 Pin 模块
from machine import Pin

# 构建 P12 对象，GPIO12输出
pin_12 = Pin(12, Pin.OUT)  

# 永真循环
while True:
    # 使 P12 输出高电平，点亮 LED
    pin_12.on()
    # 延时 0.5 秒
    time.sleep(0.5)
    # 使 P12 输出低电平，熄灭 LED
    pin_12.off()
    time.sleep(0.5)
```

运行程序，LED 就闪烁了。

