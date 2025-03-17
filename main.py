import streamlit as st
import json

# load and save library data

def load_library():
    try:
        with open("library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
    
def save_library():
    with open("library.json", "w") as file:
        json.dump(library,file,indent=4)

# initialize library
library = load_library()

st.title("Personal Library Manager")

menu = st.sidebar.radio("Select an option", ["View Library","Add a Book","Remove Book","Search Book","Save and Exit"])

# Display statistics
st.sidebar.title("Library Statistics")
total_books = len(library)
read_books = len([book for book in library if book["read_status"]])
if total_books > 0:
    read_percentage = (read_books / total_books) * 100
else:
    read_percentage = 0
st.sidebar.write(f"Total books: {total_books}")
st.sidebar.write(f"Read books: {read_books} ({read_percentage:.2f}%)")

if menu == "View Library":
    st.sidebar.title("Your Library")
    if library:
        st.table(library)
    else:
        st.write("No books in your library. Add some books!")

#add book
elif menu == "Add a Book":
    st.sidebar.title("Add a new book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Year", min_value=2000, max_value=2100,step=1)
    genre = st.text_input("Genre")
    read_status = st.checkbox("Mark as Read")

    if st.button("Add Book"):
        library.append({"title": title,"author": author,"year": year,"genre": genre,"read_status": read_status})
        save_library()
        st.success("Book added successfully!")
        st.rerun()

# Remove book
elif menu == "Remove Book":
    st.sidebar.title("Remove a book")
    book_title = [book["title"] for book in library]

    if book_title:
        selected_book = st.selectbox("Select a book to remove", book_title)
        if st.button("Remove Book"):
            library = [book for book in library if book["title"]!= selected_book]
            save_library()
            st.success("Book removed successfully!")
            st.rerun()
    else:
        st.warning("No books in your library. Add some books!")

# Search book
elif menu == "Search Book":
    st.sidebar.title("Search a book")
    search_term = st.text_input("Enter title or author name")

    if st.button("Search"):
        results = [book for book in library if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower()]
        if results:
            st.table(results)
        else:
            st.warning("No books found!")

# Save and Exit
elif menu == "Save and Exit":
    save_library()
    st.success("Library saved successfully!")




