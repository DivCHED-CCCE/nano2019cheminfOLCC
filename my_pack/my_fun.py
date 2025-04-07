from IPython.display import display, HTML

def scrollable_box(content, height='300px'):
    """
    Display a list or string in a scrollable HTML box in Jupyter Lab or Notebook.

    Parameters:
        content (str or list): The content to display.
        height (str): Height of the scrollable area (e.g., '200px', '50vh').

    Returns:
        None
    """
    if isinstance(content, list):
        content = "<br>".join(str(item) for item in content)
    elif isinstance(content, str):
        # Escape HTML-sensitive characters and preserve formatting
        content = content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        content = content.replace("\n", "<br>")

    html = f"""
    <div style='height: {height}; overflow-y: scroll; border: 1px solid lightgray;
                font-family: monospace; white-space: pre; padding: 5px; background: #f9f9f9;'>
        {content}
    </div>
    """
    display(HTML(html))

#
from IPython.display import display, HTML

def scrollable_pre(content, height='300px'):
    """
    Display a long string (e.g., SDF file) in a scrollable, preformatted block.

    Parameters:
        content (str): Multi-line text to display.
        height (str): Scrollable box height (e.g., '300px').

    Returns:
        None
    """
    if not isinstance(content, str):
        raise TypeError("Expected a string.")

    # Escape HTML-sensitive characters
    content = content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    html = f"""
    <div style="height:{height}; overflow-y:scroll; border:1px solid lightgray; padding:5px; background:#f9f9f9;">
        <pre style="font-family: monospace; white-space: pre;">{content}</pre>
    </div>
    """
    display(HTML(html))


