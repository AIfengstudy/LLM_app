# train_parameter_text = """import os
# import subprocess
#
# os.environ['CUDA_VISIBLE_DEVICES'] = '0'
#
# command = [
#     'python',
#     'src/train_bash.py',
#     '--stage', 'sft',
#     '--model_name_or_path', '{}',
#     '--do_train',
#     '--dataset', 'self_cognition',
#     '--finetuning_type', 'lora',
#     '--output_dir', 'muziAI',
#     '--per_device_train_batch_size', '2',
#     '--gradient_accumulation_steps', '2',
#     '--lr_scheduler_type', 'cosine',
#     '--logging_steps', '10',
#     '--save_steps', '1000',
#     '--learning_rate', '5e-5',
#     '--num_train_epochs', '20',
#     '--plot_loss',
#     '--fp16'
# ]
#
# subprocess.call(command)
#                 """
# # 将self.train_parameter_text写入train.py文件
# with open('train.py', 'w') as file:
#     file.write(train_parameter_text)



import hashlib
import json

# 读取 datas.json 文件内容
with open('datas.json', 'r') as file:
    data = json.load(file)

# 将数据转换为 JSON 字符串
json_str = json.dumps(data, sort_keys=True)

# 计算 SHA-1 值
sha1_hash = hashlib.sha1(json_str.encode()).hexdigest()

print("SHA-1 值:", sha1_hash)