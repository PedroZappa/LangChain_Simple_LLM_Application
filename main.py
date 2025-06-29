import getpass
import os

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage


def main():
    model = init_chat_model("phi3", model_provider="ollama")
    print(model)

    messages = [
        SystemMessage("Translate the following from English into Portuguese"),
        HumanMessage("hi, how are you today? Can I buy you a drink?!"),
    ]

    res = model.invoke(messages)
    print(res.content)
    return 0

if __name__ == "__main__":
    main()
