from pathlib import Path
from typing import List, Any
from langchain_community.document_loaders import PyMuPDFLoader, TextLoader, CSVLoader


Sample_data_path= "..\\data"

def load_all_documents(data_dir: str) -> List[Any]:

    """lets load doc here"""

    data_path= Path(data_dir).resolve()
    print(f"[debug] data path: {data_path}")
    documents=[]
    

    # load pdf files
    pdf_files= list(data_path.glob('**/*.pdf'))
    print(f'found {len(pdf_files)} pdf')

    for pdf_file in pdf_files:
        try:
            loader = PyMuPDFLoader(pdf_file)
            loaded = loader.load()
            print(f"loaded {pdf_file}")
            documents.extend(loaded)
        except:
            print(f'[error] while loading pdf{pdf_file}')    


    # load csv etc. later


    print(f"[DEBUG] Total loaded documents: {len(documents)}")
    return documents



#debug
#docs= load_all_documents(Sample_data_path)
#print(f"[debug] loaded docs: {docs[0]}")








