from zhipuai import ZhipuAI
import os
from dotenv import load_dotenv, find_dotenv

# 加载 .env 文件中的环境变量
_ = load_dotenv(find_dotenv())
api_key = os.environ['ZHIPUAI_API_KEY']

# 初始化客户端
client = ZhipuAI(api_key=api_key)

# 发起一次对话
response = client.chat.completions.create(
    model="glm-4.7-flash", # 使用免费的 Flash 模型
    messages=[
        {"role": "system", "content": "你是一个乐于助人的知识库助手。"},
        {"role": "user", "content": "什么是机器学习？"}
    ],
    temperature=0.5,
)

# 打印模型的回复
print(response.choices[0].message.content)