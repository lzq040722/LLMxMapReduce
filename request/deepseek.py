import os
from deepseek_api import DeepSeek, APIError, RateLimitError  # 假设存在类似的SDK
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
    before_sleep_log,
    retry_if_exception_type
)
import logging

logger = logging.getLogger(__name__)


class DeepSeekRequest:
    def __init__(self, model: str):
        self.client = DeepSeek(
            api_key=os.environ.get("DEEPSEEK_API_KEY"),
            base_url=os.environ.get("DEEPSEEK_API_BASE", "https://api.deepseek.com/v1")
        )
        self.model = model

    @retry(
        wait=wait_random_exponential(multiplier=2, max=60),
        stop=stop_after_attempt(10),
        retry=retry_if_exception_type((RateLimitError, APIError))  # 网络、限流、服务端错误等都重试
    )
    def completion(self, messages, **kwargs):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                **kwargs
            )
            
            # 检查响应是否有效
            if not response.choices or len(response.choices) == 0:
                logger.error("DeepSeekRequest.completion: empty response.choices")
                raise ValueError("Empty choices in DeepSeek response")
            
            answer = response.choices[0].message.content
            token_usage = response.usage
            
            return answer, token_usage
            
        except RateLimitError as e:
            logger.warning(f"Rate limit exceeded in DeepSeekRequest.completion: {e}")
            raise
        except APIError as e:
            logger.warning(f"API error in DeepSeekRequest.completion: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in DeepSeekRequest.completion: {e}. messages: \n{messages}")
            raise