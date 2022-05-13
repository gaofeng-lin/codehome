#!/bin/bash 

#1.本地编译服务
cd /C/Tools/train_code/PHenglei-Cloud/cfdplatform

echo "编译cfdplatform"
CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go.exe build -o cfdplatform main.go 
echo "编译完成"



#2.拷贝后台服务
echo "拷贝服务到指定目录"
cp ./cfdplatform ../../test_linux


# #4.前端服务编译
echo "进入前端目录"
cd ../frontend
npm run build:development
cd ./web/development
zip renderer.zip renderer
echo "打包完成"

#5.前端服务拷贝
cp ./renderer.zip ../../../../test_linux/


# 6.传输文件
cd ../../../../test_linux/
echo "传输文件"
echo "请输入root密码："
# sshpass -p yskj scp cfdplatform yskj@116.63.141.248:/home/yskj/lgf/winLinux/
# sshpass -p RYpaaD\[GvIhAYoW0SMSe^x%\[eR scp cfdplatform root@121.37.93.92:/home/yskj/lgf/test_win/
scp cfdplatform renderer.zip yskj@116.63.141.248:/home/yskj/lgf/winLinux/
echo "传输完成"

#4.连接服务器
ssh  yskj@116.63.141.248



#5.停止服务
sudo supervisorctl stop cfdplatform
sudo supervisorctl stop cfdagent
sudo supervisorctl stop cfdmonitor
sudo supervisorctl stop postserver

#6.保存数据库文件
mysqldump -u root -o 

#7.启动新数据库文件

#8.启动新服务文件



# ssh root@121.37.93.92 -i PHengleicloud <<EOF

# cd /home/yskj/lgf/test_win/

# lcd "C:\Tools\train_code"

# put test.sh

# echo "ok"

# EOF