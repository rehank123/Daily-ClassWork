import streamlit as st

def option_menu(title, options, icons, default_index):
    selected_option = st.sidebar.radio(
        title,
        options=options,
        format_func=lambda x: f'<span style="vertical-align:middle;"><i class="material-icons">{icons[options.index(x)]}</i></span> {x}',
        index=default_index
    )
    return selected_option

if __name__ == "__main__":
    selected = option_menu("Main Menu", ["Home", "Settings"], icons=['house', 'gear'], default_index=1)
    selected
