# mp3cover2mp4
fetch cover of given mp3 file and convert it to a mp4 with the cover as video content

实际上是一个非常弱智的小玩意……
用途：拿一个mp3，把封面提取出来，之后拼成画面为这个封面的mp4.用来传视频的。
实现比较简陋，我最开始只是写了个py脚本（其内就用了两个ffmpeg指令），而后想着套个壳子，就随便写了一个。

之后：
* 用后端直接转了，不依赖脚本
* 把ncm等加密的音乐文件提取过程也放进来
* 做好看点