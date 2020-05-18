# from util import *

# # Add your import statements here

# import numpy as np


# class InformationRetrieval():

# 	def __init__(self):
# 		self.index = None
# 		self.word_list = None
# 		self.tfidf_matrix = None 

# 	def buildIndex(self, docs, docIDs):
# 		"""
# 		Builds the document index in terms of the document
# 		IDs and stores it in the 'index' class variable

# 		Parameters
# 		----------
# 		arg1 : list
# 			A list of lists of lists where each sub-list is
# 			a document and each sub-sub-list is a sentence of the document
# 		arg2 : list
# 			A list of integers denoting IDs of the documents
# 		Returns
# 		-------
# 		None
# 		"""

# 		#Fill in code here
# 		word_list=list(set(word for doc in docs for sentence in doc for word in sentence))
		
# 		Nd=len(docs)
# 		Nw=len(word_list)
		
# 		tfidf_matrix=np.zeros((Nw,Nd))
# 		tf_matrix=np.zeros((Nw,Nd))
# 		idf_matrix = np.zeros((Nw,Nd))

# 		for i in range(len(docIDs)) : 
# 			doc = docs[i]

# 			if not len(doc) == 0 : 
# 				flatten_doc = list(set(sum(doc,[])))
# 				for j in flatten_doc : 
# 					index_word = word_list.index(j)
# 					idf_matrix[:,index_word] + = 1 

# 				for j in range(len(doc)) : 
# 					sentence = doc[j]

# 					for k in range(len(sentence)) : 
# 						index_word = word_list.index(sentence[k])
# 						tf_matrix[i,index_word] + = 1

# 		idf_matrix = -np.log(idf_matrix/len(docIDs))

# 		self.tfidf_matrix = tf_matrix * idf_matrix
# 		self.index = [int(x) for x in docIDs]
# 		self.word_list=word_list

# 	def rank(self, queries):
# 		"""
# 		Rank the documents according to relevance for each query

# 		Parameters
# 		----------
# 		arg1 : list
# 			A list of lists of lists where each sub-list is a query and
# 			each sub-sub-list is a sentence of the query
		

# 		Returns
# 		-------
# 		list
# 			A list of lists of integers where the ith sub-list is a list of IDs
# 			of documents in their predicted order of relevance to the ith query
# 		"""

# 		doc_IDs_ordered = []

# 		#Fill in code here
# 		modDocs=np.sqrt(np.sum(self.tfidf_matrix**2 , 1)).reshape(-1,1)
		
# 		Q=np.zeros((len(self.word_list),1))
		
# 		for query in queries:
# 			for sentence in query:
# 				for word in sentence:
# 					if (word in self.word_list):
# 						Q[self.word_list.index(word)]+=1
			
# 			modQ=np.sqrt(np.sum(Q**2))

# 			weights = None
# 			weights = np.dot(self.tfidf_matrix,Q)/modQ
# 			for i in range(weights.shape[0]) : 
# 				if not modDocs[i] == 0 :  
# 					weights[i] = weights[i]/modDocs[i]
# 				else : 
# 					weights[i] = 0	


# 			#weights=np.sum(self.index*Q[:,None],0)/(modQ)/modDocs
			
# 			sortedq=[]
# 			while(len(weights)!=0):
# 				sortedq.append(self.index[np.argmax(weights)])
# 				weights=np.delete(weights,np.argmax(weights))
# 			doc_IDs_ordered.append(sortedq)

# 		print(doc_IDs_ordered[0])	
# 		return doc_IDs_ordered




