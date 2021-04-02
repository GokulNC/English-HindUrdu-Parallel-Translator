import streamlit as st

@st.cache(allow_output_mutation=True)
def get_converters():
    from google_trans_new import google_translator
    from indictrans import Transliterator
    converters = {
        'g_translator': google_translator(url_suffix="com.pk"),
        'hi2ur': Transliterator(source='hin', target='urd', rb=False),#, build_lookup=True),
        'ur2hi': Transliterator(source='urd', target='hin', rb=False),#, build_lookup=True),
        'hi2en': Transliterator(source='hin', target='eng', rb=False),#, build_lookup=True),
        'ur2en': Transliterator(source='urd', target='eng', rb=False),#, build_lookup=True),
    }
    return converters

def write_header():
    st.title('English-HindUrdu Parallel Translator')
    st.markdown('''
        - A simple playground to understand & compare the subtle differences in the dialect-pair Hindi & Urdu.  
        - Will be useful to learn Urdu if you already know Hindi, or learn Hindi if you already know Urdu.
    ''')

def write_matrix(outputs):
    table_md = f'''
    |Script/Language|Hindi|Urdu|
    |--|--|--|
    |DevaNāgarī|**{outputs['hi']}**|{outputs['u2h']}|
    |PersoArabic|{outputs['h2u']}|**{outputs['ur']}**|
    |Roman (Approx)|{outputs['h2e']}|{outputs['u2e']}|
    '''
    st.markdown(table_md)

def write_ui():
    eng_txt = st.text_input('Enter English sentence below and hit Enter', value="India's national language Hindi, and Pakistan's national language Urdu are almost the same.")
    if not eng_txt:
        return
    converters = get_converters()
    outputs = {
        'hi': converters['g_translator'].translate(eng_txt, lang_src='en', lang_tgt='hi'),
        'ur': converters['g_translator'].translate(eng_txt, lang_src='en', lang_tgt='ur')
    }
    outputs['h2u'] = converters['hi2ur'].transform(outputs['hi'])
    outputs['u2h'] = converters['ur2hi'].transform(outputs['ur'])
    outputs['h2e'] = converters['hi2en'].transform(outputs['hi'])
    outputs['u2e'] = converters['ur2en'].transform(outputs['ur'])
    write_matrix(outputs)

def write_footer():
    st.markdown('''
        ### Note
        
        - The cells in bold are the Google translations.
        - The cross-script conversions may not be accurate.
        - This work is [open-sourced here](https://github.com/GokulNC/English-HindUrdu-Parallel-Translator).
        
        ### Interesting Facts
        
        - Hindi and Urdu together was a single same spoken language called [Hindustani](https://en.wikipedia.org/wiki/Hindustani_language), but now unfortunately divided because of communal (🕉️-☪️) and political (🇮🇳-🇵🇰) reasons.
        - Hindi-Urdu is the [third most spoken language in the world](https://www.ethnologue.com/guides/ethnologue200) with more than 800 million speakers.
        - To learn about Hindi-Urdu script conversion, [check this paper](http://www.learnpunjabi.org/pdf/paper248.pdf).
    ''')

def production_mode():
    # Src: discuss.streamlit.io/t/how-do-i-hide-remove-the-menu-in-production/362
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    return

if __name__ == '__main__':
    st.set_page_config(page_title='English-HindUrdu Translator', page_icon='☮️', layout='wide')
    production_mode()
    write_header()
    write_ui()
    write_footer()
