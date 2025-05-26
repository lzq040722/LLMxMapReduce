import logging
import random
from src.base_method.data import Dataset
from src.base_method.module import Module

from .convolution_module import ConvolutionLayerModule
from .refine_module import SelfRefineModule
from src.prompts import DIGEST_BASE_PROMPT
from src.hidden.convolution_block.neurons import (
    FeedbackClusterNeuron,
)

logger = logging.getLogger(__name__)


class SkeletonRefineModule(Module):
    """
    骨架精炼模块：对survey的大纲（skeleton）进行摘要聚类、卷积融合和自我精炼。
    """
    def __init__(
        self,
        configs,
        convolution_layer,
        receptive_field,
        result_num,
        top_k,
        self_refine_count,
        self_refine_best_of,
    ):
        super().__init__()
        # 反馈聚类神经元，用于摘要聚类与反馈
        self.feedback_cluster_neuron = FeedbackClusterNeuron(configs["cluster"])

        # 卷积层模块，用于多摘要信息融合
        self.convolution_layer_module = ConvolutionLayerModule(
            configs["convolution"],
            convolution_layer,
            receptive_field,
            result_num,
            top_k,
        )

        # 自我精炼模块，用于多轮自我改进
        self.self_refine_module = SelfRefineModule(
            configs["refine"], self_refine_count, self_refine_best_of
        )

    def forward(self, survey):
        """
        主流程：
        1. 对每个digest进行摘要聚类与反馈
        2. 进行卷积层信息融合
        3. 进行自我精炼
        4. 更新survey的block_cycle_count
        """
        logger.info(
            f"Skeleton refine module start: Survey {survey.title} block cycle count: {survey.block_cycle_count}"
        )
        skeleton = survey.skeleton
        title = survey.title
        digests = survey.digests.values()

        # 构造数据集，每个digest单独作为一个聚类单元
        dataset = Dataset(
            [
                (
                    title,
                    [digest_group],
                    skeleton,
                    DIGEST_BASE_PROMPT,
                )
                for digest_group in digests
            ]
        )

        logger.info(
            f"Feedback Cluster start: Count {len(dataset)} Survey: {title}, Digest Group Count: {len(dataset)}"
        )
        # 步骤1：摘要聚类与反馈
        utilise_results = self.feedback_cluster_neuron(dataset)
        logger.info(
            f"Feedback Cluster finished: Survey: {title}, Digest Group Count: {len(dataset)}"
        )

        # 步骤2：卷积层信息融合
        survey = self.convolution_layer_module(
            survey,
            utilise_results,
            skeleton.all_skeleton(construction=True, analysis=True, with_index=True),
        )
        logger.info(f"Convolution layer module finished: Survey {survey.title}")

        # 步骤3：自我精炼
        survey = self.self_refine_module(survey)
        logger.info(f"Self-refine module finished: Survey {survey.title}")

        # 步骤4：更新block_cycle_count
        survey.block_cycle_count += 1
        logger.info(
            f"Skeleton-refine module finished: Survey {survey.title} block cycle count: {survey.block_cycle_count}"
        )
        return survey

    def merge_results_from_one_description(self, utilise_results):
        """
        将同一description下的多个结果合并，随机打乱后拼接。
        返回合并后的结果列表。
        """
        result_dict = {}
        for result, description in utilise_results:
            if description not in result_dict:
                result_dict[description] = []
            result_dict[description].append(result)
        for description, results in result_dict.items():
            random.shuffle(results)
            result_dict[description] = "/n".join(results)
        result_list = [
            (result, description) for description, result in result_dict.items()
        ]
        random.shuffle(result_list)
        return result_list
