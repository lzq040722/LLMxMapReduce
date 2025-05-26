from request import RequestWrapper
import logging
import time
logger = logging.getLogger(__name__)

class APIModel:
    def __init__(self, model, infer_type):
        self.model = model
        self.request = RequestWrapper(model, infer_type)
        
    def __req(self, text, temperature=0):
        result = None
        retry = 3
        while retry > 0:
            try:
                result = self.request.completion(text, temperature=temperature)
                break
            except ValueError as e:
                temperature += 0.1
                logger.warning(f"RequestException: {e} ")
                logger.info(f'第{4-retry}次尝试失败。')
                retry -= 1

        return result
    # def __req(self, text, temperature=0):
    #     result = None
    #     retry = 10
    #     delay = 1  # 初始延迟时间（秒）
        
    #     while retry > 0:
    #         try:
    #             result = self.request.completion(text, temperature=temperature)
    #             break
    #         except ValueError as e:
    #             temperature += 0.1
    #             retry -= 1
                
    #             # 记录重试信息
    #             logger.info(f"第 {10 - retry} 次请求失败，{delay} 秒后重试")
                
    #             # 等待一段时间后再重试，采用指数退让策略
    #             time.sleep(delay)
    #             delay *= 2  # 每次重试后将延迟时间加倍

    #     return result
 
    def chat(self, text, temperature=0):
        response = self.__req(text, temperature=temperature)
        return response
