# English to Hindi-Urdu Parallel Translation Playground

A simple playground to understand & learn the subtle differences in the dialect-pair Hindi & Urdu.

The deployed demo application is available here:  
https://share.streamlit.io/gokulnc/english-hindurdu-parallel-translator/app.py

## Installing dependencies

0. Ensure you have Python 3.6+ installed
1. `pip install -r requirements.txt`

## Running the UI

```
streamlit run app.py
```

## Note

- Please raise an issue here on this repo if the translator doesn't work.
- Use [this discussion thread](https://discuss.streamlit.io/t/hindurdu-translator-learn-hindi-to-urdu-or-urdu-to-hindi-yourself/9681) for other ideas or improvement.

## Credits

- [Library for Google Translation](https://github.com/UlionTse/translators)
  - This free API does not give high quality results
- Library for Transliteration: [Indic-Trans](https://github.com/libindic/indic-trans)
  - For approximate Hindi-Urdu Script conversion
- Library for Web UI: [StreamLit](https://docs.streamlit.io/)
  - For easy and free hosting on *Streamlit Sharing*
