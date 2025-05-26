from google import genai

client = genai.Client(api_key="AIzaSyC46-pzZLDSNG_ZS9ZCQH_Ad8XpIkSMd7k")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)
print(response.text)


# AIzaSyDX1hkB7aiZjXr-dm7wUux0dun9w8_LwMI-cst
# AIzaSyD4nCq4FYeUZwPqX4Pf4TttgikkEC1z6c8-ly
# AIzaSyC46-pzZLDSNG_ZS9ZCQH_Ad8XpIkSMd7k-mine
#AIzaSyBNo8P7UDowKjYllzPJSlxYbOI1fR82SsM-lzx
#AIzaSyCcfcy3bkSeqfpNZ5ALqqQ2-RlBNrIQfyE-hunter