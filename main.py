import getpass
import os

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate


def main():
    model = init_chat_model("phi3", model_provider="ollama")
    print(model)

    system_template = "Translate the following from English into {language}"

    prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_template), ("user", "{text}")]
    )
    prompt = prompt_template.invoke({"language": "Italian", "text": "hi!"})

    response = model.invoke(prompt)
    print(response.content)
    return 0

if __name__ == "__main__":
    main()
