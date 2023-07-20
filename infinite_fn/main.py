import importlib
import inspect

import gradio as gr
from dotenv import load_dotenv
from func_ai.function_indexer import FunctionIndexer
from func_ai.utils import OpenAIInterface

_chat_message = []

load_dotenv()
_fi = FunctionIndexer()


def get_llm() -> OpenAIInterface:
    """
    Returns the LLM interface with system prompt

    :return:
    """
    intf = OpenAIInterface()
    intf.add_conversation_message({"role": "system",
                                   "content": "You are a helpful assistant that helps people in achieving their goal through a variety of functions."
                                              "Do not answer the user's question directly but first reflect on what the user wants to achieve."
                                              "Do not suggest any information other than what the user is actually asking about"
                                              "Write no more than 2-3 sentences as a reflection on the user's query."
                                              "Do not expose the underlying functions to the user."
                                              "If no function to help with user query is found, tell the user 'I am sorry but I cannot help you with that any further.'"
                                   })
    return intf


def index_module(module_name: str, function_indexer: FunctionIndexer):
    """
    Indexes all functions in a module

    :param module_name: The name of the module to index (e.g. "func_ai.utils")
    :param function_indexer:  The function indexer to use
    :return:
    """
    module = importlib.import_module(module_name)
    functions = inspect.getmembers(module, inspect.isfunction)
    # print({fn: isinstance(f, functools.partial) for fn, f in functions})
    function_indexer.index_functions([f for _, f in functions], enhanced_summary=True)


def update_convo(user_message: str):
    """
    Updates the conversation with a user message

    :param user_message:
    :return:
    """
    global _fi
    _llm_interface = get_llm()
    _resp = _llm_interface.send(user_message)
    _fresp = _fi.find_functions(query=_resp['content'], max_results=3)
    assert len(_fresp) > 0, "No functions found"
    if len(_fresp) >= 1:
        _llm_interface.add_conversation_message({"role": "assistant",
                                                 "content": f"I have found a function to call: {_fresp[0].name}"},
                                                update_llm=True,
                                                functions=[_fresp[0].wrapper.schema])
        _fresp[0].wrapper.from_response(_llm_interface.conversation_store.get_last_message())
        _llm_interface.add_conversation_message(_fresp[0].wrapper.last_call['function_response'], update_llm=True)
    else:
        _llm_interface.add_conversation_message({"role": "assistant",
                                                 "content": f"I am sorry but I cannot help you with that any further."},
                                                update_llm=True)
    return f"{_llm_interface.conversation_store.get_last_message()['content']}\n\n Usage: {_llm_interface.get_usage()}"


def add_text(history, text):
    global _chat_message
    history = history + [(text, None)]
    _chat_message.append(update_convo(text))
    return history, ""


def bot(history):
    global _chat_message
    history[-1][1] = _chat_message[-1]
    return history


with gr.Blocks() as demo:
    chatbot = gr.Chatbot([], elem_id="chatbot")

    with gr.Row():
        with gr.Column(scale=1):
            txt = gr.Textbox(
                show_label=False,
                placeholder="Enter text and press enter",
                container=False
            )
    txt.submit(add_text, [chatbot, txt], [chatbot, txt]).then(
        bot, chatbot, chatbot
    )

if __name__ == "__main__":
    # print(_fi._collection.get())
    # _fi.reset_function_index()
    index_module("infinite_fn.python_fns.trip", _fi)
    index_module("infinite_fn.python_fns.attractions", _fi)
    index_module("infinite_fn.python_fns.weather", _fi)
    index_module("infinite_fn.python_fns.lodging", _fi)

    demo.launch(server_name="0.0.0.0", server_port=9003)
    # run_alternative_convo()
