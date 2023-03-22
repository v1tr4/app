import streamlit as st

#Text elements:

# Title
st.title('Streamlit app 1st attempt')
# Header
st.header('ini bagian headernya')
# Subheader
st.subheader(" Ini bagian subheader ")
# Markdown
st.markdown(' # markdown1 ')
st.markdown(' ## markdown2 ')
st.markdown(' ### markdown3 ')
st.markdown(' ##### markdown4 ')

# markdown multi baris 
st.markdown("""
  # test1
  ## test 2
  ### test 3
  """, True)


# Caption


# Code block

st.code("y = mx + c")

# Text
st.text("This is a trial project !")

# LaTeX

st.latex("\ int a y^2 \ , dy")


