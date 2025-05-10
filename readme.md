git add rpa readme.md requirements.txt

git commit -m "给我老婆重写小红书的自动评论截流方法"

git remote add origin git@github.com:cheraljun/rpa.git

git remote add origin https://github.com/cheraljun/rpa.git

git push origin master

# 更新说明：

# 指定位置单击操作(5月2日新增)

# 重写指令类型(5月3日修订)

# 重写指令类型(5月3日第二次修订，优化小红书rpa逻辑)

# 优化小红书模拟人类操作的逻辑(5月3日第三次修订)

# 新增多个public_api





# 指令类型说明：
# mouse - 鼠标操作（悬停/点击）
# scroll - 滚轮滚动操作
# wait - 等待操作
# input - 输入操作

# 内容说明：
# 对于鼠标操作，内容为 {action: 'hover/click', click_times: 点击次数, lOrR: 'left/right', img: 图片名, x: x坐标, y: y坐标}
# 对于滚轮操作，内容为滚动的距离（正数向上，负数向下）
# 对于等待操作，内容为等待的时长（秒）
# 对于输入操作，内容为 {content: 要输入的字符串, use_api: 是否使用外部api}

# 重复次数说明：
# -1 代表一直重复
# 正整数代表重复的次数



# 5月2日：开发出雏形，后续会想办法解决点击操作时找不到图片的情况

