from openai import OpenAI      # 改成 OpenAI 客户端
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
api_key = os.environ['MOONSHOT_API_KEY']   # 改环境变量名

# 初始化 Kimi 客户端（OpenAI 兼容）
client = OpenAI(
    api_key=api_key,
    base_url="https://api.moonshot.cn/v1"   # 指定 Kimi 的 API 地址
)

def ask(prompt, system="你是一个 helpful assistant.", temperature=0.5, model="moonshot-v1-128k"):
    """
    发送 prompt 到 Kimi API 并打印回复
    默认使用基础免费模型 moonshot-v1-8k，你也可以换成 kimi-k2 等
    """
    response = client.chat.completions.create(
        model=model,                         # 使用 Kimi 的模型名
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
    )
    print(response.choices[0].message.content)
    
if __name__ == "__main__":
    ask("你好，请用一句话介绍你自己。")