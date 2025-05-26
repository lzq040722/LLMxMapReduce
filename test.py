# from openai import OpenAI
# client = OpenAI(
#     base_url='https://az.gptplus5.com/v1',
#     # sk-xxx替换为自己的key
#     api_key='sk-f2gatclNeOnbQVvx41DfA6EeAaD44926BcCbF9Af3c3fFbCb'
# )
# completion = client.chat.completions.create(
#   model="gpt-4o-mini",
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Hello!"}
#   ]
# )
# print(completion.choices[0].message)

# import requests

# params = {
#   'query':'coffee',
#   "GOOGLE_CSE_ID":'a43142871ef39412c',
#   'GOOGLE_API_KEY':"AIzaSyC46-pzZLDSNG_ZS9ZCQH_Ad8XpIkSMd7k",
# }

# response = requests.get("https://cse.google.com", params=params,timeout=10)
# print(response.text)


# import os
# from langchain_core.tools import Tool
# from langchain_google_community import GoogleSearchAPIWrapper


# os.environ["GOOGLE_CSE_ID"] = "a43142871ef39412c"  # 使用API代理服务提高访问稳定性
# os.environ["GOOGLE_API_KEY"] = "AIzaSyBgtywGBixG2OXg2aAPj2QHf58nWnV8m6I"  # 使用API代理服务提高访问稳定性


# search = GoogleSearchAPIWrapper()

# tool = Tool(
#     name="google_search",
#     description="Search Google for recent results.",
#     func=search.run,
# )

# # 执行搜索查询
# result = tool.run("Obama's first name?")
# print(result)


# from google import genai


# client = genai.Client(api_key="AIzaSyD4nCq4FYeUZwPqX4Pf4TttgikkEC1z6c8")

# response = client.models.generate_content(
#     model="gemini-2.0-flash-thinking-exp-1219", contents="Explain how AI works in a few words"
# )
# print(response.text)

# import asyncio
# from playwright.async_api import async_playwright

# async def run():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=True)
#         context = await browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
#         page = await context.new_page()
        
#         # 打开PDF链接
#         await page.goto('https://aclanthology.org/2024.emnlp-main.64.pdf', wait_until='networkidle')
        
#         # 等待一段时间以查看页面
#         await page.wait_for_timeout(5000)  # 等待5秒
        
#         # 关闭浏览器
#         await browser.close()

# # 运行异步函数
# asyncio.run(run())


# url_list = ['1','2']
# with open("1.txt",'w') as f:
#     f.write(str(url_list))

# e={'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits.', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_content_free_tier_requests', 'quotaId': 'GenerateRequestsPerMinutePerProjectPerModel-FreeTier', 'quotaDimensions': {'location': 'global', 'model': 'gemini-2.0-flash-exp'}, 'quotaValue': '10'}]}, {'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.RetryInfo', 'retryDelay': '11s'}]}}
# for key,value in e.items():
#     print(f'{key} : {value}')

# print()
# print(e['error'])

# from request import RequestWrapper

# req_pool = RequestWrapper(
#     model='gemini-2.0-flash-thinking-exp-1219 ',
#     infer_type='Google'
# )

# message = 'How to study English well'
# result = req_pool.completion(message)
# print(result)

# from serpapi import BaiduSearch

# params = {
#   "engine": "baidu",
#   "q": "Coffee",
#   "api_key": "3d6c70e6528130804f1c42cf5a54d58349365ac217c89f4d455ba4c1b2d5fd27"
# }

# search = BaiduSearch(params)
# results = search.get_dict()
# with open('url_list.txt','r') as f:
#     content = f.read()

# url_list = eval(str(content))

# print(type(url_list))
# print(url_list)
# with open('/home/lzq/LLMxMapReduce/LLMxMapReduce_V2/Bias and Fairness in LLMs_url_list.txt','r') as f:
#             content = f.read()
# url_list = eval(str(content))
# print(len(url_list))

import os

print(os.environ.get('DEEPSEEK_API_KEY'))
os.environ.pop('DEEPSEEK_API_KEY',None)
print(os.environ.get('DEEPSEEK_API_KEY'))
os.environ['DEEPSEEK_API_KEY'] = 'bndjsf'
print(os.environ.get('DEEPSEEK_API_KEY'))


