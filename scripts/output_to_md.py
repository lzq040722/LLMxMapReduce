import json
import os

input_file = "/home/lzq/LLMxMapReduce/LLMxMapReduce_V2/output/Bias_and_Fairness_in_LLMs.jsonl"
output_dir = "/home/lzq/LLMxMapReduce/LLMxMapReduce_V2/output/"

with open(input_file, "r") as f:
    for line in f:
        data = json.loads(line)
        content = data["content"]
        content += "\n\n" + data["ref_str"]
        with open(os.path.join(output_dir, data["title"] + ".md") , "w") as out:
            out.write(content)