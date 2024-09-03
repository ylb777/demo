import csv
import os


def write_to_csv(file_path, data_list):
    # 检查文件路径是否存在，如果不存在则创建文件路径
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))

    # 打开CSV文件，以写入模式打开
    with open(file_path, 'a', newline='') as csvfile:
        # 创建CSV写入器
        writer = csv.writer(csvfile)

        # 将列表的内容写入CSV文件的同一列中
        writer.writerow(data_list)


import torch
import torch.nn as nn


# 定义一个简单的神经网络模型
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc1 = nn.Linear(10, 5)
        self.fc2 = nn.Linear(5, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x


# 创建一个模型实例
model = SimpleModel()
print('ss')
# 使用 .named_parameters() 函数遍历模型中的所有参数
for name, param in model.named_parameters():
    print(f'Parameter name: {name}, Parameter shape: {param.shape}')
