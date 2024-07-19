import streamlit as st
import time

# Set the page configuration with a custom title and star icon
st.set_page_config(
    page_title="Krishna Dua Python Tutorial",
    page_icon="⭐"  # Unicode star character
)

# Add custom CSS for styling and effects
st.markdown("""
    <style>
    .header {
        font-size: 24px;
        color: white;
        background-color: #007BFF;
        text-align: center;
        padding: 20px;
        position: fixed;
        width: calc(100% - 0px);
        top: 30px;
        left: 0;
        transition: all 0.3s ease-in-out;
        z-index: 1000;
    }
    .header:hover {
        background-color: #0056b3;
        transform: scale(1.05);
    }
    .footer {
        font-size: 14px;
        color: white;
        background-color: #007BFF;
        text-align: center;
        padding: 10px;
        position: fixed;
        width: 100%;
        bottom: 0;
        left: 0;
        marg-top:-400px;
    }
    .content {
            margin-top:-200px;
        padding-top: 80px; /* Adjust this value based on the height of your header */
        padding-bottom: 50px; /* Adjust this value based on the height of your footer */
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
        padding: 20px;
        border-right: 1px solid #ddd;
        height: 100%;
    }
    .sidebar .sidebar-content h1 {
        font-size: 24px;
        color: #333;
    }
    .sidebar .sidebar-content a {
        color: #007BFF;
        text-decoration: none;
        display: block;
        margin: 10px 0;
        transition: color 0.3s ease;
    }
    .sidebar .sidebar-content a:hover {
        color: #0056b3;
    }
    .confetti {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 999;
        overflow: hidden;
    }
    .confetti div {
        position: absolute;
        width: 10px;
        height: 10px;
        background: #FF6347;
        opacity: 0;
        transform: rotate(45deg);
        animation: confetti 3s ease-in-out infinite;
    }
    @keyframes confetti {
        0% {
            transform: translateY(0) rotate(45deg);
            opacity: 1;
        }
        100% {
            transform: translateY(100vh) rotate(45deg);
            opacity: 0;
        }
    }
    .spinner {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        border: 8px solid #f3f3f3;
        border-top: 8px solid #007BFF;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        animation: spin 1s linear infinite;
    }
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    @media (max-width: 768px) {
        .header {
            font-size: 20px;
            padding: 15px;
        }
        .footer {
            font-size: 12px;
            padding: 8px;
        }
        .content {
            padding-top: 70px;
            padding-bottom: 40px;
        }
        .sidebar .sidebar-content {
            padding: 15px;
        }
        .sidebar .sidebar-content h1 {
            font-size: 20px;
        }
    }
    @media (max-width: 480px) {
        .header {
            font-size: 18px;
            padding: 10px;
        }
        .footer {
            font-size: 10px;
            padding: 6px;
        }
        .content {
            padding-top: 60px;
            padding-bottom: 30px;
        }
        .sidebar .sidebar-content {
            padding: 10px;
        }
        .sidebar .sidebar-content h1 {
            font-size: 18px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# JavaScript to inject confetti and spinner
st.markdown("""
    <script>
    window.onload = function() {
        // Create confetti effect
        let confettiContainer = document.createElement('div');
        confettiContainer.className = 'confetti';
        document.body.appendChild(confettiContainer);

        for (let i = 0; i < 100; i++) {
            let confettiPiece = document.createElement('div');
            confettiPiece.style.left = Math.random() * 100 + 'vw';
            confettiPiece.style.backgroundColor = '#' + Math.floor(Math.random() * 16777215).toString(16);
            confettiPiece.style.animationDuration = Math.random() * 3 + 2 + 's';
            confettiContainer.appendChild(confettiPiece);
        }

        // Show spinner for 2 seconds
        let spinner = document.createElement('div');
        spinner.className = 'spinner';
        document.body.appendChild(spinner);
        setTimeout(() => {
            document.body.removeChild(spinner);
        }, 2000);
    };
    </script>
    """, unsafe_allow_html=True)

# Create the header
st.markdown('<div class="header">Krishna Dua Python Tutorial</div>', unsafe_allow_html=True)

# Create the sidebar
st.sidebar.title("Contents")
st.sidebar.markdown("""
- [Introduction](#introduction)
- [Variables](#variables)
- [Control Flow](#control-flow)
- [Functions](#functions)
- [Data Structures](#data-structures)
- [Modules and Packages](#modules-and-packages)
- [Conclusion](#conclusion)
""")

# Main content
st.markdown('<div class="content">', unsafe_allow_html=True)

# Introduction section
st.header("Introduction")
st.write("""
Welcome to this Python tutorial! This tutorial will guide you through the basics of Python programming. 
Python is a versatile language that you can use on the backend, frontend, or full stack of a web application.
""")

# Function to simulate code copying and trigger balloons
def copy_code():
    st.balloons()

# Variables section
st.header("Variables")
code_variables = '''# This is a comment
x = 10  # This is an integer
y = 20.5  # This is a float
z = "Hello"  # This is a string

print(x)
print(y)
print(z)
'''
st.code(code_variables, language='python')
if st.button("Copy code to clipboard", key="copy_variables"):
    copy_code()

# Control Flow section
st.header("Control Flow")
code_control_flow = '''# If statement
a = 10
if a > 5:
    print("a is greater than 5")

# For loop
for i in range(5):
    print(i)
'''
st.code(code_control_flow, language='python')
if st.button("Copy code to clipboard", key="copy_control_flow"):
    copy_code()

# Functions section
st.header("Functions")
code_functions = '''def greet(name):
    return "Hello, " + name

print(greet("Alice"))
'''
st.code(code_functions, language='python')
if st.button("Copy code to clipboard", key="copy_functions"):
    copy_code()

# Data Structures section
st.header("Data Structures")
code_data_structures = '''# List
my_list = [1, 2, 3, 4, 5]
print(my_list)

# Dictionary
my_dict = {"name": "Alice", "age": 25}
print(my_dict)

# Tuple
my_tuple = (1, 2, 3)
print(my_tuple)

# Set
my_set = {1, 2, 3, 4, 5}
print(my_set)
'''
st.code(code_data_structures, language='python')
if st.button("Copy code to clipboard", key="copy_data_structures"):
    copy_code()

# Modules and Packages section
st.header("Modules and Packages")
code_modules = '''# Importing a module
import math

print(math.sqrt(16))

# Creating a module
# In a file named my_module.py
def add(a, b):
    return a + b

# In another file
from my_module import add

print(add(5, 3))
'''
st.code(code_modules, language='python')
if st.button("Copy code to clipboard", key="copy_modules"):
    copy_code()

# Conclusion section
st.header("Conclusion")
st.write("""
Thank you for following this tutorial. We hope it was helpful in getting you started with Python programming. 
Continue practicing and exploring Python's vast ecosystem to become proficient.
""")

# End content div
st.markdown('</div>', unsafe_allow_html=True)

# Create the footer
st.markdown('<div class="footer">© 2024 Krishna Dua</div>', unsafe_allow_html=True)
