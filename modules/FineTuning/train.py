import os
import subprocess

os.environ['CUDA_VISIBLE_DEVICES'] = '0'

command = [
    'python',
    'src/train_bash.py',
    '--stage', 'sft',
    '--model_name_or_path', '{}',
    '--do_train',
    '--dataset', 'self_cognition',
    '--finetuning_type', 'lora',
    '--output_dir', 'muziAI',
    '--per_device_train_batch_size', '2',
    '--gradient_accumulation_steps', '2',
    '--lr_scheduler_type', 'cosine',
    '--logging_steps', '10',
    '--save_steps', '1000',
    '--learning_rate', '5e-5',
    '--num_train_epochs', '20',
    '--plot_loss',
    '--fp16'
]

subprocess.call(command)
                