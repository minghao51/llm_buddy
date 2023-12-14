import streamlit as st

tab1, tab2, tab3 = st.tabs(["buttom_options", "picture_select", "html_display"])

with tab1:
        
    st.title('Counter Example')

    st.session_state['policy_type'] = st.selectbox('Select', [ 'CI','Term','Saving','Investment','Medical'], index=0)
    st.session_state['age'] = st.slider('Age', min_value=17, max_value=65)
    st.session_state['gender'] = st.radio('Gender:', ['Male','Female'])
    st.session_state['marital'] = st.radio('Marital:', ['Married','Single','Divorced'])

    st.write('policy_type = ', st.session_state['policy_type'])
    st.write('age = ', st.session_state['age'])
    st.write('gender = ', st.session_state['gender'])
    st.write('marital = ', st.session_state['marital'])

    # Streamlit runs from top to bottom on every iteraction so
    # we check if `count` has already been initialized in st.session_state.

    # If no, then initialize count to 0
    # If count is already initialized, don't do anything
    if 'count' not in st.session_state:
        st.session_state.count = 0

    # Create a button which will increment the counter
    increment = st.button('Increment')
    if increment:
        st.session_state.count += 1

    # A button to decrement the counter
    decrement = st.button('Decrement')
    if decrement:
        st.session_state.count -= 1

    st.write('Count = ', st.session_state.count)

with tab2:
    from streamlit_image_select import image_select
    img = image_select(
        label = "Label",
        images= ["images/cat1.jpeg", "images/cat2.jpeg", "images/cat3.jpeg","images/cat4.jpeg"],
        captions=["A cat", "Another cat", "Oh look, a cat!", "Guess what, a cat..."]
    )
    st.write(img)
    st.write(str(img)[:100])

with tab3:
    import streamlit.components.v1 as components

    # bootstrap 4 collapse example
    components.html(
        """
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        <div id="accordion">
        <div class="card">
            <div class="card-header" id="headingOne">
            <h5 class="mb-0">
                <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                Collapsible Group Item #1
                </button>
            </h5>
            </div>
            <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
            <div class="card-body">
                Collapsible Group Item #1 content
            </div>
            </div>
        </div>
        <div class="card">
            <div class="card-header" id="headingTwo">
            <h5 class="mb-0">
                <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                Collapsible Group Item #2
                </button>
            </h5>
            </div>
            <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
            <div class="card-body">
                Collapsible Group Item #2 content
            </div>
            </div>
        </div>
        </div>
        """,
        scrolling=True,
        height=600,
    )
    