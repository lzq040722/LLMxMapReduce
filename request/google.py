# google_request.py
import os
import logging
from google import genai
from google.genai import types
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
    retry_if_exception_type
)

logger = logging.getLogger(__name__)

# proxy = "http://127.0.0.1:7890"
# os.environ["HTTP_PROXY"]  = proxy
# os.environ["http_proxy"]  = proxy
# os.environ["HTTPS_PROXY"] = proxy
# os.environ["https_proxy"] = proxy


from google import genai

class GoogleRequest:
    def __init__(self, model: str):
        self.client = genai.Client(
            api_key=os.environ.get("GOOGLE_API_KEY"),
            )
        self.model = model
    @retry(
        wait=wait_random_exponential(multiplier=2, max=60),
        stop=stop_after_attempt(15),
        retry=retry_if_exception_type(Exception)  # 网络、限流、服务端错误等都重试
    )
    def completion(self, messages, **kwargs) -> str:

        contents = [
            {"role": m["role"], "parts": [types.Part.from_text(text=m["content"])]}
            for m in messages
        ]
            
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=contents,
                config=genai.types.GenerateContentConfig(
                    thinking_config=genai.types.ThinkingConfig(
                    thinking_budget=0
                    )
                )
            )
        except genai.errors.ClientError as e:
            if e.code == 429:
                logger.error("Received 429 error, resetting GOOGLE_API_KEY another")
                # # os.environ["GOOGLE_API_KEY"] = "AIzaSyCcfcy3bkSeqfpNZ5ALqqQ2-RlBNrIQfyE"  # 替换为新的API_KEY
                self.client = genai.Client(
                     api_key='AIzaSyDX1hkB7aiZjXr-dm7wUux0dun9w8_LwMI',
                 )
                raise  # 重新抛出异常以便重试
            else:
                # 如果不是 429 错误，则重新抛出该异常，让 tenacity 进行重试或其他处理
                logger.error('不是429错误')
                raise
        
        text = getattr(response, "text", None)
        token_usage = response.usage_metadata.total_token_count
        if not text:
            logger.error("GoogleRequest.completion: empty response.text")
            raise ValueError("Empty response from GoogleRequest")
        return text, token_usage
