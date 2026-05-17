# 修改点 1: 导入方式变了，不再需要 zhipuai
from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

# 加载环境变量的方式不变
_ = load_dotenv(find_dotenv())
# 修改点 2: 读取的环境变量名改成你刚刚配置的
api_key = os.environ['MOONSHOT_API_KEY']

# 修改点 3: 初始化客户端的代码变了，需要指定 base_url 为新地址
client = OpenAI(
    api_key=api_key,
    base_url="https://api.moonshot.cn/v1"  # <--- Kimi 的 API 地址
)

# 修改点 4: 调用模型的方式基本一样，但 model 参数需要换成 Kimi 的模型名
response = client.chat.completions.create(
    model="moonshot-v1-128k",  # 选择一个合适的模型，先试试这个基础版
    messages=[{"role": "user", "content": "给我简单介绍一下机器学习"}],
    temperature=0.5,
)
print(response.choices[0].message.content)