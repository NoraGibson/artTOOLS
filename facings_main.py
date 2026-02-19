import streamlit as st
import random

# -------------------------------------------------
# PAGE SETUP
# -------------------------------------------------
st.set_page_config(
    page_title="Ballet Flashcards",
    layout="centered"
)

# -------------------------------------------------
# STYLE (mobile friendly)
# -------------------------------------------------
st.markdown("""
<style>
.stButton button {
    background-color: #ffd6e7;
    color: black;
    border-radius: 14px;
    height: 3em;
    font-size: 18px;
}
.title {
    text-align:center;
    font-size:32px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# DATA LIBRARIES
# -------------------------------------------------

FACINGS = {
    "Croisé devant": {
        "image": "images/crdev.png",
        "description": "Facing front diagonal, front leg is extended in tendu/devant, legs are crossed."
    },
    "Effacé devant": {
        "image": "images/efdev.png",
        "description": "Facing front diagonal, working leg is extended in front but is open (uncrossed)."
    },
    "En face": {
        "image": "images/enfac.png",
        "description": "Facing directly front, the working leg is extended to the side."
    },
    "Croisé derrière": {
        "image": "images/crder.png",
        "description": "Working leg is extended behind toward back diagonal, legs are crossed."
    },
    "Écarté devant": {
        "image": "images/ecdev.png",
        "description": "Facing front diagonal, working leg extended in second position pointing toward the front corner."
    },
    "Écarté derrière": {
        "image": "images/ecder.png",
        "description": "Facing front diagonal, working leg extended in second position pointing toward the back corner."
    },
    "Effacé derrière": {
        "image": "images/efder.png",
        "description": "Working leg is extended behind toward back diagonal, but is open."
    }
}

ARABESQUES = {
    "First Arabesque": {"image": "images/1ar.png"},
    "Second Arabesque": {"image": "images/2ar.png"},
    "Third Arabesque": {"image": "images/3ar.png"},
    "Third Arabesque (Russian)": {"image": "images/3arv.png"},
    "Fourth Arabesque": {"image": "images/4ar.png"},
}

# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------
def init_state():
    defaults = {
        "mode": "menu",
        "deck": [],
        "current": None,
        "show_description": False,
        "show_image": False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()


# -------------------------------------------------
# FLASHCARD LOGIC
# -------------------------------------------------
def new_deck(source):
    deck = list(source.keys())
    random.shuffle(deck)
    return deck


def next_card(source):
    if not st.session_state.deck:
        st.session_state.deck = new_deck(source)

    st.session_state.current = st.session_state.deck.pop()
    st.session_state.show_description = False
    st.session_state.show_image = False


def back_to_menu():
    st.session_state.mode = "menu"
    st.session_state.deck = []
    st.session_state.current = None
    st.session_state.show_description = False
    st.session_state.show_image = False


# -------------------------------------------------
# MAIN MENU
# -------------------------------------------------
if st.session_state.mode == "menu":

    st.markdown('<div class="title"> Ballet Flashcards</div>',
                unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Facings"):
            st.session_state.mode = "facing"
            st.session_state.deck = new_deck(FACINGS)
            next_card(FACINGS)
            st.rerun()

    with col2:
        if st.button("Arabesques"):
            st.session_state.mode = "arabesque"
            st.session_state.deck = new_deck(ARABESQUES)
            next_card(ARABESQUES)
            st.rerun()

# -------------------------------------------------
# FACINGS VIEW
# -------------------------------------------------
elif st.session_state.mode == "facing":

    item = st.session_state.current
    data = FACINGS[item]

    st.header(item)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        if st.button("Description"):
            st.session_state.show_description = True

    with c2:
        if st.button("Image"):
            st.session_state.show_image = True

    with c3:
        if st.button("Next"):
            next_card(FACINGS)
            st.rerun()

    with c4:
        if st.button("⬅ Menu"):
            back_to_menu()
            st.rerun()

    if st.session_state.show_description:
        st.info(data["description"])

    if st.session_state.show_image:
        st.image(data["image"], use_container_width=True)

# -------------------------------------------------
# ARABESQUES VIEW
# -------------------------------------------------
elif st.session_state.mode == "arabesque":

    item = st.session_state.current
    data = ARABESQUES[item]

    st.header(item)

    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button("Image"):
            st.session_state.show_image = True

    with c2:
        if st.button("Next"):
            next_card(ARABESQUES)
            st.rerun()

    with c3:
        if st.button("⬅ Menu"):
            back_to_menu()
            st.rerun()

    if st.session_state.show_image:
        st.image(data["image"], use_container_width=True)