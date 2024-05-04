import streamlit as st
import functions

todo=functions.read_todos()

def add_todo():
    new=st.session_state['new_todo'] + '\n'
    todo.append(new)
    functions.write_todos(todo)
st.title("My todos")
st.subheader("This is my todos app")
st.write("Hello")


for index,i in enumerate(todo):
    checkbox=st.checkbox(i,key=i)
    if checkbox:
        todo.pop(index)
        functions.write_todos(todo)
        st.experimental_rerun()

st.text_input(label='Enter todo',placeholder="Add a new todo...",
              on_change=add_todo,key='new_todo')
st.session_state