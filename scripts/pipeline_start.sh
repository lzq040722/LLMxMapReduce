export LD_LIBRARY_PATH=${HOME}/miniconda3/envs/llm_mr_v2/lib/python3.11/site-packages/nvidia/nvjitlink/lib:${LD_LIBRARY_PATH}
export PYTHONPATH=$(pwd):${PYTHONPATH}
export OPENAI_API_KEY='sk-f2gatclNeOnbQVvx41DfA6EeAaD44926BcCbF9Af3c3fFbCb'
export OPENAI_API_BASE='https://az.gptplus5.com/v1'
export SERP_API_KEY='77867df71c1004995af6726571723f3d0129358ffaef52f9747ee2a3c93c95df'
export GOOGLE_API_KEY='AIzaSyC46-pzZLDSNG_ZS9ZCQH_Ad8XpIkSMd7k'

topic=$1
timestamp=$(date +%Y%m%d_%H%M%S)
log_dir="./output/log"
output_dir="./output"  
topic_safe=$(echo "$topic" | sed 's/ /_/g' | sed 's/[^a-zA-Z0-9_.-]//g')
log_file="${log_dir}/${timestamp}_${topic_safe}.log"
output_file="${output_dir}/${topic_safe}.jsonl"

mkdir -p "$log_dir"

python ./src/start_pipeline.py \
    --input_file '/home/lzq/LLMxMapReduce/LLMxMapReduce_V2/output/Bias and Fairness in LLMs_20250507_014104_crawl_result.jsonl' \
    --top_n 80 \
    --output_file "$output_file" \
    --config_file ./config/model_config.json \
    --parallel_num 2 \
    --block_count 1 \
    --data_num 1 \
    2>&1 | tee "$log_file"

echo "Log file: $log_file"
echo "Output file: $output_file"