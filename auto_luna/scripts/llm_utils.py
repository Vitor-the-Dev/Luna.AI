import openai
from config import Config
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
    elif cfg.use_wrapper:
        response = querywrapper(
            message= messages,
            path=cfg.wrapperpath
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
