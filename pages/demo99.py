import streamlit as st
import streamlit.components.v1 as components


def centered_text(text, font_size=None, color=None):
    style = "text-align: center;"
    if font_size:
        style += f" font-size: {font_size};"
    if color:
        style += f" color: {color};"
    return f"<div style='{style}'>{text}</div>"



st.markdown(centered_text("<h1 style= 'color : #37D2DC'>LIVE STATUS OF ASSETS</h1>"), unsafe_allow_html=True)
#st.divider()


# Set Streamlit to wide mode
#st.set_page_config(layout="wide")
# HTML code for the Power BI dashboard iframe
dashboard_url = """
<style>
    .responsive-iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }
    .iframe-container {
        position: relative;
        width: 100%;
        padding-top: 56.25%; /* Aspect ratio 16:9 */
    }
</style>
<div class="iframe-container">
    <iframe class="responsive-iframe" 
            src="https://app.powerbi.com/view?r=eyJrIjoiODI1NDAwNDMtNjdhYy00OTUxLTg0M2YtZTU1ZjE3MzE4YjAyIiwidCI6ImE0MGMwZDY4LTMzOGUtNDRlZi1hYjE3LTgxMmVlNDJkMTJjNyIsImMiOjh9" 
            frameborder="0" allowfullscreen="true"></iframe>
</div>
"""

# Use components.html to render the iframe
components.html(dashboard_url, height=1000)

