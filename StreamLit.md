---
Title: StreamLitCheatsheet 
Description: Contains important StreamLit commands and features which can be used to convert data scripts into interactive web apps.
Created At: 2022-10-02
---

For Documentation you can visit official site:
-https://docs.streamlit.io/library/cheatsheet


### How to install


```python
pip install streamlit
streamlit hello
```

### Import Streamlit

```python
import streamlit as st
```

### Add Widgets to Sidebar


```python st.sidebar.<widget>
a = st.sidebar.radio('R:',[1,2])
```
### Command Line

```python streamlit --help
streamlit run your_script.py
streamlit hello
streamlit config show
streamlit cache clear
streamlit docs
streamlit --version
pip uninstall streamlit
pip install streamlit-nightly --upgrade
```
### Display text

```python st.text('Fixed width text')
st.markdown('_Markdown_') # see *
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')
* optional kwarg unsafe_allow_html = True
st.caption('This is a small text')
```
### Display data

```python st.dataframe(my_dataframe)
st.table(data.iloc[0:10])
st.json({'foo':'bar','fu':'ba'})
```
### Display charts

```python st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)
st.pyplot(fig)
st.altair_chart(data)
st.vega_lite_chart(data)
st.plotly_chart(data)
st.bokeh_chart(data)
st.pydeck_chart(data)
st.deck_gl_chart(data)
st.graphviz_chart(data)
st.map(data)
```
### Display media

```python st.image('./header.png')
st.audio(data)
st.video(data)
```
### Display interactive widgets

```python st.button('Hit me')
st.checkbox('Check me out')
st.radio('Radio', [1,2,3])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
st.color_picker('Pick a color')
```
### Use widgets’ returned values in variables:

```python
>>> for i in range(int(st.number_input('Num:'))): foo()
>>> if st.sidebar.selectbox('I:',['f']) == 'f': b()
>>> my_slider_val = st.slider('Quinn Mallory', 1, 88)
>>> st.write(slider_val)
```
### Batch widgets together in a form:

```python 
>>> with st.form(key='my_form'):
>>> 	text_input = st.text_input(label='Enter some text')
>>> 	submit_button = st.form_submit_button(label='Submit')
```
### Control flow

```python 
st.stop()
```

### Lay out your app

```python 
st.container()
st.columns(spec)
>>> col1, col2 = st.columns(2)
>>> col1.subheader('Columnisation')
st.expander('Expander')
>>> with st.expander('Expand'):
>>>     st.write('Juicy deets')
```
### Display code

```python
st.echo()
>>> with st.echo():
>>>     st.write('Code will be executed and printed'
```

### Display progress and status

```python st.progress(progress_variable_1_to_100)
st.spinner()
>>> with st.spinner(text='In progress'):
>>>     time.sleep(5)
>>>     st.success('Done')
st.balloons()
st.error('Error message')
st.warning('Warning message')
st.info('Info message')
st.success('Success message')
st.exception(e)
```
### Placeholders, help, and options

```python st.empty()
>>> my_placeholder = st.empty()
>>> my_placeholder.text('Replaced!')
st.help(pandas.DataFrame)
st.get_option(key)
st.set_option(key, value)
st.set_page_config(layout='wide')
```
### Mutate data

```python DeltaGenerator.add_rows(data)
>>> my_table = st.table(df1)
>>> my_table.add_rows(df2)
>>> my_chart = st.line_chart(df1)
>>> my_chart.add_rows(df2)
```
### Optimize performance

```python 
@st.cache
>>> @st.cache
... def foo(bar):
...     # Mutate bar
...     return data
>>> # Executes d1 as first time
>>> d1 = foo(ref1)
>>> # Does not execute d1; returns cached value, d1==d2
>>> d2 = foo(ref1)
>>> # Different arg, so function d1 executes
>>> d3 = foo(ref2)
```
### Store data across reruns

```python st.title('Counter Example')
if 'count' not in st.session_state:
    st.session_state.count = 0
increment = st.button('Increment')
if increment:
    st.session_state.count += 1
st.write('Count = ', st.session_state.count)
```

### Magic commands


```python
# Magic commands implicitly `st.write()`
''' _This_ is some __Markdown__ '''
a=3
'dataframe:', data
```
