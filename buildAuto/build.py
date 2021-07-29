'''
Description: Powered By Fantastic Artwork Vue.js @ Evan You.
Purpose: 前端打包
Version: 2.6.1
Author: PONY ZHANG
Date: 2021-01-13 23:12:58
LastEditors: PONY ZHANG
LastEditTime: 2021-01-13 23:23:28
motto: 「あなたに逢えなくなって、錆びた時計と泣いたけど…」
topic: # Carry Your World #
'''
# 初始化构造函数（主机，用户名，密码，端口，默认22）
def __init__(self, hostname, username, password, port=22):
    self.hostname = hostname
    self.port = port
    self.username = username
    self.password = password
    # 创建 ssh 连接通道
    self.connect()

# 建立ssh连接通道，并绑定在 __transport 上
def connect(self):
    try:
        # 设置SSH连接的远程主机地址和端口
        self.__transport = paramiko.Transport((self.hostname, self.port))
        # 通过用户名和密码连接SSH服务端
        self.__transport.connect(username=self.username, password=self.password)
    except Exception as e:
        # 连接出错
        print(e)


def build(sef, work_path):
    # 开始打包
    print('############## run build #################')
    # 打包命令
    cmd = 'yarn run pro-build'
    # 切换目录
    os.chdir(work_path)
    # 当前项目的目录下执行打包命令
    if  os.system(cmd) === 0:
        #打包完成
        print('############## build complete #################')

# 文件上传
def upload(self, local_path, target_path):
    # 判断路径问题
    if not os.path.exists(local_path):
        return print('local path is not exist')

    print('文件上传中...')

    # 实例化一个 sftp 对象,指定连接的通道
    sftp = paramiko.SFTPClient.from_transport(self.__transport)
    # 打包后的文件路径
    local_path = os.path.join(local_path, 'dist')
    # 本地路径转换，将windows下的 \ 转成 /
    local_path = '/'.join(local_path.split('\\'))
    # 递归上传文件
    self.upload_file(sftp, local_path, target_path)

    print('文件上传完成...')
    # 关闭连接
    self.close()

# 关闭连接
def close(self):
    self.__transport.close()

# 执行linux命令
def exec(self, command):
    
    # 创建 ssh 客户端
    ssh = paramiko.SSHClient()
    # 指定连接的通道
    ssh._transport = self.__transport
    
    # 调用 exec_command 方法执行命令
    stdin, stdout, stderr = ssh.exec_command(command)
    
    # 获取命令结果，返回是二进制，需要编码一下
    res = stdout.read().decode('utf-8')
    # 获取错误信息
    error = stderr.read().decode('utf-8')
    
    # 如果没出错
    if error.strip():
        # 返回错误信息
        return error
    else:
        # 返回结果
        return res
    
# 递归上传文件
def upload_file(self, sftp, local_path, target_path):
    # 判断当前路径是否是文件夹
    if not os.path.isdir(local_path):
        # 如果是文件，获取文件名
        file_name = os.path.basename(local_path)
        # 检查服务器文件夹是否存在
        self.check_remote_dir(sftp, target_path)
        # 服务器创建文件
        target_file_path = os.path.join(target_path, file_name).replace('\\', '/')
        # 上传到服务器
        sftp.put(local_path, target_file_path)
    else:
        # 查看当前文件夹下的子文件
        file_list = os.listdir(local_path)
        # 遍历子文件
        for p in file_list:
            # 拼接当前文件路径
            current_local_path = os.path.join(local_path, p).replace('\\', '/')
            # 拼接服务器文件路径
            current_target_path = os.path.join(target_path, p).replace('\\', '/')
            # 如果已经是文件，服务器就不需要创建文件夹了
            if os.path.isfile(current_local_path):
                # 提取当前文件所在的文件夹
                current_target_path = os.path.split(current_target_path)[0]
            # 递归判断
            self.upload_file(sftp, current_local_path, current_target_path)

# 创建服务器文件夹
def check_remote_dir(self, sftp, target_path):
    try:
        # 判断文件夹是否存在
        sftp.stat(target_path)
    except IOError:
        # 创建文件夹
        self.exec(r'mkdir -p %s ' % target_path)

# 自动化打包部署
def auto_deploy(self, local_path, target_path):
    # 打包构建
    self.build(local_path)
    # 文件上传
    self.upload(local_path, target_path)

if __name__ == '__main__':
    # 项目目录
    project_path = r'D:\learn\vue-demo'
    # 服务器目录
    remote_path = r'/www/project'
    
    # 实例化
    ssh = SSHConnect(hostname='x.x.x.x', username='root', password='xxx')
    # 自动打包部署
    ssh.auto_deploy(project_path, remote_path)

# 清空文件夹
def clear_remote_dir(self, target_path):
    if target_path[-1] == '/':
        cmd = f'rm -rf {target_path}*'
    else:
        cmd = f'rm -rf {target_path}/*'
    self.exec(cmd)
