import subprocess

command = [
    'python',
    'src/export_model.py',
    '--model_name_or_path',
    r'D:\rkwork\app\LLMapp\ChatGLM3\chatglm3-models',
    '--finetuning_type',
    'lora',
    '--checkpoint_dir',
    r'C:\Users\rkwork\Desktop\GZZC_LLM\checkpoint_output',
    '--output_dir',
    'muziAI'
]

subprocess.call(command)