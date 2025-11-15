
from data_loader import load_all_documents
from vectorstore import FaissVectorStore




docs= load_all_documents("..\\data")

building=FaissVectorStore()

building.build_from_documents(documents=docs)


