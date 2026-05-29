import os
from dotenv import load_dotenv
from supabase import create_client

caminho_env = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(caminho_env)

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = create_client(url, key)

resposta = supabase.table("teste").select("*").execute()
print("Dados da nuvem:", resposta.data)