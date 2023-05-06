import openai
from config import Config
from Luna_AI.Luna_wrapping import access_local_wrapper
cfg = Config()

openai.api_key = cfg.openai_api_key

# Overly simple abstraction until we create something better
def create_chat_completion(messages, model=None, temperature=None, max_tokens=None)->str:
    if cfg.use_azure:
        response = openai.ChatCompletion.create(
            deployment_id=cfg.openai_deployment_id,
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
    #added in Luna.AI
    elif cfg.use_wrapper: #will find a _modelthat matches model variable, config thst on luna.
        response = access_local_wrapper(
            llmmodel=llmmodel,
            message= messages,
            temperature=temperature
        )
    #Add elif for config option to use the wrapper, will query the respective wrapper providing path, messages, and temperature 
    else:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )

    return response.choices[0].message["content"]
