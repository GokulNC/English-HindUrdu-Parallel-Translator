import streamlit as st

@st.cache(allow_output_mutation=True)
def get_converters():
    from google_trans_new import google_translator
    from indictrans import Transliterator
    converters = {
        'g_translator': google_translator(url_suffix="pk"),
        'hi2ur': Transliterator(source='hin', target='urd', rb=False),#, build_lookup=True),
        'ur2hi': Transliterator(source='urd', target='hin', rb=False),#, build_lookup=True),
        'hi2en': Transliterator(source='hin', target='eng', rb=False),#, build_lookup=True),
        'ur2en': Transliterator(source='urd', target='eng', rb=False),#, build_lookup=True),
    }
    return converters

def write_header():
    st.title('English-HindUrdu Parallel Translator')
    st.markdown('A simple playground to understand & learn the subtle differences in the dialect-pair Hindi & Urdu.')

def write_matrix(outputs):
    table_md = f'''
    |Script/Language|Hindi|Urdu|
    |--|--|--|
    |DevaNāgarī|**{outputs['hi']}**|{outputs['u2h']}|
    |PersoArabic|{outputs['h2u']}|**{outputs['ur']}**|
    |Latin (Approx)|{outputs['h2e']}|{outputs['u2e']}|
    '''
    st.markdown(table_md)

def write_ui():
    eng_txt = st.text_input('Enter English sentence below and hit Enter', value='I am an Indian who speaks Urdu.')
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
        
        - The cells in bold are the original translations.
        - The cross-script transliterations may not be exact.
        - This work is [open-sourced here](https://github.com/GokulNC/English-HindUrdu-Parallel-Translator).
        
        ### Interesting Facts
        
        - Hindi and Urdu together is a single same spoken language called [Hindawi](https://en.wikipedia.org/wiki/Hindustani_language), but still unfortunately divided in reality because of communal (🕉️-☪️) and political (🇮🇳-🇵🇰) reasons.
        - Hindi-Urdu is the [third most spoken language in the world](https://www.ethnologue.com/guides/ethnologue200) with more than 800 million speakers.
    ''')

if __name__ == '__main__':
    st.set_page_config(page_title='English-HindUrdu Translator', page_icon='☮️', layout='wide')
    write_header()
    write_ui()
    write_footer()
