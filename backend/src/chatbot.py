# from torch import cuda, bfloat16
# from transformers import AutoTokenizer, transformers
# from time import time
# import torch

# model_id = 'model_id'
# device = f'cuda:{cuda.current_device()}' if cuda.is_available() else 'cpu'

# """
# comment
# Prepare the model and the tokenizer.
# """
# def prep_model_and_tokenizer():
#     time_start = time()
#     bnb_config = config_bnb()
#     model_config = transformers.AutoConfig.from_pretrained(
#         model_id,
#         trust_remote_code=True,
#         max_new_tokens=1024
#     )
#     model = transformers.AutoModelForCausalLM.from_pretrained(
#         model_id,
#         trust_remote_code=True,
#         config=model_config,
#         quantization_config=bnb_config,
#         device_map='auto',
#     )
#     tokenizer = AutoTokenizer.from_pretrained(model_id)
#     time_end = time()
#     print(f"Prepare model and tokenizer: {round(time_end-time_start, 3)} sec.")
#     return model, tokenizer

# """
# comment
# set quantization configuration to load large model with less GPU memory 
# this requires the `bitsandbytes` library
# """
# def config_bnb():
#     bnb_config = transformers.BitsAndBytesConfig(
#         load_in_4bit=True,
#         bnb_4bit_quant_type='nf4',
#         bnb_4bit_use_double_quant=True,
#         bnb_4bit_compute_dtype=bfloat16
#     )
#     print(device)
#     return bnb_config

# """
# comment
# """
# def create_pipeline(model, tokenizer):
#     time_start = time()
#     query_pipeline = transformers.pipeline(
#         "text-generation",
#         model=model,
#         tokenizer=tokenizer,
#         torch_dtype=torch.float16,
#         max_length=1024,
#         device_map="auto")
#     time_end = time()
#     print(f"Prepare pipeline: {round(time_end-time_start, 3)} sec.")
#     return query_pipeline

# """
# comment
# """
# def test_model(tokenizer, pipeline, message): 
#     time_start = time()
#     sequences = pipeline(
#         message,
#         do_sample=True,
#         top_k=10,
#         num_return_sequences=1,
#         eos_token_id=tokenizer.eos_token_id,
#         max_length=200,)
#     time_end = time()
#     total_time = f"{round(time_end-time_start, 3)} sec."
    
#     question = sequences[0]['generated_text'][:len(message)]
#     answer = sequences[0]['generated_text'][len(message):]
    
#     return f"Question: {question}\nAnswer: {answer}\nTotal time: {total_time}" 


# """
# comment
# """
# def query_llm():
#     model, tokenizer = prep_model_and_tokenizer()
#     query_pipeline = create_pipeline(model, tokenizer)
#     return test_model(tokenizer,query_pipeline,
#                    "Please explain what is EU AI Act.")
