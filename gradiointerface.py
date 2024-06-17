import gradio as gr

#@tool("Gradio Channel")
def question_ui_tool(question, levelofexperience):
    """The gradio interface is a UI for the user to be able key in their question and indicate their level of experience in the field. This allows the crew member to develop a prompt that is most suitable for the user"""
    return question + " " + "Your years of experience is: " + str(levelofexperience) + " years."

# Define the Gradio interface
gr_tool= gr.Interface(
    fn=question_ui_tool,
    inputs=["text", "slider"],
    outputs= "text",
    title="Question UI Tool",
    description="Enter your question and indicate your level of experience.")

gr_tool.launch()