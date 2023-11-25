import streamlit as st  # 모든 streamlit 명령은 "st" alias로 사용할 수 있습니다.
# import bedrock as glib  # 로컬 라이브러리 스크립트에 대한 참조
# from langchain.callbacks import StreamlitCallbackHandler


st.title("💬 Knox Manage API reference")   #page 제목
st.subheader('Search documentation', divider='blue')
st.caption("Welcome to the reference for the Knox Manage Open API. The Knox Manage Open API provides a broad set of operations and resources that: 1) User, device, organization, group management 2) Apply policies to users, groups, organizations, and devices 3) User authentication, etc.")

prompt = st.chat_input("Serach documentation")
if prompt:
    with st.chat_message("user"):
        st.write(f"{prompt}")
    with st.spinner("Working..."):
        # st_callback = StreamlitCallbackHandler(st.container())
        # response_content = glib.get_rag_chat_response(
        #     input_text=prompt, streaming_callback=st_callback)
        message = st.chat_message("assistant")
        message.write(response_content)


with st.chat_message("user"):
    st.write("How to add my company logo to my app?")
message = st.chat_message("assistant")
message.write("Set the logo")
message.write("The image must be a GIF, JPG, PNG or BMP file. The file cannot be larger than 190 X 33 and must be 1 MB or lower. Click Default to use the default image as your company logo.")
message.write(
    "https://docs.samsungknox.com/admin/knox-manage/configure/advanced-settings/set-the-logo")
with st.chat_message("user"):
    st.write(
        "Okay, I'm not uploading an image to my app, but want to add an icon for my windows app.")
message = st.chat_message("assistant")
message.write("Add internal Windows apps")
message.write("Click the frame to open a file dialog, then select an image from your file system. The icon can be a JPG or PNG file and must not exceed 5MB in size.")
message.write(
    "https://docs.samsungknox.com/admin/knox-manage/configure/applications/add-applications/add-internal-windows-app")
