import transformers
import torch
from transformers import AutoTokenizer
from time import time
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFacePipeline
from langchain.prompts import PromptTemplate
import chromadb

class Chatbot:
  def __init__(self):
    print("Setting up model, tokenizer and pipeline")
    time_start = time()
    bnb_config = transformers.BitsAndBytesConfig(
        load_in_4bit = True,
        bnb_4bit_quant_type = "nf4",
        bnb_4bit_compute_dtype = torch.float16,
        bnb_4bit_use_double_quant = True,
        llm_int8_enable_fp32_cpu_offload=True 
    )
    model = transformers.AutoModelForCausalLM.from_pretrained(
        "meta-llama/Meta-Llama-3-8B",
        trust_remote_code=True,
        quantization_config=bnb_config,
        device_map='cuda:0',
        offload_buffers=True,
        low_cpu_mem_usage = True
    )
    tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B", use_fast=True)
    query_pipe = transformers.pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        pad_token_id = tokenizer.eos_token_id,
        torch_dtype=torch.float16,
        max_length=800,
        temperature = 0.3,
        top_p = 0.8,
        top_k = 10,
        repetition_penalty = 1.15,
        truncation = True,
        device_map="cuda:0",
    )
    llm = HuggingFacePipeline(pipeline=query_pipe)
    time_end = time()

    embedding_func = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")
    chroma_client = chromadb.PersistentClient(path="tv_series_database")

    vector_store_from_client = Chroma(
        client=chroma_client,
        collection_name="tv_series_rag",
        embedding_function=embedding_func,
    )

    template = """
    Based on the provided titles and descriptions, summarize each title in a brief and concise manner. 
    Your summary should strictly follow the given descriptions without introducing any new details or interpretations. 
    Only summarize what is present in the provided descriptions, without adding personal insights or modifications.

    {context}

    Answer:
    """

    PROMPT = PromptTemplate(
    template=template, input_variables=["context"])
    chain_type_kwargs = {"prompt": PROMPT}

    self.qa_chain = RetrievalQA.from_chain_type(
      llm = llm,
      chain_type = "stuff",
      retriever = vector_store_from_client.as_retriever(search_kwargs={"k": 2}),
      chain_type_kwargs = chain_type_kwargs,
      verbose = True
    )
    print(f"Finished setup after: {round(time_end-time_start, 3)} sec.")

  def invoke_llm(self, question):
    llm_response = self.qa_chain.invoke(question)  
    return llm_response['result']
  
chatbot = Chatbot()