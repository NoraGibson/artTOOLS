import random
import streamlit as st

#set up the page:
st.set_page_config(
    page_title="Contemporary Ballet Choreography Tool", 
    page_icon="🩰", 
    layout="wide"
)

#set up the session states:
if 'current_step' not in st.session_state:
    st.session_state.current_step = "[Step]"

if 'current_modifier' not in st.session_state:
    st.session_state.current_modifier = "[Modifier]"

if 'current_facing' not in st.session_state:
    st.session_state.current_facing = "[Facing]"
if 'saved_sequence' not in st.session_state:
    st.session_state.saved_sequence = []  



ballet_terms = ["Allongé", "Arabesque", "Assemblé", "Attitude", "Balancé", "Ballonné", "Ballotté", "Battement", "Battement dégagé", "Battement développé", "Battement fondu", "Battement frappé", "Battement jeté", "Battement lent", "Battement tendu", "Battu", "Bourrée", "Brisé", "Cabriole", "Cambré", "Chaînés", "Changé", "Changement", "Chassé", "Ciseaux (pas de)", "Coupé", "Dégagé", "Demi-plié", "Détourné", "Développé", "Échappé", "Entrechat quatre", "Entrechat trois", "Entrechat cinq","Failli", "Fondu", "Fouetté", "Frappé", "Glissade", "Grand battement", "Grand Fouetté","Grand jeté", "Grand plié", "Grand port de bras", "Jeté", "Jeté entrelacé", "Manèges", "Pas de basque", "Pas de bourrée", "Pas de bourrée en tournant","Pas de chat", "Pas de cheval", "Passé", "Penché", "Petit battement", "Piqué", "Piqué en dehors (lame duck)","Pirouette (en de hors)", "Pirouette (en dedans)","Plié", "Port de bras", "Promenade", "Relevé", "Renversé", "Retiré", "Rond de jambe", "Rond de jambe à terre", "Rond de jambe en l’air", "Sauté", "Saut de basque", "Saut de chat", "Sissonne ferme", "Sissonne overt", "Sous-sus", "Soubresaut", "Soutenu", "Sur le cou-de-pied", "Temps lié", "Temps levé", "Temps de cuisse","Tendu", "Tombé", "Tour en l’air", "Tour jeté"]

modifiers = ["Blur", "Burst", "Collapse", "Coil", "Contract", "Crystallize", "Crumble", "Detach", "Dim", "Disintegrate", "Dissolve", "Distill", "Drift", "Echo", "Erode", "Expand outward", "Fade", "Flick", "Flicker", "Float", "Fluctuate", "Flow", "Flutter", "Fold", "Freeze", "Fragment", "Glitch", "Glow", "Hover", "Inflate", "Invert", "Jerk", "Magnetize", "Mesh", "Melt", "Multiply", "Pause", "Perforate", "Pixelate", "Pop", "Pulse", "Pulse in", "Pulse out", "Punctuate", "Quiver", "Radiate", "Reverse", "Rotate", "Scatter", "Shake", "Shatter", "Shimmer", "Shudder", "Skitter", "Slide", "Smear", "Snap", "Snap open", "Snap shut", "Soften", "Sous-sus", "Spiral", "Spiral inward", "Spiral outward", "Strobe", "Stretch", "Suspend", "Swell", "Swipe", "Tangle", "Teeter", "Tilt", "Undulate", "Vibrate", "Warp", "Wave", "Zig-zag"]

facings = ["Croisé", "Écarté", "Éffacé", "En face"]

#Takes a list and returns a random item from it:
def get_random_item(item_list):
    return random.choice(item_list)


def add_to_sequence():
    if(st.session_state.current_step != "[Step]" and st.session_state.current_modifier != "[Modifier]" and st.session_state.current_facing != "[Facing]"):
        st.session_state.saved_sequence.append({
            "step": st.session_state.current_step, 
            "modifier": st.session_state.current_modifier, "facing": st.session_state.current_facing})
    else:
        st.warning("Complete your selections")
    

#Removes the last tuple in the sequence:
def remove_last():
    if st.session_state.saved_sequence:
        st.session_state.saved_sequence.pop()
    

#Main app:
def main():

    migrated = []
    for item in st.session_state.saved_sequence:
        if isinstance(item, dict):
            migrated.append(item)
        elif isinstance(item, tuple):
            if len(item) == 3:
                step, mod, facing = item
                migrated.append({"step": step, "modifier": mod, "facing": facing})
            elif len(item) == 2:
                step, mod = item
                migrated.append({"step": step, "modifier": mod, "facing": "[Facing]"})
    st.session_state.saved_sequence = migrated
    
    # NEW: Custom font styling
    st.markdown("""
    <style>
        * {
            font-family: 'Arial', sans-serif;
        }
    </style>
    """, unsafe_allow_html=True)

    #title:
    st.title("Choreography Tool for Contemporary Ballet")

    #layout:
    col1, col2 = st.columns([1,2])
    
    with col1:
        st.subheader("Select")
    
        #button for steps:
        if st.button("Choose a step", key="choose_step"):
            st.session_state.current_step = get_random_item(ballet_terms)
        st.info(st.session_state.current_step)
                
        #button for modifiers:    
        if st.button("Modify your step", key="modify_step"):
            st.session_state.current_modifier = get_random_item(modifiers)
        st.info(st.session_state.current_modifier)

        if st.button("Choose a facing", key="choose_facing"):
            st.session_state.current_facing = get_random_item(facings)
        st.info(st.session_state.current_facing)

        st.button("Add to sequence", key="add_sequence", on_click=add_to_sequence)


    with col2:
        st.subheader("Saved Sequence")

        if st.session_state.saved_sequence:
            for idx, item in enumerate(st.session_state.saved_sequence, start=1):
                step = item["step"]
                mod = item["modifier"]
                facing = item["facing"]
                st.write(f"{idx}. {step} ({mod}) - Facing: {facing}")
            else:
                st.write("Your sequence will appear here ...")


        #remove last step/mod pair:
        if st.session_state.saved_sequence:
           st.button("Remove last", key="remove_last", on_click=remove_last)
        else:
            st.info("Sequence is empty")


        if st.session_state.saved_sequence:
                lines = ["Choreographic Sequence", "--------------------"]
                for idx, item in enumerate(st.session_state.saved_sequence, start=1):
                    step = item["step"]
                    mod = item["modifier"]
                    facing = item["facing"]
                    lines.append(f"{idx}. {step} ({mod}) - Facing: {facing}")
                file_content = "\n".join(lines)
                st.download_button(
                    label="Download Sequence",
                    data=file_content,
                    file_name="choreographic-sequence.txt",
                    mime="text/plain"
            ) 
        else:
            st.info("No sequence to download")

st.markdown("""
<style>
.footer-link {
  position: fixed !important;
  bottom: 12px !important;
  left: 12px !important;
  font-size: 13px !important;
  z-index: 9999 !important;
  background: rgba(255,255,255,0.8);
  padding: 4px 8px;
  border-radius: 6px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.2);
}
.footer-link a {
  color: #1a0dab !important;
  text-decoration: none !important;
  font-weight: 500;
}
.footer-link a:hover {
  text-decoration: underline !important;
}
</style>
<div class="footer-link">
  <a href="https://noragibsonvisualist.com" target="_blank" rel="noopener">
    noragibsonvisualist.com
  </a>
</div>
            
""", unsafe_allow_html=True)


#run the main function:
if __name__ == "__main__":
    main()