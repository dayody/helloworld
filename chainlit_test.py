from pathlib import Path
import chainlit as cl

@cl.on_chat_start
async def main():

    # add startup message
    language = cl.user_session.get("languages").split(",")[0]

    root_path  = Path(__file__).parent
    
    translated_chainlit_md_path = root_path / f"chainlit_{language}.md"
    default_chainlit_md_path = root_path / "chainlit.md"
    if translated_chainlit_md_path.exists():
        message = translated_chainlit_md_path.read_text()
    else:
        message = default_chainlit_md_path.read_text()
    startup_message = cl.Message(content=message)
    await startup_message.send()


    