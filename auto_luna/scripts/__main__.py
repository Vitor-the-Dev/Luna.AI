from spinner import spinner


def main():
    pass


if __name__ == '__main__':
    while True:
        #main AI interaction loop
        with Spinner("Thinking... "):
        assistant_reply = chat_with_ai( #chat.chat_with_ai will be replaced by chat_with_ai, which will come from using a llm wrapper
            prompt,
            user_input,
            full_message_history,
            memory,
            cfg.fast_token_limit) # TODO: This hardcodes the model to use GPT3.5. Make this an argument

    main()