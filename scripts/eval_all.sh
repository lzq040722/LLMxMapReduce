# modify the LD_LIBRARY_PATH to your actual python environmental path
export LD_LIBRARY_PATH=${HOME}/miniconda3/envs/llm_mr_v2/lib/python3.11/site-packages/nvidia/nvjitlink/lib:${LD_LIBRARY_PATH}
export PYTHONPATH=$(pwd):${PYTHONPATH}
export OPENAI_API_KEY='sk-f2gatclNeOnbQVvx41DfA6EeAaD44926BcCbF9Af3c3fFbCb'
export OPENAI_API_BASE='https://az.gptplus5.com/v1'
export SERP_API_KEY='a88e4d137a031980fbc83d0707d6d1648a7bcb6524613c404933c732f24ba791'
export GOOGLE_API_KEY='AIzaSyC46-pzZLDSNG_ZS9ZCQH_Ad8XpIkSMd7k'
current_datetime=$(date +%Y%m%d_%H%M%S)
jsonl_file=$1

echo "start to eval"
echo "logging to ./output/eval/log/${current_datetime}_eval_survey.log"

mkdir -p ./output/eval/log
sleep 1
python ./evaluation/all_eval.py \
    --jsonl_file $jsonl_file \
    --saving_path ./output/eval/${current_datetime} \
    --eval_model  gpt-4o-mini \
    --infer_type OpenAI \
    --method_name LLMxMRv2  \
     2>&1 | tee ./output/eval/log/${current_datetime}_eval_survey.log