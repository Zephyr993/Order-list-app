import streamlit as st
import function


def add():
    todo = st.session_state['new'] + "\n"
    todos.append(todo)
    function.write_todos(todos)


todos = function.get_todos()
st.title("Grocery List")
st.header("My Grocery List")
st.write("This app is used to make your grocery list")
for i,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=f'todo_{i}')

    if checkbox:
         todos.pop(i)
         function.write_todos(todos)
         del st.session_state[f'todo_{i}']
         st.experimental_rerun()


ya =  st.text_input(label="Grocery List", placeholder="Enter your grocery list..",
              on_change=add, key='new')

